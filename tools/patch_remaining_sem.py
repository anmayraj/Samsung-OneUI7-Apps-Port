import os
import re

count_fields = 0
count_static = 0

for root, dirs, files in os.walk('decompiled_clock'):
    for f in files:
        if f.endswith('.smali') and f != 'SemShim.smali':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            # 1. Replace Configuration field accesses
            # iget vx, vy, Landroid/content/res/Configuration;->sem...:I -> const/4 vx, 0x0
            def replace_iget(m):
                global count_fields
                count_fields += 1
                dst_reg = m.group(1)
                return f"const/4 {dst_reg}, 0x0"
            
            content, c1 = re.subn(r'iget\s+([a-zA-Z0-9]+),\s*[a-zA-Z0-9]+,\s*Landroid/content/res/Configuration;->sem[a-zA-Z0-9_]+:I', replace_iget, content)
            
            # 2. Replace empty invoke-static {}, Landroid/...;->sem...
            def replace_empty_static(m):
                global count_static
                count_static += 1
                method, args, ret = m.groups()
                return f"invoke-static {{}}, Lcom/samsung/android/util/SemShim;->{method}({args}){ret}"
            
            content, c2 = re.subn(r'invoke-static\s+\{\},\s*Landroid/[a-zA-Z0-9_/$]+;->(sem[a-zA-Z0-9_]+)\(([^)]*)\)([a-zA-Z0-9_/[;]*)', replace_empty_static, content)
            
            if c1 > 0 or c2 > 0:
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(content)

print(f"Patched {count_fields} Configuration fields and {count_static} empty static calls.")
