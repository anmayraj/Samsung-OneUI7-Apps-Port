package com.samsung.android.feature;

public class SemCscFeature {
    private static final SemCscFeature sInstance = new SemCscFeature();

    public static SemCscFeature getInstance() {
        return sInstance;
    }

    public boolean getBoolean(String tag) {
        return false;
    }

    public boolean getBoolean(String tag, boolean defaultValue) {
        return defaultValue;
    }

    public String getString(String tag) {
        return "";
    }

    public String getString(String tag, String defaultValue) {
        return defaultValue;
    }

    public int getInt(String tag) {
        return 0;
    }

    public int getInt(String tag, int defaultValue) {
        return defaultValue;
    }
}
