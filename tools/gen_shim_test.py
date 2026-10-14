import os
import re

signatures = set()
for root, dirs, files in os.walk('decompiled_clock'):
    for f in files:
        if f.endswith('.smali'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    if '->sem' in line:
                        m = re.search(r'(Landroid/[a-zA-Z0-9_/$]+;)->(sem[a-zA-Z0-9_]+)\(([^)]*)\)([a-zA-Z0-9_/[;]*)', line)
                        if m:
                            cls, method, args, ret = m.groups()
                            signatures.add((cls, method, args, ret))

print(f"Total unique methods to shim: {len(signatures)}")

# Write SemShim.java generator
java_methods = []

def smali_type_to_java(st):
    if st == 'V': return 'void'
    if st == 'Z': return 'boolean'
    if st == 'I': return 'int'
    if st == 'J': return 'long'
    if st == 'F': return 'float'
    if st == 'D': return 'double'
    if st == 'C': return 'char'
    if st == 'B': return 'byte'
    if st == 'S': return 'short'
    if st.startswith('['): return 'Object'
    if st.startswith('L'): return 'Object'
    return 'Object'

def parse_args(args_str):
    args = []
    i = 0
    while i < len(args_str):
        if args_str[i] in 'ZBCSIJFD':
            args.append(args_str[i])
            i += 1
        elif args_str[i] == '[':
            # array
            start = i
            while args_str[i] == '[':
                i += 1
            if args_str[i] == 'L':
                while args_str[i] != ';':
                    i += 1
                i += 1
            else:
                i += 1
            args.append(args_str[start:i])
        elif args_str[i] == 'L':
            start = i
            while args_str[i] != ';':
                i += 1
            i += 1
            args.append(args_str[start:i])
        else:
            i += 1
    return args

shim_methods_smali = []

for cls, method, args, ret in sorted(list(signatures)):
    arg_list = parse_args(args)
    java_ret = smali_type_to_java(ret)
    
    # Check if static call originally
    # Classes that are utility: HapticFeedbackConstants, TextUtils, Settings$System, UserHandle
    # We will accept Object thisObj as 1st param for virtual, or no thisObj for static
    print(f"Signature: {cls}->{method}({args}){ret}")

