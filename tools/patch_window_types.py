import os
import re

# 1. Patch HeadUpNotificationService.smali
huns_path = os.path.join("decompiled_clock", "smali_classes5", "com", "sec", "android", "app", "clockpackage", "commonalert", "viewmodel", "HeadUpNotificationService.smali")
with open(huns_path, "r", encoding="utf-8") as f:
    code = f.read()

# Change window types 0x7d9 -> 0x7f6
code = code.replace("const/16 v3, 0x7d9", "const/16 v3, 0x7f6")
code = code.replace("const/16 v1, 0x7d9", "const/16 v1, 0x7f6")

# Replace getSystemService("sem_statusbar") with direct instantiation
old_statusbar = """    const-string v0, "sem_statusbar"

    invoke-virtual {p0, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    const-string v1, "null cannot be cast to non-null type android.app.SemStatusBarManager"

    invoke-static {v0, v1}, Lkotlin/jvm/internal/l;->c(Ljava/lang/Object;Ljava/lang/String;)V

    check-cast v0, Landroid/app/SemStatusBarManager;

    iput-object v0, p0, Lcom/sec/android/app/clockpackage/commonalert/viewmodel/HeadUpNotificationService;->mStatusBarManager:Landroid/app/SemStatusBarManager;"""

new_statusbar = """    new-instance v0, Landroid/app/SemStatusBarManager;

    invoke-direct {v0}, Landroid/app/SemStatusBarManager;-><init>()V

    iput-object v0, p0, Lcom/sec/android/app/clockpackage/commonalert/viewmodel/HeadUpNotificationService;->mStatusBarManager:Landroid/app/SemStatusBarManager;"""

code = code.replace(old_statusbar, new_statusbar)

# Wrap addView in try-catch
old_addview = """    invoke-interface {v0, v1, v2}, Landroid/view/ViewManager;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iput-object v0, p0, Lcom/sec/android/app/clockpackage/commonalert/viewmodel/HeadUpNotificationService;->mWindowManager:Landroid/view/WindowManager;"""

new_addview = """    :try_start_addview
    invoke-interface {v0, v1, v2}, Landroid/view/ViewManager;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iput-object v0, p0, Lcom/sec/android/app/clockpackage/commonalert/viewmodel/HeadUpNotificationService;->mWindowManager:Landroid/view/WindowManager;
    :try_end_addview
    .catchall {:try_start_addview .. :try_end_addview} :catch_addview

    goto :goto_addview_done

    :catch_addview
    move-exception v1

    const-string v2, "HeadUpNotificationService"

    const-string v0, "addView failed"

    invoke-static {v2, v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_addview_done"""

code = code.replace(old_addview, new_addview)

# Wrap removeView in try-catch
old_remview = """    invoke-interface {v0, v1}, Landroid/view/ViewManager;->removeView(Landroid/view/View;)V"""
new_remview = """    :try_start_rem
    invoke-interface {v0, v1}, Landroid/view/ViewManager;->removeView(Landroid/view/View;)V
    :try_end_rem
    .catchall {:try_start_rem .. :try_end_rem} :catch_rem

    :catch_rem"""

code = code.replace(old_remview, new_remview)

with open(huns_path, "w", encoding="utf-8") as f:
    f.write(code)
print("Patched HeadUpNotificationService.smali")

# 2. Patch SnackbarWrapper.smali
snack_path = os.path.join("decompiled_clock", "smali_classes5", "com", "sec", "android", "app", "clockpackage", "common", "util", "SnackbarWrapper.smali")
with open(snack_path, "r", encoding="utf-8") as f:
    scode = f.read()

scode = scode.replace("const/16 v1, 0x7d9", "const/16 v1, 0x7f6")
with open(snack_path, "w", encoding="utf-8") as f:
    f.write(scode)
print("Patched SnackbarWrapper.smali")

# 3. Patch FullAlertActivity.smali
faa_path = os.path.join("decompiled_clock", "smali_classes5", "com", "sec", "android", "app", "clockpackage", "commonalert", "activity", "FullAlertActivity.smali")
with open(faa_path, "r", encoding="utf-8") as f:
    faacode = f.read()

old_faa_method = """.method private final getSemStatusBarManager()Landroid/app/SemStatusBarManager;
    .locals 1
    .annotation build Landroid/annotation/SuppressLint;
        value = {
            "WrongConstant"
        }
    .end annotation

    const-string v0, "sem_statusbar"

    invoke-virtual {p0, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object p0

    const-string v0, "null cannot be cast to non-null type android.app.SemStatusBarManager"

    invoke-static {p0, v0}, Lkotlin/jvm/internal/l;->c(Ljava/lang/Object;Ljava/lang/String;)V

    check-cast p0, Landroid/app/SemStatusBarManager;

    return-object p0
.end method"""

new_faa_method = """.method private final getSemStatusBarManager()Landroid/app/SemStatusBarManager;
    .locals 1
    .annotation build Landroid/annotation/SuppressLint;
        value = {
            "WrongConstant"
        }
    .end annotation

    new-instance v0, Landroid/app/SemStatusBarManager;

    invoke-direct {v0}, Landroid/app/SemStatusBarManager;-><init>()V

    return-object v0
.end method"""

faacode = faacode.replace(old_faa_method, new_faa_method)
with open(faa_path, "w", encoding="utf-8") as f:
    f.write(faacode)
print("Patched FullAlertActivity.smali")
