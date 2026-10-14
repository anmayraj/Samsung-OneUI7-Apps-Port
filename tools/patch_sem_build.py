import os
import re

files_to_check = [
    'decompiled_clock/smali/com/sec/android/app/clockpackage/alarmbackground/utils/videopreview/helper/SEFHelper.smali',
    'decompiled_clock/smali/com/sec/android/app/clockpackage/commonalert/view/AlertSlidingTab.smali',
    'decompiled_clock/smali/com/sec/android/app/clockpackage/worldclock/activity/SearchBarActivity.smali',
]

# Or scan all files and replace
total_replaced = 0

for root, dirs, files in os.walk('decompiled_clock'):
    for f in files:
        if f.endswith('.smali'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            orig = content
            # sget vx, Landroid/os/Build$VERSION;->SEM_INT:I -> const vx, 0x27100
            content = re.sub(r'sget\s+([a-zA-Z0-9]+),\s*Landroid/os/Build\$VERSION;->SEM_INT:I', r'const \1, 0x27100', content)
            # sget vx, Landroid/os/Build$VERSION;->SEM_PLATFORM_INT:I -> const vx, 0x27100
            content = re.sub(r'sget\s+([a-zA-Z0-9]+),\s*Landroid/os/Build\$VERSION;->SEM_PLATFORM_INT:I', r'const \1, 0x27100', content)
            # sget vx, Landroid/os/Build$VERSION;->SEM_FIRST_SDK_INT:I -> const/16 vx, 0x22
            content = re.sub(r'sget\s+([a-zA-Z0-9]+),\s*Landroid/os/Build\$VERSION;->SEM_FIRST_SDK_INT:I', r'const/16 \1, 0x22', content)
            
            if content != orig:
                total_replaced += 1
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                print(f"Patched SEM Build fields in: {f}")

print(f"Total files updated: {total_replaced}")
