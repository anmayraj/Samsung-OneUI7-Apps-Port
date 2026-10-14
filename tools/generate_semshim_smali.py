import re

semshim_smali = """\
.class public Lcom/samsung/android/util/SemShim;
.super Ljava/lang/Object;
.source "SemShim.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static semAddAudioTag(Ljava/lang/Object;Ljava/lang/String;)Landroid/media/AudioAttributes$Builder;
    .locals 0

    check-cast p0, Landroid/media/AudioAttributes$Builder;

    return-object p0
.end method

.method public static semAddAudioTag(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .locals 0

    return-object p0
.end method

.method public static semAddExtensionFlags(Ljava/lang/Object;I)V
    .locals 0

    return-void
.end method

.method public static semApplyEffectStrength(Ljava/lang/Object;I)Landroid/os/VibrationEffect;
    .locals 0

    check-cast p0, Landroid/os/VibrationEffect;

    return-object p0
.end method

.method public static semApplyEffectStrength(Ljava/lang/Object;I)Ljava/lang/Object;
    .locals 0

    return-object p0
.end method

.method public static semClearExtensionFlags(Ljava/lang/Object;I)V
    .locals 0

    return-void
.end method

.method public static semConvertFromTranslucent(Ljava/lang/Object;Z)V
    .locals 0

    return-void
.end method

.method public static semConvertToTranslucent(Ljava/lang/Object;Landroid/app/Activity$SemTranslucentConversionListener;)Z
    .locals 1

    const/4 v0, 0x1

    return v0
.end method

.method public static semConvertToTranslucent(Ljava/lang/Object;Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x1

    return v0
.end method

.method public static semCreateWaveform(II)Landroid/os/VibrationEffect;
    .locals 2

    const/16 v0, 0xc8

    const/4 v1, -0x1

    invoke-static {v0, v1}, Landroid/os/VibrationEffect;->createOneShot(II)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
.end method

.method public static semCreateWaveform(II)Ljava/lang/Object;
    .locals 2

    const/16 v0, 0xc8

    const/4 v1, -0x1

    invoke-static {v0, v1}, Landroid/os/VibrationEffect;->createOneShot(II)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
.end method

.method public static semCreateWaveform(IILandroid/os/VibrationEffect$SemMagnitudeType;)Landroid/os/VibrationEffect;
    .locals 2

    const/16 v0, 0xc8

    const/4 v1, -0x1

    invoke-static {v0, v1}, Landroid/os/VibrationEffect;->createOneShot(II)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
.end method

.method public static semCreateWaveform(IILjava/lang/Object;)Ljava/lang/Object;
    .locals 2

    const/16 v0, 0xc8

    const/4 v1, -0x1

    invoke-static {v0, v1}, Landroid/os/VibrationEffect;->createOneShot(II)Landroid/os/VibrationEffect;

    move-result-object v0

    return-object v0
.end method

.method public static semDismissPopup(Ljava/lang/Object;)V
    .locals 0

    return-void
.end method

.method public static semExitMultiWindowMode(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semForceHideSoftInput(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semGetActiveStreamType()I
    .locals 1

    const/4 v0, 0x4

    return v0
.end method

.method public static semGetApplicationIconForIconTray(Ljava/lang/Object;Ljava/lang/String;I)Landroid/graphics/drawable/Drawable;
    .locals 1

    :try_start_0
    check-cast p0, Landroid/content/pm/PackageManager;

    invoke-virtual {p0, p1}, Landroid/content/pm/PackageManager;->getApplicationIcon(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v0
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    return-object v0

    :catch_0
    const/4 v0, 0x0

    return-object v0
.end method

.method public static semGetApplicationIconForIconTray(Ljava/lang/Object;Ljava/lang/Object;I)Ljava/lang/Object;
    .locals 1

    :try_start_0
    check-cast p0, Landroid/content/pm/PackageManager;

    check-cast p1, Ljava/lang/String;

    invoke-virtual {p0, p1}, Landroid/content/pm/PackageManager;->getApplicationIcon(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v0
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    return-object v0

    :catch_0
    const/4 v0, 0x0

    return-object v0
.end method

.method public static semGetAudioFocusedPackageName(Ljava/lang/Object;)Ljava/lang/String;
    .locals 1

    const-string v0, ""

    return-object v0
.end method

.method public static semGetCallState(Ljava/lang/Object;I)I
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semGetCallingUserId()I
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semGetCurrentUser()I
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semGetInputSource(I)I
    .locals 0

    return p0
.end method

.method public static semGetIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I
    .locals 1

    :try_start_0
    invoke-static {p0, p1, p2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    return v0

    :catch_0
    return p2
.end method

.method public static semGetIntForUser(Ljava/lang/Object;Ljava/lang/Object;II)I
    .locals 1

    :try_start_0
    check-cast p0, Landroid/content/ContentResolver;

    check-cast p1, Ljava/lang/String;

    invoke-static {p0, p1, p2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    return v0

    :catch_0
    return p2
.end method

.method public static semGetMyUserId()I
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semGetPrefixCharForSpan(Landroid/text/TextPaint;Ljava/lang/CharSequence;[C)[C
    .locals 0

    return-object p2
.end method

.method public static semGetPrefixCharForSpan(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .locals 0

    return-object p2
.end method

.method public static semGetRingerModeInternal(Ljava/lang/Object;)I
    .locals 1

    instance-of v0, p0, Landroid/media/AudioManager;

    if-eqz v0, :cond_0

    check-cast p0, Landroid/media/AudioManager;

    invoke-virtual {p0}, Landroid/media/AudioManager;->getRingerMode()I

    move-result v0

    return v0

    :cond_0
    const/4 v0, 0x2

    return v0
.end method

.method public static semGetSupportedVibrationType(Ljava/lang/Object;)I
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semGetVibrationIndex(I)I
    .locals 0

    return p0
.end method

.method public static semIsAccessoryKeyboard(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsDefaultFontStyle()Z
    .locals 1

    const/4 v0, 0x1

    return v0
.end method

.method public static semIsInEmergencyCallbackMode(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsManagedProfile(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsPermissionRevokedByUserFixed(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/String;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsPermissionRevokedByUserFixed(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsRecordActive(Ljava/lang/Object;I)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsResumed(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x1

    return v0
.end method

.method public static semIsUriValid(Ljava/lang/Object;)Z
    .locals 1

    if-eqz p0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method

.method public static semIsVibrating(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsVideoCall(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semIsVoiceCallActive(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semMinimizeSoftInput(Ljava/lang/Object;Landroid/os/IBinder;I)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semMinimizeSoftInput(Ljava/lang/Object;Ljava/lang/Object;I)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semRequestAccessibilityFocus(Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semSetActionModeMenuItemEnabled(Ljava/lang/Object;IZ)V
    .locals 0

    return-void
.end method

.method public static semSetAnchor(Ljava/lang/Object;II)V
    .locals 0

    return-void
.end method

.method public static semSetAnimation(Ljava/lang/Object;Landroid/widget/SemRemoteViewsAnimation;)V
    .locals 0

    return-void
.end method

.method public static semSetAnimation(Ljava/lang/Object;Ljava/lang/Object;)V
    .locals 0

    return-void
.end method

.method public static semSetAutoPowerUp(Ljava/lang/Object;Ljava/lang/String;)V
    .locals 0

    return-void
.end method

.method public static semSetAutoPowerUp(Ljava/lang/Object;Ljava/lang/Object;)V
    .locals 0

    return-void
.end method

.method public static semSetBackgroundBlurEnabled(Ljava/lang/Object;Z)V
    .locals 0

    return-void
.end method

.method public static semSetBlurInfo(Ljava/lang/Object;ILandroid/view/SemBlurInfo;)V
    .locals 0

    return-void
.end method

.method public static semSetBlurInfo(Ljava/lang/Object;ILjava/lang/Object;)V
    .locals 0

    return-void
.end method

.method public static semSetBlurInfo(Ljava/lang/Object;Landroid/view/SemBlurInfo;)V
    .locals 0

    return-void
.end method

.method public static semSetBlurInfo(Ljava/lang/Object;Ljava/lang/Object;)V
    .locals 0

    return-void
.end method

.method public static semSetBlurRadius(Ljava/lang/Object;I)V
    .locals 0

    return-void
.end method

.method public static semSetButtonShapeEnabled(Ljava/lang/Object;Z)V
    .locals 0

    return-void
.end method

.method public static semSetGfxImageFilter(Ljava/lang/Object;Lcom/samsung/android/graphics/SemGfxImageFilter;)V
    .locals 0

    return-void
.end method

.method public static semSetGfxImageFilter(Ljava/lang/Object;Ljava/lang/Object;)V
    .locals 0

    return-void
.end method

.method public static semSetHoverPopupType(Ljava/lang/Object;I)V
    .locals 0

    return-void
.end method

.method public static semSetMarginsRelative(Ljava/lang/Object;IIII)V
    .locals 0

    return-void
.end method

.method public static semSetMin(Ljava/lang/Object;I)V
    .locals 0

    return-void
.end method

.method public static semSetMode(Ljava/lang/Object;I)V
    .locals 0

    return-void
.end method

.method public static semSetMultiSelectionEnabled(Ljava/lang/Object;Z)V
    .locals 0

    return-void
.end method

.method public static semSetPendingIntentAfterUnlock(Ljava/lang/Object;Landroid/app/PendingIntent;Landroid/content/Intent;)V
    .locals 0

    return-void
.end method

.method public static semSetPendingIntentAfterUnlock(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V
    .locals 0

    return-void
.end method

.method public static semSetPopOverOptions(Ljava/lang/Object;[I[I[Landroid/graphics/Point;[I)Landroid/app/ActivityOptions;
    .locals 1

    instance-of v0, p0, Landroid/app/ActivityOptions;

    if-eqz v0, :cond_0

    check-cast p0, Landroid/app/ActivityOptions;

    return-object p0

    :cond_0
    const/4 v0, 0x0

    return-object v0
.end method

.method public static semSetPopOverOptions(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .locals 0

    return-object p0
.end method

.method public static semSetRoundedCornerColor(Ljava/lang/Object;II)V
    .locals 0

    return-void
.end method

.method public static semSetRoundedCorners(Ljava/lang/Object;I)V
    .locals 0

    return-void
.end method

.method public static semSetVideoSize(Ljava/lang/Object;IIZZ)V
    .locals 0

    return-void
.end method

.method public static semStartFlashNotificationSequence(Ljava/lang/Object;Landroid/content/Context;I)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semStartFlashNotificationSequence(Ljava/lang/Object;Ljava/lang/Object;I)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semStopFlashNotificationSequence(Ljava/lang/Object;Landroid/content/Context;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method

.method public static semStopFlashNotificationSequence(Ljava/lang/Object;Ljava/lang/Object;)Z
    .locals 1

    const/4 v0, 0x0

    return v0
.end method
"""

with open("decompiled_clock/smali/com/samsung/android/util/SemShim.smali", "w", encoding="utf-8") as f:
    f.write(semshim_smali)

print("SemShim.smali generated successfully.")
