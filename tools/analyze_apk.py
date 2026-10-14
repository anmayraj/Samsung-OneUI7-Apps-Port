import os
import glob
import re

smali_dirs = glob.glob('decompiled_clock/smali*')
print('Smali directories:', len(smali_dirs))

mfr_checks = []
sem_floating = []
cloud_checks = []
knox_checks = []

for sdir in smali_dirs:
    for root, dirs, files in os.walk(sdir):
        for f in files:
            if f.endswith('.smali'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    if '"samsung"' in content or '"SAMSUNG"' in content:
                        mfr_checks.append(path)
                    if 'SemFloatingFeature' in content or 'SemCscFeature' in content:
                        sem_floating.append(path)
                    if 'samsung.account' in content.lower() or 'samsungcloud' in content.lower():
                        cloud_checks.append(path)
                    if 'enterprise.knox' in content.lower() or 'sec_knox' in content.lower():
                        knox_checks.append(path)

print(f"Files with 'samsung' string: {len(mfr_checks)}")
print(f"Files with SemFloatingFeature/Csc: {len(sem_floating)}")
print(f"Files with Samsung Cloud/Account: {len(cloud_checks)}")
print(f"Files with Knox: {len(knox_checks)}")

print("\n--- Top SemFloatingFeature usages ---")
for p in sem_floating[:8]:
    print(" ", p)

print("\n--- Top Manufacturer check usages ---")
for p in mfr_checks[:8]:
    print(" ", p)
