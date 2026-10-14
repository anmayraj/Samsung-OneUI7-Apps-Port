import os

stubs = {}

stubs["stubs_src/android/os/SemSystemProperties.java"] = """package android.os;

public class SemSystemProperties {
    public static String get(String key) {
        return "";
    }
    public static String get(String key, String def) {
        return def;
    }
    public static boolean getBoolean(String key, boolean def) {
        return def;
    }
    public static int getInt(String key, int def) {
        return def;
    }
    public static String getCountryCode() {
        return "";
    }
    public static String getCountryIso() {
        return "";
    }
    public static String getSalesCode() {
        return "";
    }
}
"""

stubs["stubs_src/android/app/SemActivityTaskManager.java"] = """package android.app;

public class SemActivityTaskManager {
    private static final SemActivityTaskManager sInstance = new SemActivityTaskManager();

    public static SemActivityTaskManager getInstance() {
        return sInstance;
    }

    public int getCameraCutoutSetting(int userId, String packageName) {
        return 0;
    }
}
"""

stubs["stubs_src/android/app/SemStatusBarManager.java"] = """package android.app;

public class SemStatusBarManager {
    public SemStatusBarManager() {}
    public void collapsePanels() {}
    public void expandNotificationsPanel() {}
}
"""

stubs["stubs_src/android/view/SemBlurInfo.java"] = """package android.view;

public class SemBlurInfo {
    public static class Builder {
        public Builder(int type) {}
        public Builder setRadius(int radius) { return this; }
        public Builder setColorCurve(float a, float b, float c, float d, float e, float f) { return this; }
        public Builder setColorCurvePreset(int preset) { return this; }
        public SemBlurInfo build() { return new SemBlurInfo(); }
    }
}
"""

stubs["stubs_src/android/widget/SemRemoteViewsAnimation.java"] = """package android.widget;

public class SemRemoteViewsAnimation {
    public SemRemoteViewsAnimation() {}
}
"""

stubs["stubs_src/android/widget/SemRemoteViewsPropertyAnimation.java"] = """package android.widget;

public class SemRemoteViewsPropertyAnimation extends SemRemoteViewsAnimation {
    public SemRemoteViewsPropertyAnimation(int viewId, int property) {
        super();
    }
}
"""

stubs["stubs_src/android/widget/SemRemoteViewsDrawableAnimation.java"] = """package android.widget;

public class SemRemoteViewsDrawableAnimation extends SemRemoteViewsAnimation {
    public SemRemoteViewsDrawableAnimation(int viewId, boolean isReverse, int duration) {
        super();
    }
}
"""

stubs["stubs_src/android/widget/SemRemoteViewsValueAnimation.java"] = """package android.widget;

public class SemRemoteViewsValueAnimation extends SemRemoteViewsAnimation {
    public SemRemoteViewsValueAnimation(int viewId, String method, String property, int from, int to, long duration) {
        super();
    }
    public SemRemoteViewsValueAnimation(int viewId, String method, String property, float from, float to, long duration) {
        super();
    }
}
"""

for path, content in stubs.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(stubs)} additional android.* stub Java source files.")
