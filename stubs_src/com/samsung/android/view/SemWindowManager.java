package com.samsung.android.view;

import android.content.ComponentName;
import android.os.Handler;

public class SemWindowManager {
    private static final SemWindowManager sInstance = new SemWindowManager();

    public static SemWindowManager getInstance() {
        return sInstance;
    }

    public boolean isFolded() {
        return false;
    }

    public interface FoldStateListener {
        void onFoldStateChanged(boolean isFolded);
    }

    public void registerFoldStateListener(FoldStateListener listener, Handler handler) {}
    public void unregisterFoldStateListener(FoldStateListener listener) {}

    public boolean requestSystemKeyEvent(int keyCode, ComponentName componentName, boolean request) {
        return false;
    }
}
