import os

os.makedirs("decompiled_clock/smali/android/os", exist_ok=True)
os.makedirs("decompiled_clock/smali/android/app", exist_ok=True)
os.makedirs("decompiled_clock/smali/com/samsung/android/util", exist_ok=True)

# 1. VibrationEffect$SemMagnitudeType.smali
with open("decompiled_clock/smali/android/os/VibrationEffect$SemMagnitudeType.smali", "w", encoding="utf-8") as f:
    f.write(""".class public final enum Landroid/os/VibrationEffect$SemMagnitudeType;
.super Ljava/lang/Enum;
.source "VibrationEffect.java"

# static fields
.field private static final synthetic $VALUES:[Landroid/os/VibrationEffect$SemMagnitudeType;

.field public static final enum TYPE_CALL:Landroid/os/VibrationEffect$SemMagnitudeType;
.field public static final enum TYPE_MAX:Landroid/os/VibrationEffect$SemMagnitudeType;
.field public static final enum TYPE_MIN:Landroid/os/VibrationEffect$SemMagnitudeType;
.field public static final enum TYPE_NOTIFICATION:Landroid/os/VibrationEffect$SemMagnitudeType;
.field public static final enum TYPE_TOUCH:Landroid/os/VibrationEffect$SemMagnitudeType;

# direct methods
.method static constructor <clinit>()V
    .locals 7

    new-instance v0, Landroid/os/VibrationEffect$SemMagnitudeType;
    const-string v1, "TYPE_TOUCH"
    const/4 v2, 0x0
    invoke-direct {v0, v1, v2}, Landroid/os/VibrationEffect$SemMagnitudeType;-><init>(Ljava/lang/String;I)V
    sput-object v0, Landroid/os/VibrationEffect$SemMagnitudeType;->TYPE_TOUCH:Landroid/os/VibrationEffect$SemMagnitudeType;

    new-instance v1, Landroid/os/VibrationEffect$SemMagnitudeType;
    const-string v2, "TYPE_NOTIFICATION"
    const/4 v3, 0x1
    invoke-direct {v1, v2, v3}, Landroid/os/VibrationEffect$SemMagnitudeType;-><init>(Ljava/lang/String;I)V
    sput-object v1, Landroid/os/VibrationEffect$SemMagnitudeType;->TYPE_NOTIFICATION:Landroid/os/VibrationEffect$SemMagnitudeType;

    new-instance v2, Landroid/os/VibrationEffect$SemMagnitudeType;
    const-string v3, "TYPE_CALL"
    const/4 v4, 0x2
    invoke-direct {v2, v3, v4}, Landroid/os/VibrationEffect$SemMagnitudeType;-><init>(Ljava/lang/String;I)V
    sput-object v2, Landroid/os/VibrationEffect$SemMagnitudeType;->TYPE_CALL:Landroid/os/VibrationEffect$SemMagnitudeType;

    new-instance v3, Landroid/os/VibrationEffect$SemMagnitudeType;
    const-string v4, "TYPE_MAX"
    const/4 v5, 0x3
    invoke-direct {v3, v4, v5}, Landroid/os/VibrationEffect$SemMagnitudeType;-><init>(Ljava/lang/String;I)V
    sput-object v3, Landroid/os/VibrationEffect$SemMagnitudeType;->TYPE_MAX:Landroid/os/VibrationEffect$SemMagnitudeType;

    new-instance v4, Landroid/os/VibrationEffect$SemMagnitudeType;
    const-string v5, "TYPE_MIN"
    const/4 v6, 0x4
    invoke-direct {v4, v5, v6}, Landroid/os/VibrationEffect$SemMagnitudeType;-><init>(Ljava/lang/String;I)V
    sput-object v4, Landroid/os/VibrationEffect$SemMagnitudeType;->TYPE_MIN:Landroid/os/VibrationEffect$SemMagnitudeType;

    const/4 v5, 0x5
    new-array v5, v5, [Landroid/os/VibrationEffect$SemMagnitudeType;
    const/4 v6, 0x0
    aput-object v0, v5, v6
    const/4 v0, 0x1
    aput-object v1, v5, v0
    const/4 v0, 0x2
    aput-object v2, v5, v0
    const/4 v0, 0x3
    aput-object v3, v5, v0
    const/4 v0, 0x4
    aput-object v4, v5, v0
    sput-object v5, Landroid/os/VibrationEffect$SemMagnitudeType;->$VALUES:[Landroid/os/VibrationEffect$SemMagnitudeType;

    return-void
.end method

.method private constructor <init>(Ljava/lang/String;I)V
    .locals 0

    invoke-direct {p0, p1, p2}, Ljava/lang/Enum;-><init>(Ljava/lang/String;I)V
    return-void
.end method

.method public static valueOf(Ljava/lang/String;)Landroid/os/VibrationEffect$SemMagnitudeType;
    .locals 1

    const-class v0, Landroid/os/VibrationEffect$SemMagnitudeType;
    invoke-static {v0, p0}, Ljava/lang/Enum;->valueOf(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Enum;
    move-result-object p0
    check-cast p0, Landroid/os/VibrationEffect$SemMagnitudeType;
    return-object p0
.end method

.method public static values()[Landroid/os/VibrationEffect$SemMagnitudeType;
    .locals 1

    sget-object v0, Landroid/os/VibrationEffect$SemMagnitudeType;->$VALUES:[Landroid/os/VibrationEffect$SemMagnitudeType;
    invoke-virtual {v0}, [Landroid/os/VibrationEffect$SemMagnitudeType;->clone()Ljava/lang/Object;
    move-result-object v0
    check-cast v0, [Landroid/os/VibrationEffect$SemMagnitudeType;
    return-object v0
.end method
""")

# 2. Activity$SemTranslucentConversionListener.smali
with open("decompiled_clock/smali/android/app/Activity$SemTranslucentConversionListener.smali", "w", encoding="utf-8") as f:
    f.write(""".class public interface abstract Landroid/app/Activity$SemTranslucentConversionListener;
.super Ljava/lang/Object;
.source "Activity.java"

# virtual methods
.method public abstract onTranslucentConversionComplete(Z)V
.end method
""")

print("Stub files written successfully.")
