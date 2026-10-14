# Samsung Clock Port (One UI 7 / Android 16 Base) for Non-Samsung Devices

[![Android 14+](https://img.shields.io/badge/Android-14%20%7C%2015%20%7C%2016-green.svg)](https://developer.android.com)
[![One UI 7](https://img.shields.io/badge/One%20UI-7.0%20%2F%208.5%20Base-blue.svg)](https://www.samsung.com)
[![No Root Required](https://img.shields.io/badge/Root-Not%20Required-brightgreen.svg)](#installation-guide)
[![License](https://img.shields.io/badge/License-Apache%202.0%20%2F%20MIT-orange.svg)](LICENSE)

> **The first functional port of Samsung Clock (`com.sec.android.app.clockpackage` v12.5.60.30, Android 16 / One UI 7 base) running natively, sounding alarms, and operating crash-free on non-Samsung Android devices without root.**

---

## 🌟 Overview

Historically, Samsung proprietary application ports (such as those by *AyraHikari* and other early developers) were developed for One UI 4 / 5 on Android 11–12 and ceased updates years ago. Modern Samsung apps (One UI 6, 7, and the latest Android 16 / SDK 36 preview bases) introduce deep architectural bindings to Samsung Knox, proprietary window managers (`TYPE_KEYGUARD_DIALOG`), custom haptic engines, and privileged system IPC interfaces that instantly crash on non-Samsung firmware.

This project delivers a reverse-engineered, bytecode-patched port of **Samsung Clock 12.5.60.30** (`1256030100`), retaining 100% of the authentic One UI 7 design language, audio, animations, and features while operating purely on standard Android / AOSP APIs.

---

## ✨ Features & Working Modules

- ✅ **Alarm Engine**: Set, edit, schedule, enable/disable alarms with full repeat schedules.
- ✅ **Real-Time Heads-Up Notification (HUN)**: Floating overlay banner displaying the active alarm with *Dismiss* and *Snooze* action buttons over any app or launcher.
- ✅ **Full-Screen Alarm Alert**: Full-screen alarm activity that triggers when the device is locked.
- ✅ **Alarm Background Customization**: Live background picker with custom colors, gradients, video wallpapers, and real-time Samsung Blur engine simulation.
- ✅ **Vibration & Haptics**: Full vibration playback mapped safely to standard Android vibration channels.
- ✅ **Audio Playback**: Plays alarm ringtones, Bixby briefing / custom audio tracks seamlessly.
- ✅ **World Clock**: Global city search, interactive timezone clocks, and daylight tracking.
- ✅ **Stopwatch**: High-precision stopwatch with lap times.
- ✅ **Timer**: Multi-timer support with presets and notification sound alerts.

---

## 🔬 Technical Reverse Engineering Breakdown

To make this Android 16 One UI 7 application run on standard AOSP / OEM firmware, the following reverse engineering and smali patching solutions were developed:

### 1. De-privileging Window Type 2009 (`BadTokenException`)
* **The Problem**: In One UI 7, `HeadUpNotificationService` creates overlay banners with `WindowManager.LayoutParams.type = 0x7d9` (`TYPE_KEYGUARD_DIALOG`, 2009). On non-Samsung ROMs, third-party apps attempting to add a window of type 2009 throw:
  ```text
  android.view.WindowManager$BadTokenException: Unable to add window -- token null is not valid; is your activity running?
  ```
* **The Solution**: Patched bytecode in `HeadUpNotificationService.smali` and `SnackbarWrapper.smali` to replace window type `0x7d9` with `0x7f6` (`TYPE_APPLICATION_OVERLAY`, 2038). Wrapped `WindowManager.addView` and `removeView` in try-catch guards.

### 2. Eliminating `SemStatusBarManager` NPE
* **The Problem**: Samsung Clock queries `Context.getSystemService("sem_statusbar")`. On non-Samsung devices, this returns `null`, causing an immediate `NullPointerException`:
  ```text
  null cannot be cast to non-null type android.app.SemStatusBarManager
  ```
* **The Solution**: Replaced the system service query with direct instantiation of our safe `SemStatusBarManager` stub.

### 3. AOSP Vibration Engine Alignment (`createOneShot`)
* **The Problem**: Samsung's internal `SemShim.semCreateWaveform` mistakenly invoked `VibrationEffect.createOneShot(II)` (`int, int`). The standard Android SDK only defines `createOneShot(long milliseconds, int amplitude)` (`(JI)`). When an alarm triggered vibration, ART crashed with:
  ```text
  java.lang.NoSuchMethodError: No static method createOneShot(II)Landroid/os/VibrationEffect;
  ```
* **The Solution**: Rewrote all `semCreateWaveform` overloads to pass `(long, int)` with `const-wide/16 v0, 0xc8` and wrapped the calls in try-catch blocks returning fallback nulls.

### 4. Bypassing Signature-Level Screensaver IPC (`READ_DREAM_STATE`)
* **The Problem**: Before triggering alerts, `AlarmAlertUtils.cancelDreamActivity` calls `IDreamManager.isDreaming()` to dismiss active Daydream screensavers. On AOSP, this requires `android.permission.READ_DREAM_STATE`, a privileged/signature-only permission that throws a fatal `SecurityException`.
* **The Solution**: Replaced the method bodies of `cancelDreamActivity(Context)` in both `AlarmAlertUtils.smali` and `TimerUtils.smali` with `return-void`.

### 5. Safe Telephony State Shims (`READ_PHONE_STATE`)
* **The Problem**: Samsung Clock checks whether the device is in an active phone call via `TelephonyManager.registerTelephonyCallback`. On Android 12+, this requires `READ_PHONE_STATE`.
* **The Solution**: Injected `SemShim.registerTelephonyCallback` and `unregisterTelephonyCallback` with internal try-catch blocks and added `<uses-permission android:name="android.permission.READ_PHONE_STATE"/>` to `AndroidManifest.xml`.

### 6. Samsung Blur Engine (`SemBlurInfo$Builder`)
* **The Problem**: Opening the Alarm Background preview threw `NoSuchMethodError` for missing builder methods:
  - `setCanvasScale(I)`
  - `setBackgroundColor(I)`
  - `setBackgroundCornerRadius(F)`
  - `setBackgroundCornerRadius(FFFF)`
* **The Solution**: Implemented the missing method stubs in `android.view.SemBlurInfo$Builder.smali` returning `this`.

### 7. Samsung Framework Stubs & Platform Constants
* **Constants**: Injected `Build.VERSION.SEM_INT = 0x27100` (160000, One UI 8.x) and `SEM_PLATFORM_INT = 0x27100`.
* **Stubs**: Injected clean Java-based stubs for `com.samsung.android.feature.*`, `com.samsung.android.cover.*`, `SemFloatingFeature`, `SemCscFeature`, `SemTipPopup`, and `SemLog`.

### 8. Landscape Alert Drag-to-Dismiss Fix (`AlertSlidingTabHandle`)
* **The Problem**: On tablets and landscape devices, dragging the dismiss icon on the full-screen alarm alert failed to register or drag. Samsung's OEM code calculated the touch target by subtracting an arbitrary `mTopOffset` from absolute `getLocationOnScreen()` coordinates while comparing against local `event.getX()`/`event.getY()` coordinates, creating a huge offset disparity in landscape.
* **The Solution**: Rewrote `isInCircle` and `getTargetProximityRatio` in `AlertSlidingTabHandle.smali` to calculate the center directly from local child coordinates (`getLeft() + getWidth() / 2`, `getTop() + getHeight() / 2`). This guarantees 100% responsive, seamless drag-to-dismiss in both portrait and landscape across all display aspect ratios.

---

## 📱 Device Compatibility

| Device | Android Version | Status | Notes |
|---|---|---|---|
| **Lenovo Idea Tab Pro (TB373FU)** | **Android 16 Preview (SDK 36, ZUI)** | **Tested & Verified** | 100% Functional (Alarms, Audio, Vibration, Overlay) |
| **Google Pixel Series** | Android 14 / 15 / 16 | Compatible | Requires ADB / Shizuku permission grants |
| **Motorola / Lenovo Devices** | Android 14 / 15 / 16 | Compatible | Tested and verified |
| **Xiaomi / Redmi / POCO (HyperOS)** | Android 14 / 15 | Compatible | Enable "Display pop-up windows while running in background" |
| **OnePlus / OPPO / Realme (ColorOS)** | Android 14 / 15 | Compatible | Enable background overlay in App Info |
| **AOSP Custom ROMs (LineageOS, crDroid)** | Android 14 / 15 / 16 | Compatible | Works out of the box after permissions |

---

## 📥 Installation Guide

### Option 1: Via ADB (Recommended, Fast & Easy)

1. Connect your device via USB with **USB Debugging** enabled.
2. Install the APK:
   ```bash
   adb install -r -d SamsungClock-OneUI7-Ported-v12.5.60.30.apk
   ```
3. Grant the required permissions for alarms and floating Heads-Up banners:
   ```bash
   adb shell appops set com.sec.android.app.clockpackage SYSTEM_ALERT_WINDOW allow
   adb shell appops set com.sec.android.app.clockpackage SCHEDULE_EXACT_ALARM allow
   adb shell pm grant com.sec.android.app.clockpackage android.permission.POST_NOTIFICATIONS
   adb shell pm grant com.sec.android.app.clockpackage android.permission.READ_PHONE_STATE
   ```
4. Open **Clock** and set your alarm!

### Option 2: Without PC (Using Shizuku & App Ops)

1. Download and install `SamsungClock-OneUI7-Ported-v12.5.60.30.apk`.
2. Install [Shizuku](https://shizuku.rikka.app/) and [App Ops](https://play.google.com/store/apps/details?id=rikka.appops).
3. In App Ops, find **Samsung Clock** and enable:
   - **Display over other apps** (`SYSTEM_ALERT_WINDOW`)
   - **Alarms & Reminders** (`SCHEDULE_EXACT_ALARM`)
   - **Notifications** (`POST_NOTIFICATIONS`)
4. Disable Battery Optimization (set to *Unrestricted*) so the system doesn't freeze the alarm process.

---

## 🛠️ Building from Source

To reproduce or modify the port:

### Prerequisites:
- Java JDK 17 or higher
- Python 3.10 or higher
- Original Samsung Clock APK: `com.sec.android.app.clockpackage` v12.5.60.30

### Build Instructions:
1. Clone this repository:
   ```bash
   git clone https://github.com/anmayraj/Samsung-OneUI7-Apps-Port.git
   cd SamsungClock-OneUI-Port
   ```
2. Run the automated build script:
   ```bash
   # On Windows:
   .\build_port.bat

   # Or via Python:
   python tools/build_port.py
   ```
3. The signed, zipaligned APK will be output to:
   `release/SamsungClock-OneUI7-Ported-v12.5.60.30.apk`

---

## 📜 Credits & Acknowledgements

- **Samsung Electronics**: Creator of the original Samsung Clock app and One UI design assets.
- **Anmay**: Reverse engineering, smali patching pipeline, AOSP vibration & overlay adaptation, and port maintenance.
- **AyraHikari**: Early inspiration for Samsung application porting on legacy One UI 4/5.
- **Apktool** & **Uber-Apk-Signer**: Essential tools for reverse engineering and packaging.

---

## ⚠️ Disclaimer

This is a non-commercial, educational reverse-engineering project aimed at interoperability. All intellectual property, trademarks, and copyright associated with Samsung One UI and Samsung Clock remain the sole property of Samsung Electronics Co., Ltd.
