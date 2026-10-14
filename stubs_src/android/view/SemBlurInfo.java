package android.view;

public class SemBlurInfo {
    public static class Builder {
        public Builder(int type) {}
        public Builder setRadius(int radius) { return this; }
        public Builder setColorCurve(float a, float b, float c, float d, float e, float f) { return this; }
        public Builder setColorCurvePreset(int preset) { return this; }
        public SemBlurInfo build() { return new SemBlurInfo(); }
    }
}
