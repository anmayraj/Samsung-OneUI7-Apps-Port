import os
import re

pattern = re.compile(r'invoke-(virtual|static)(/range)?\s+(\{[^}]+\}),\s*Landroid/[a-zA-Z0-9_/$]+;->(sem[a-zA-Z0-9_]+)\(([^)]*)\)([a-zA-Z0-9_/[;]*)')

total_rewrites = 0
files_modified = 0

for root, dirs, files in os.walk('decompiled_clock'):
    for f in files:
        if f.endswith('.smali') and f != 'SemShim.smali':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            def replace_call(m):
                global total_rewrites
                itype, is_range, regs, name, args, ret = m.groups()
                total_rewrites += 1
                range_str = is_range if is_range else ""
                
                # If was virtual, 1st param in SemShim is Ljava/lang/Object;
                if itype == 'virtual':
                    new_args = "Ljava/lang/Object;" + args
                else:
                    new_args = args
                
                return f"invoke-static{range_str} {regs}, Lcom/samsung/android/util/SemShim;->{name}({new_args}){ret}"
            
            new_content, count = pattern.subn(replace_call, content)
            if count > 0:
                files_modified += 1
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(new_content)

print(f"Total call sites rewritten: {total_rewrites} across {files_modified} files")
