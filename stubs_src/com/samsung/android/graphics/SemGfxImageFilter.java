package com.samsung.android.graphics;

import android.graphics.Bitmap;

public class SemGfxImageFilter {
    public SemGfxImageFilter() {}
    public void setSaturation(float saturation) {}
    public void setCurve(float[] curve) {}
    public void setBlurRadius(float radius) {}
    public void setBlurQuality(float quality) {}
    public void setBlurPreset(int preset) {}
    public Bitmap applyToBitmap(Bitmap bitmap) { return bitmap; }
}
