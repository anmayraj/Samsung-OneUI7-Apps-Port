import os
import shutil
import re

# 1. Copy smali stubs
src_smali_root = "decompiled_stubs/smali/com/samsung/android"
dst_smali_root = "decompiled_clock/smali/com/samsung/android"

for root, dirs, files in os.walk(src_smali_root):
    rel_path = os.path.relpath(root, src_smali_root)
    target_dir = os.path.join(dst_smali_root, rel_path)
    os.makedirs(target_dir, exist_ok=True)
    for f in files:
        if f.endswith('.smali'):
            shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))

print("Copied all smali stubs into decompiled_clock/smali/com/samsung/android/")

# 2. Patch apktool.yml
with open("decompiled_clock/apktool.yml", "r", encoding="utf-8") as f:
    yml = f.read()

yml = re.sub(r'minSdkVersion:\s*36', 'minSdkVersion: 34', yml)
yml = re.sub(r'targetSdkVersion:\s*36', 'targetSdkVersion: 34', yml)

with open("decompiled_clock/apktool.yml", "w", encoding="utf-8") as f:
    f.write(yml)
print("Patched apktool.yml to minSdkVersion 34 / targetSdkVersion 34")

# 3. Patch AndroidManifest.xml
with open("decompiled_clock/AndroidManifest.xml", "r", encoding="utf-8") as f:
    manifest = f.read()

# Fix compileSdkVersion and platformBuildVersion
manifest = manifest.replace('compileSdkVersion="36"', 'compileSdkVersion="34"')
manifest = manifest.replace('platformBuildVersionCode="36"', 'platformBuildVersionCode="34"')
manifest = manifest.replace('platformBuildVersionName="16"', 'platformBuildVersionName="14"')

# Fix uses-feature to required="false"
manifest = re.sub(
    r'<uses-feature\s+android:name="com\.samsung\.android\.api\.version\.3601"\s*/>',
    r'<uses-feature android:name="com.samsung.android.api.version.3601" android:required="false"/>',
    manifest
)
manifest = re.sub(
    r'<uses-feature\s+android:name="com\.samsung\.feature\.samsung_experience_mobile"\s*/>',
    r'<uses-feature android:name="com.samsung.feature.samsung_experience_mobile" android:required="false"/>',
    manifest
)

# Fix uses-permission with minSdkVersion="36"
manifest = manifest.replace('android:minSdkVersion="36"', 'android:minSdkVersion="34"')

with open("decompiled_clock/AndroidManifest.xml", "w", encoding="utf-8") as f:
    f.write(manifest)
print("Patched AndroidManifest.xml successfully!")
