import os
import re

semshim_path = os.path.join("decompiled_clock", "smali", "com", "samsung", "android", "util", "SemShim.smali")
with open(semshim_path, "r", encoding="utf-8") as f:
    shim_content = f.read()

methods_to_add = """
.method public static registerTelephonyCallback(Landroid/telephony/TelephonyManager;Ljava/util/concurrent/Executor;Landroid/telephony/TelephonyCallback;)V
    .locals 3

    if-eqz p0, :cond_0

    if-nez p2, :cond_1

    :cond_0
    return-void

    :cond_1
    :try_start_0
    invoke-virtual {p0, p1, p2}, Landroid/telephony/TelephonyManager;->registerTelephonyCallback(Ljava/util/concurrent/Executor;Landroid/telephony/TelephonyCallback;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    move-exception v0

    const-string v1, "SemShim"

    const-string v2, "safeRegisterTelephonyCallback failed"

    invoke-static {v1, v2, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    return-void
.end method

.method public static unregisterTelephonyCallback(Landroid/telephony/TelephonyManager;Landroid/telephony/TelephonyCallback;)V
    .locals 3

    if-eqz p0, :cond_0

    if-nez p1, :cond_1

    :cond_0
    return-void

    :cond_1
    :try_start_0
    invoke-virtual {p0, p1}, Landroid/telephony/TelephonyManager;->unregisterTelephonyCallback(Landroid/telephony/TelephonyCallback;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    move-exception v0

    const-string v1, "SemShim"

    const-string v2, "safeUnregisterTelephonyCallback failed"

    invoke-static {v1, v2, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    return-void
.end method
"""

if "safeRegisterTelephonyCallback" not in shim_content:
    with open(semshim_path, "a", encoding="utf-8") as f:
        f.write("\n" + methods_to_add + "\n")
    print("Added telephony methods to SemShim.smali")
else:
    print("Telephony methods already in SemShim.smali")

# Patch all smali calls
reg_pat = re.compile(r'invoke-virtual\s*(\{[^}]+\}),\s*Landroid/telephony/TelephonyManager;->registerTelephonyCallback\(Ljava/util/concurrent/Executor;Landroid/telephony/TelephonyCallback;\)V')
unreg_pat = re.compile(r'invoke-virtual\s*(\{[^}]+\}),\s*Landroid/telephony/TelephonyManager;->unregisterTelephonyCallback\(Landroid/telephony/TelephonyCallback;\)V')

total_reg = 0
total_unreg = 0

for root, _, files in os.walk("decompiled_clock"):
    for f in files:
        if f.endswith(".smali") and f != "SemShim.smali":
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8") as fp:
                code = fp.read()
            
            new_code, n1 = reg_pat.subn(r'invoke-static \1, Lcom/samsung/android/util/SemShim;->registerTelephonyCallback(Landroid/telephony/TelephonyManager;Ljava/util/concurrent/Executor;Landroid/telephony/TelephonyCallback;)V', code)
            new_code, n2 = unreg_pat.subn(r'invoke-static \1, Lcom/samsung/android/util/SemShim;->unregisterTelephonyCallback(Landroid/telephony/TelephonyManager;Landroid/telephony/TelephonyCallback;)V', new_code)
            
            if n1 > 0 or n2 > 0:
                with open(p, "w", encoding="utf-8") as fp:
                    fp.write(new_code)
                total_reg += n1
                total_unreg += n2
                print(f"Patched {f}: {n1} register, {n2} unregister")

print(f"Total patched: {total_reg} register, {total_unreg} unregister")

# Also add READ_PHONE_STATE to AndroidManifest.xml
manifest_path = os.path.join("decompiled_clock", "AndroidManifest.xml")
with open(manifest_path, "r", encoding="utf-8") as f:
    mf = f.read()

if "android.permission.READ_PHONE_STATE" not in mf:
    target = '<uses-permission android:name="android.permission.WAKE_LOCK"/>'
    replacement = '<uses-permission android:name="android.permission.READ_PHONE_STATE"/>\n    <uses-permission android:name="android.permission.WAKE_LOCK"/>'
    mf = mf.replace(target, replacement, 1)
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(mf)
    print("Added READ_PHONE_STATE permission to AndroidManifest.xml")
else:
    print("READ_PHONE_STATE already in AndroidManifest.xml")
