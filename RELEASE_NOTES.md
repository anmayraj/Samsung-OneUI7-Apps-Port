# Samsung Clock (One UI 7 / Android 16 Base) - Release v12.5.60.30

## 🚀 Highlights & Features
- **World's First Working One UI 7 / Android 16 App Port** for non-Samsung devices.
- **Tested & 100% Functional** on Android 16 Preview / SDK 36 on Lenovo Idea Tab Pro (TB373FU).
- **Crash-Free Operation**:
  - Alarms fire accurately at scheduled times.
  - Heads-Up Notification (HUN) floating banners over home screen and active apps with interactive Dismiss and Snooze actions.
  - Full-screen alert on lockscreen with smooth drag-to-dismiss in both portrait and landscape orientations.
  - Alarm background customization with live video/color picker and Samsung blur simulation.
  - Audio and haptic vibration engine adapted cleanly for standard Android.
- **No Root Required**: Works purely via standard user-space permissions and optional ADB / Shizuku commands.

## 📦 Package Details
- **Package Name:** `com.sec.android.app.clockpackage`
- **Version Name:** `12.5.60.30`
- **Version Code:** `1256030100`
- **Target SDK:** 34 (Android 14) / Min SDK: 34 (Fully forward-compatible with Android 15 & 16)
- **File:** `SamsungClock-OneUI7-Ported-v12.5.60.30.apk`
- **File Size:** `60,421,321 bytes` (~57.6 MB)
- **SHA256:** `80AAD0D7913465A4A22D72EBC2291DB182922EE482CC3B5D1E16234F23F14490`

## 📲 Quick Installation via ADB
```bash
adb install -r -d SamsungClock-OneUI7-Ported-v12.5.60.30.apk
adb shell appops set com.sec.android.app.clockpackage SYSTEM_ALERT_WINDOW allow
adb shell appops set com.sec.android.app.clockpackage SCHEDULE_EXACT_ALARM allow
adb shell pm grant com.sec.android.app.clockpackage android.permission.POST_NOTIFICATIONS
adb shell pm grant com.sec.android.app.clockpackage android.permission.READ_PHONE_STATE
```

*For more details, source code, and manual installation instructions, check the [README.md](README.md).*
