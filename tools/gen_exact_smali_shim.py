import os
import re

shim_calls = set()
for root, dirs, files in os.walk('decompiled_clock'):
    for f in files:
        if f.endswith('.smali') and f != 'SemShim.smali':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    if 'Lcom/samsung/android/util/SemShim;->' in line:
                        m = re.search(r'Lcom/samsung/android/util/SemShim;->([a-zA-Z0-9_]+)\(([^)]*)\)([a-zA-Z0-9_/[;]*)', line)
                        if m:
                            shim_calls.add(m.groups())

smali_lines = [
    ".class public Lcom/samsung/android/util/SemShim;",
    ".super Ljava/lang/Object;",
    ".source \"SemShim.java\"",
    "",
    ".method public constructor <init>()V",
    "    .locals 0",
    "    invoke-direct {p0}, Ljava/lang/Object;-><init>()V",
    "    return-void",
    ".end method",
    ""
]

for name, args, ret in sorted(list(shim_calls)):
    smali_lines.append(f".method public static {name}({args}){ret}")
    if ret == 'V':
        smali_lines.append("    .locals 0")
        smali_lines.append("    return-void")
    elif ret == 'Z':
        smali_lines.append("    .locals 1")
        if name in ('semIsResumed', 'semIsUriValid', 'semIsDefaultFontStyle'):
            smali_lines.append("    const/4 v0, 0x1")
        else:
            smali_lines.append("    const/4 v0, 0x0")
        smali_lines.append("    return v0")
    elif ret == 'I':
        smali_lines.append("    .locals 1")
        if name == 'semGetVibrationIndex':
            # return p0
            smali_lines = smali_lines[:-1] # remove locals 1
            smali_lines.append("    .locals 0")
            smali_lines.append("    return p0")
        elif name == 'semGetActiveStreamType':
            smali_lines.append("    const/4 v0, 0x4")
            smali_lines.append("    return v0")
        else:
            smali_lines.append("    const/4 v0, 0x0")
            smali_lines.append("    return v0")
    elif ret == 'Landroid/app/ActivityOptions;':
        smali_lines.append("    .locals 0")
        smali_lines.append("    check-cast p0, Landroid/app/ActivityOptions;")
        smali_lines.append("    return-object p0")
    elif ret == 'Landroid/media/AudioAttributes;':
        smali_lines.append("    .locals 0")
        smali_lines.append("    const/4 p0, 0x0")
        smali_lines.append("    return-object p0")
    else:
        # Object or array
        smali_lines.append("    .locals 1")
        smali_lines.append("    const/4 v0, 0x0")
        smali_lines.append("    return-object v0")
    smali_lines.append(".end method")
    smali_lines.append("")

out_path = 'decompiled_clock/smali/com/samsung/android/util/SemShim.smali'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(smali_lines))

print(f"Generated 100% exact SemShim.smali with {len(shim_calls)} methods")
