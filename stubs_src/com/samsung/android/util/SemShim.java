package com.samsung.android.util;

import android.app.Activity;
import android.media.AudioManager;
import android.os.Build;

public class SemShim {
    public static Object semAddAudioTag(Object obj, Object p0) { return null; }
    public static void semAddExtensionFlags(Object obj, int p0) {}
    public static Object semApplyEffectStrength(Object obj, int p0) { return null; }
    public static void semClearExtensionFlags(Object obj, int p0) {}
    public static void semConvertFromTranslucent(Object obj, boolean p0) {}
    public static boolean semConvertToTranslucent(Object obj, Object p0) { return false; }
    public static Object semCreateWaveform(int p0, int p1) { return null; }
    public static Object semCreateWaveform(int p0, int p1, Object p2) { return null; }
    public static void semDismissPopup(Object obj) {}
    public static boolean semExitMultiWindowMode(Object obj) { return false; }
    public static boolean semForceHideSoftInput(Object obj) { return false; }
    public static Object semGetApplicationIconForIconTray(Object obj, Object p0, int p1) { return null; }
    public static Object semGetAudioFocusedPackageName(Object obj) { return ""; }
    public static int semGetCallState(Object obj, int p0) { return 0; }
    public static int semGetInputSource(int p0) { return 0; }
    public static int semGetIntForUser(Object p0, Object p1, int p2, int p3) { return 0; }
    public static Object semGetPrefixCharForSpan(Object p0, Object p1, Object p2) { return null; }
    public static int semGetRingerModeInternal(Object obj) { if (obj instanceof AudioManager) return ((AudioManager)obj).getRingerMode(); return 2; }
    public static int semGetSupportedVibrationType(Object obj) { return 0; }
    public static int semGetVibrationIndex(int p0) { return p0; }
    public static boolean semIsAccessoryKeyboard(Object obj) { return false; }
    public static boolean semIsInEmergencyCallbackMode(Object obj) { return false; }
    public static boolean semIsManagedProfile(Object obj) { return false; }
    public static boolean semIsPermissionRevokedByUserFixed(Object obj, Object p0, Object p1) { return false; }
    public static boolean semIsRecordActive(Object obj, int p0) { return false; }
    public static boolean semIsResumed(Object obj) { return true; }
    public static boolean semIsUriValid(Object obj) { return true; }
    public static boolean semIsVibrating(Object obj) { return false; }
    public static boolean semIsVideoCall(Object obj) { return false; }
    public static boolean semIsVoiceCallActive(Object obj) { return false; }
    public static boolean semMinimizeSoftInput(Object obj, Object p0, int p1) { return false; }
    public static boolean semRequestAccessibilityFocus(Object obj) { return false; }
    public static void semSetActionModeMenuItemEnabled(Object obj, int p0, boolean p1) {}
    public static void semSetAnchor(Object obj, int p0, int p1) {}
    public static void semSetAnimation(Object obj, Object p0) {}
    public static void semSetAutoPowerUp(Object obj, Object p0) {}
    public static void semSetBackgroundBlurEnabled(Object obj, boolean p0) {}
    public static void semSetBlurInfo(Object obj, int p0, Object p1) {}
    public static void semSetBlurInfo(Object obj, Object p0) {}
    public static void semSetBlurRadius(Object obj, int p0) {}
    public static void semSetButtonShapeEnabled(Object obj, boolean p0) {}
    public static void semSetGfxImageFilter(Object obj, Object p0) {}
    public static void semSetHoverPopupType(Object obj, int p0) {}
    public static void semSetMarginsRelative(Object obj, int p0, int p1, int p2, int p3) {}
    public static void semSetMin(Object obj, int p0) {}
    public static void semSetMode(Object obj, int p0) {}
    public static void semSetMultiSelectionEnabled(Object obj, boolean p0) {}
    public static void semSetPendingIntentAfterUnlock(Object obj, Object p0, Object p1) {}
    public static Object semSetPopOverOptions(Object obj, Object p0, Object p1, Object p2, Object p3) { return null; }
    public static void semSetRoundedCornerColor(Object obj, int p0, int p1) {}
    public static void semSetRoundedCorners(Object obj, int p0) {}
    public static void semSetVideoSize(Object obj, int p0, int p1, boolean p2, boolean p3) {}
    public static boolean semStartFlashNotificationSequence(Object obj, Object p0, int p1) { return false; }
    public static boolean semStopFlashNotificationSequence(Object obj, Object p0) { return false; }

    public static int semGetCurrentUser() { return 0; }
    public static int semGetMyUserId() { return 0; }
    public static int semGetCallingUserId() { return 0; }
    public static boolean semIsDefaultFontStyle() { return true; }
    public static int semGetActiveStreamType() { return 4; }

}