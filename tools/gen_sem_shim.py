import os
import re

# Collect all call sites and their exact forms
call_sites = []
pattern = re.compile(r'invoke-(virtual|static)(/range)?\s+\{([^}]+)\},\s*(Landroid/[a-zA-Z0-9_/$]+;)->(sem[a-zA-Z0-9_]+)\(([^)]*)\)([a-zA-Z0-9_/[;]*)')

methods_needed = {}

for root, dirs, files in os.walk('decompiled_clock'):
    for f in files:
        if f.endswith('.smali'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    m = pattern.search(line)
                    if m:
                        itype, is_range, regs, cls, name, args, ret = m.groups()
                        key = (name, args, ret, itype == 'static')
                        if key not in methods_needed:
                            methods_needed[key] = {
                                'name': name,
                                'args': args,
                                'ret': ret,
                                'is_static': (itype == 'static'),
                                'cls': cls
                            }

print(f"Total distinct methods needed in SemShim: {len(methods_needed)}")

# Generate SemShim.java
java_lines = [
    "package com.samsung.android.util;",
    "",
    "import android.app.Activity;",
    "import android.media.AudioManager;",
    "import android.os.Build;",
    "",
    "public class SemShim {",
]

def smali_type_to_java(t):
    if t == 'V': return 'void'
    if t == 'Z': return 'boolean'
    if t == 'I': return 'int'
    if t == 'J': return 'long'
    if t == 'F': return 'float'
    if t == 'D': return 'double'
    if t == 'C': return 'char'
    if t == 'B': return 'byte'
    if t == 'S': return 'short'
    if t.startswith('['): return 'Object'
    if t.startswith('L'): return 'Object'
    return 'Object'

def parse_args(args_str):
    args = []
    i = 0
    while i < len(args_str):
        if args_str[i] in 'ZBCSIJFD':
            args.append(args_str[i])
            i += 1
        elif args_str[i] == '[':
            start = i
            while i < len(args_str) and args_str[i] == '[':
                i += 1
            if i < len(args_str) and args_str[i] == 'L':
                while i < len(args_str) and args_str[i] != ';':
                    i += 1
                i += 1
            else:
                i += 1
            args.append(args_str[start:i])
        elif args_str[i] == 'L':
            start = i
            while i < len(args_str) and args_str[i] != ';':
                i += 1
            i += 1
            args.append(args_str[start:i])
        else:
            i += 1
    return args

for key, info in sorted(methods_needed.items()):
    name = info['name']
    args = info['args']
    ret = info['ret']
    is_static = info['is_static']
    
    arg_types = parse_args(args)
    params = []
    if not is_static:
        params.append("Object obj")
    for idx, at in enumerate(arg_types):
        jt = smali_type_to_java(at)
        params.append(f"{jt} p{idx}")
    
    jret = smali_type_to_java(ret)
    param_str = ", ".join(params)
    
    # Body logic
    if jret == 'void':
        body = "{}"
    elif jret == 'boolean':
        if name in ('semIsResumed', 'semIsUriValid', 'semIsDefaultFontStyle'):
            body = "{ return true; }"
        else:
            body = "{ return false; }"
    elif jret == 'int':
        if name == 'semGetVibrationIndex':
            body = "{ return p0; }"
        elif name == 'semGetActiveStreamType':
            body = "{ return 4; }"
        elif name == 'semGetRingerModeInternal':
            body = "{ if (obj instanceof AudioManager) return ((AudioManager)obj).getRingerMode(); return 2; }"
        else:
            body = "{ return 0; }"
    elif jret == 'long':
        body = "{ return 0L; }"
    elif jret == 'float':
        body = "{ return 0.0f; }"
    elif jret == 'double':
        body = "{ return 0.0; }"
    else:
        # Object
        if ret == 'Ljava/lang/String;':
            body = '{ return ""; }'
        else:
            body = "{ return null; }"
            
    java_lines.append(f"    public static {jret} {name}({param_str}) {body}")

java_lines.append("}")

with open("stubs_src/com/samsung/android/util/SemShim.java", "w", encoding="utf-8") as f:
    f.write("\n".join(java_lines))

print(f"Generated SemShim.java with {len(methods_needed)} methods")
