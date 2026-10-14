import os
import re

# 1. Patch SemShim.smali
shim_path = os.path.join("decompiled_clock", "smali", "com", "samsung", "android", "util", "SemShim.smali")
with open(shim_path, "r", encoding="utf-8") as f:
    shim = f.read()

old_waveform_block = re.search(r'\.method public static semCreateWaveform\(II\)Landroid/os/VibrationEffect;.*?\.end method\s*\.method public static semCreateWaveform\(II\)Ljava/lang/Object;.*?\.end method\s*\.method public static semCreateWaveform\(IILandroid/os/VibrationEffect\$SemMagnitudeType;\)Landroid/os/VibrationEffect;.*?\.end method\s*\.method public static semCreateWaveform\(IILjava/lang/Object;\)Ljava/lang/Object;.*?\.end method', shim, re.DOTALL)

if old_waveform_block:
    new_waveform_block = """.method public static semCreateWaveform(II)Landroid/os/VibrationEffect;
    .locals 3

    :try_start_0
    const-wide/16 v0, 0xc8

    const/4 v2, -0x1

    invoke-static {v0, v1, v2}, Landroid/os/VibrationEffect;->createOneShot(JI)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    const/4 v0, 0x0

    return-object v0
.end method

.method public static semCreateWaveform(II)Ljava/lang/Object;
    .locals 3

    :try_start_0
    const-wide/16 v0, 0xc8

    const/4 v2, -0x1

    invoke-static {v0, v1, v2}, Landroid/os/VibrationEffect;->createOneShot(JI)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    const/4 v0, 0x0

    return-object v0
.end method

.method public static semCreateWaveform(IILandroid/os/VibrationEffect$SemMagnitudeType;)Landroid/os/VibrationEffect;
    .locals 3

    :try_start_0
    const-wide/16 v0, 0xc8

    const/4 v2, -0x1

    invoke-static {v0, v1, v2}, Landroid/os/VibrationEffect;->createOneShot(JI)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    const/4 v0, 0x0

    return-object v0
.end method

.method public static semCreateWaveform(IILjava/lang/Object;)Ljava/lang/Object;
    .locals 3

    :try_start_0
    const-wide/16 v0, 0xc8

    const/4 v2, -0x1

    invoke-static {v0, v1, v2}, Landroid/os/VibrationEffect;->createOneShot(JI)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    const/4 v0, 0x0

    return-object v0
.end method"""
    shim = shim[:old_waveform_block.start()] + new_waveform_block + shim[old_waveform_block.end():]
    with open(shim_path, "w", encoding="utf-8") as f:
        f.write(shim)
    print("Patched semCreateWaveform in SemShim.smali")
else:
    print("Could not match old semCreateWaveform block")

# 2. Patch cancelDreamActivity in AlarmAlertUtils.smali
alarm_utils_path = os.path.join("decompiled_clock", "smali_classes3", "com", "sec", "android", "app", "clockpackage", "alarm", "utils", "AlarmAlertUtils.smali")
with open(alarm_utils_path, "r", encoding="utf-8") as f:
    au_code = f.read()

au_match = re.search(r'\.method public static final cancelDreamActivity\(Landroid/content/Context;\)V.*?:goto_6\s*return-void\s*\.end method', au_code, re.DOTALL)
if au_match:
    new_method = """.method public static final cancelDreamActivity(Landroid/content/Context;)V
    .locals 0

    return-void
.end method"""
    au_code = au_code[:au_match.start()] + new_method + au_code[au_match.end():]
    with open(alarm_utils_path, "w", encoding="utf-8") as f:
        f.write(au_code)
    print("Patched cancelDreamActivity in AlarmAlertUtils.smali")
else:
    # Alternative regex
    au_match2 = re.search(r'\.method public static final cancelDreamActivity\(Landroid/content/Context;\)V.*?\.end method', au_code, re.DOTALL)
    if au_match2:
        new_method = """.method public static final cancelDreamActivity(Landroid/content/Context;)V
    .locals 0

    return-void
.end method"""
        au_code = au_code[:au_match2.start()] + new_method + au_code[au_match2.end():]
        with open(alarm_utils_path, "w", encoding="utf-8") as f:
            f.write(au_code)
        print("Patched cancelDreamActivity (fallback) in AlarmAlertUtils.smali")
    else:
        print("Could not find cancelDreamActivity in AlarmAlertUtils.smali")

# 3. Patch cancelDreamActivity in TimerUtils.smali
timer_utils_path = os.path.join("decompiled_clock", "smali_classes3", "com", "sec", "android", "app", "clockpackage", "timer", "util", "TimerUtils.smali")
with open(timer_utils_path, "r", encoding="utf-8") as f:
    tu_code = f.read()

tu_match = re.search(r'\.method public final cancelDreamActivity\(Landroid/content/Context;\)V.*?\.end method', tu_code, re.DOTALL)
if tu_match:
    new_method = """.method public final cancelDreamActivity(Landroid/content/Context;)V
    .locals 0

    return-void
.end method"""
    tu_code = tu_code[:tu_match.start()] + new_method + tu_code[tu_match.end():]
    with open(timer_utils_path, "w", encoding="utf-8") as f:
        f.write(tu_code)
    print("Patched cancelDreamActivity in TimerUtils.smali")
else:
    print("Could not find cancelDreamActivity in TimerUtils.smali")
