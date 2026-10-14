#!/usr/bin/env python3
"""
Samsung Clock (One UI 7 / Android 16 Base) - Automated Build & Patch Pipeline
Ported for Non-Samsung Android 14+ Devices (AOSP, Pixel, Lenovo, Motorola, Xiaomi, OnePlus)

Author: Anmay & Community
Target Package: com.sec.android.app.clockpackage
Version: 12.5.60.30 (1256030100)
"""

import os
import sys
import subprocess
import shutil
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TOOLS_DIR = os.path.join(ROOT_DIR, "tools")
DECOMPILED_DIR = os.path.join(ROOT_DIR, "decompiled_clock")
OUTPUT_APK_UNSIGNED = os.path.join(ROOT_DIR, "SamsungClock_Ported_Unsigned.apk")
RELEASE_DIR = os.path.join(ROOT_DIR, "release")
RELEASE_APK = os.path.join(RELEASE_DIR, "SamsungClock-OneUI7-Ported-v12.5.60.30.apk")
APKTOOL_JAR = os.path.join(TOOLS_DIR, "apktool.jar")
UBER_SIGNER_JAR = os.path.join(TOOLS_DIR, "uber-apk-signer.jar")


def run_cmd(cmd, cwd=ROOT_DIR):
    print(f"[*] Running: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=cwd)
    if res.returncode != 0:
        print(f"[!] Error: Command exited with code {res.returncode}")
        sys.exit(res.returncode)


def apply_patch_pipeline():
    print("=" * 60)
    print(" [1/6] Copying Samsung Framework Stubs & Manifest Patches")
    print("=" * 60)
    run_cmd(f'python "{os.path.join(TOOLS_DIR, "patch_clock.py")}"')

    print("=" * 60)
    print(" [2/6] Patching SEM Build & Platform Version Constants")
    print("=" * 60)
    run_cmd(f'python "{os.path.join(TOOLS_DIR, "patch_sem_build.py")}"')

    print("=" * 60)
    print(" [3/6] Patching Configuration Fields & Static SEM Methods")
    print("=" * 60)
    run_cmd(f'python "{os.path.join(TOOLS_DIR, "patch_remaining_sem.py")}"')

    print("=" * 60)
    print(" [4/6] Patching Window Overlay Types (0x7d9 -> 0x7f6)")
    print("=" * 60)
    run_cmd(f'python "{os.path.join(TOOLS_DIR, "patch_window_types.py")}"')

    print("=" * 60)
    print(" [5/6] Injecting Telephony Safe Shim & Manifest Permission")
    print("=" * 60)
    run_cmd(f'python "{os.path.join(TOOLS_DIR, "patch_telephony.py")}"')

    print("=" * 60)
    print(" [6/7] Patching Vibration Waveforms & Stubbing Screensaver IPC")
    print("=" * 60)
    run_cmd(f'python "{os.path.join(TOOLS_DIR, "patch_vibe_and_dreams.py")}"')

    print("=" * 60)
    print(" [7/7] Patching Alert Sliding Tab Handle for Landscape Orientation")
    print("=" * 60)
    run_cmd(f'python "{os.path.join(TOOLS_DIR, "patch_sliding_tab.py")}"')


def verify_blur_builder():
    print("[*] Verifying SemBlurInfo$Builder smali...")
    blur_path = os.path.join(DECOMPILED_DIR, "smali", "android", "view", "SemBlurInfo$Builder.smali")
    if not os.path.exists(blur_path):
        print(f"[!] Warning: {blur_path} not found.")
        return
    with open(blur_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    needed_methods = [
        "setCanvasScale(I)Landroid/view/SemBlurInfo$Builder;",
        "setBackgroundColor(I)Landroid/view/SemBlurInfo$Builder;",
        "setBackgroundCornerRadius(F)Landroid/view/SemBlurInfo$Builder;",
        "setBackgroundCornerRadius(FFFF)Landroid/view/SemBlurInfo$Builder;"
    ]
    missing = [m for m in needed_methods if m not in content]
    if missing:
        print(f"[!] Appending missing SemBlurInfo$Builder methods: {missing}")
        addition = """
.method public setCanvasScale(I)Landroid/view/SemBlurInfo$Builder;
    .locals 0
    return-object p0
.end method

.method public setBackgroundColor(I)Landroid/view/SemBlurInfo$Builder;
    .locals 0
    return-object p0
.end method

.method public setBackgroundCornerRadius(F)Landroid/view/SemBlurInfo$Builder;
    .locals 0
    return-object p0
.end method

.method public setBackgroundCornerRadius(FFFF)Landroid/view/SemBlurInfo$Builder;
    .locals 0
    return-object p0
.end method
"""
        with open(blur_path, "a", encoding="utf-8") as f:
            f.write(addition)
        print("[+] Added missing SemBlurInfo$Builder methods.")
    else:
        print("[+] SemBlurInfo$Builder contains all required methods.")


def build_and_sign():
    print("=" * 60)
    print(" [*] Rebuilding APK with apktool...")
    print("=" * 60)
    run_cmd(f'java -jar "{APKTOOL_JAR}" b "{DECOMPILED_DIR}" -o "{OUTPUT_APK_UNSIGNED}"')

    print("=" * 60)
    print(" [*] Signing & ZipAligning APK with uber-apk-signer...")
    print("=" * 60)
    run_cmd(f'java -jar "{UBER_SIGNER_JAR}" -a "{OUTPUT_APK_UNSIGNED}" --overwrite')

    os.makedirs(RELEASE_DIR, exist_ok=True)
    shutil.copy2(OUTPUT_APK_UNSIGNED, RELEASE_APK)
    print("=" * 60)
    print(f"[✓] BUILD SUCCESSFUL!")
    print(f"[✓] Release APK created: {RELEASE_APK}")
    print("=" * 60)


if __name__ == "__main__":
    print("============================================================")
    print("  Samsung Clock One UI 7 / Android 16 Build & Patch Engine   ")
    print("============================================================")
    apply_patch_pipeline()
    verify_blur_builder()
    build_and_sign()
