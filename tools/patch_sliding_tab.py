import os
import re

handle_path = os.path.join("decompiled_clock", "smali_classes5", "com", "sec", "android", "app", "clockpackage", "commonalert", "view", "AlertSlidingTabHandle.smali")

with open(handle_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace isInCircle(FFZIZI)Z
old_is_in_circle = re.search(r'\.method public final isInCircle\(FFZIZI\)Z.*?\.end method', code, re.DOTALL)
new_is_in_circle = """.method public final isInCircle(FFZIZI)Z
    .locals 5

    iput p4, p0, Lcom/sec/android/app/clockpackage/commonalert/view/AlertSlidingTabHandle;->mTopOffset:I

    iput p6, p0, Lcom/sec/android/app/clockpackage/commonalert/view/AlertSlidingTabHandle;->mDiameter:I

    invoke-virtual {p0}, Landroid/view/View;->getLeft()I

    move-result p3

    invoke-virtual {p0}, Landroid/view/View;->getWidth()I

    move-result p4

    div-int/lit8 p4, p4, 0x2

    add-int/2addr p3, p4

    int-to-float p3, p3

    invoke-virtual {p0}, Landroid/view/View;->getTop()I

    move-result p4

    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result v0

    div-int/lit8 v0, v0, 0x2

    add-int/2addr p4, v0

    int-to-float p4, p4

    sub-float/2addr p1, p3

    float-to-double v0, p1

    invoke-static {v0, v1}, Ljava/lang/Math;->abs(D)D

    move-result-wide v0

    sub-float/2addr p2, p4

    float-to-double p1, p2

    invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D

    move-result-wide p1

    mul-double/2addr v0, v0

    mul-double/2addr p1, p1

    add-double/2addr p1, v0

    invoke-static {p1, p2}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide p1

    iget p3, p0, Lcom/sec/android/app/clockpackage/commonalert/view/AlertSlidingTabHandle;->mDiameter:I

    if-gtz p3, :cond_0

    invoke-virtual {p0}, Landroid/view/View;->getWidth()I

    move-result p3

    if-gtz p3, :cond_0

    const/16 p3, 0xc8

    :cond_0
    int-to-double p3, p3

    div-double/2addr p1, p3

    const-wide v0, 0x3ff3333333333333L    # 1.2

    cmpg-double p0, p1, v0

    if-gez p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    const/4 p0, 0x0

    return p0
.end method"""

if old_is_in_circle:
    code = code.replace(old_is_in_circle.group(0), new_is_in_circle)
    print("Replaced isInCircle successfully!")
else:
    print("Could not find isInCircle!")

# 2. Replace getTargetProximityRatio(FFIIZ)D
old_proximity = re.search(r'\.method public final getTargetProximityRatio\(FFIIZ\)D.*?\.end method', code, re.DOTALL)
new_proximity = """.method public final getTargetProximityRatio(FFIIZ)D
    .locals 5

    iput p3, p0, Lcom/sec/android/app/clockpackage/commonalert/view/AlertSlidingTabHandle;->mTopOffset:I

    iput p4, p0, Lcom/sec/android/app/clockpackage/commonalert/view/AlertSlidingTabHandle;->mDiameter:I

    invoke-virtual {p0}, Landroid/view/View;->getLeft()I

    move-result p3

    invoke-virtual {p0}, Landroid/view/View;->getWidth()I

    move-result v0

    div-int/lit8 v0, v0, 0x2

    add-int/2addr p3, v0

    int-to-float p3, p3

    invoke-virtual {p0}, Landroid/view/View;->getTop()I

    move-result v0

    invoke-virtual {p0}, Landroid/view/View;->getHeight()I

    move-result v1

    div-int/lit8 v1, v1, 0x2

    add-int/2addr v0, v1

    int-to-float v0, v0

    sub-float/2addr p1, p3

    float-to-double v1, p1

    invoke-static {v1, v2}, Ljava/lang/Math;->abs(D)D

    move-result-wide v1

    sub-float/2addr p2, v0

    float-to-double p1, p2

    invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D

    move-result-wide p1

    mul-double/2addr v1, v1

    mul-double/2addr p1, p1

    add-double/2addr p1, v1

    invoke-static {p1, p2}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide p1

    iget p3, p0, Lcom/sec/android/app/clockpackage/commonalert/view/AlertSlidingTabHandle;->mDiameter:I

    if-gtz p3, :cond_0

    invoke-virtual {p0}, Landroid/view/View;->getWidth()I

    move-result p3

    if-gtz p3, :cond_0

    const/16 p3, 0xc8

    :cond_0
    int-to-double v0, p3

    div-double/2addr p1, v0

    return-wide p1
.end method"""

if old_proximity:
    code = code.replace(old_proximity.group(0), new_proximity)
    print("Replaced getTargetProximityRatio successfully!")
else:
    print("Could not find getTargetProximityRatio!")

with open(handle_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated AlertSlidingTabHandle.smali")
