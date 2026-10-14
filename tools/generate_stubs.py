import os

stubs = {}

stubs["stubs_src/com/samsung/android/feature/SemFloatingFeature.java"] = """package com.samsung.android.feature;

public class SemFloatingFeature {
    private static final SemFloatingFeature sInstance = new SemFloatingFeature();

    public static SemFloatingFeature getInstance() {
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
"""

stubs["stubs_src/com/samsung/android/feature/SemCscFeature.java"] = """package com.samsung.android.feature;

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
"""

stubs["stubs_src/com/samsung/android/util/SemLog.java"] = """package com.samsung.android.util;

import android.util.Log;

public class SemLog {
    public static int v(String tag, String msg) { return Log.v(tag, msg); }
    public static int d(String tag, String msg) { return Log.d(tag, msg); }
    public static int i(String tag, String msg) { return Log.i(tag, msg); }
    public static int w(String tag, String msg) { return Log.w(tag, msg); }
    public static int e(String tag, String msg) { return Log.e(tag, msg); }
    public static int e(String tag, String msg, Throwable tr) { return Log.e(tag, msg, tr); }
    public static int secV(String tag, String msg) { return Log.v(tag, msg); }
    public static int secD(String tag, String msg) { return Log.d(tag, msg); }
    public static int secI(String tag, String msg) { return Log.i(tag, msg); }
    public static int secW(String tag, String msg) { return Log.w(tag, msg); }
    public static int secE(String tag, String msg) { return Log.e(tag, msg); }
    public static int wtf(String tag, String msg) { return Log.wtf(tag, msg); }
}
"""

stubs["stubs_src/com/samsung/android/view/SemWindowManager.java"] = """package com.samsung.android.view;

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
"""

stubs["stubs_src/com/samsung/android/app/SemMultiWindowManager.java"] = """package com.samsung.android.app;

public class SemMultiWindowManager {
    public SemMultiWindowManager() {}
    public int getMode() { return 0; }
}
"""

stubs["stubs_src/com/samsung/android/knox/SemPersonaManager.java"] = """package com.samsung.android.knox;

public class SemPersonaManager {
    public static boolean isKnoxId(int userId) { return false; }
    public static boolean isSecureFolderId(int userId) { return false; }
}
"""

stubs["stubs_src/com/samsung/android/game/SemGameManager.java"] = """package com.samsung.android.game;

public class SemGameManager {
    public SemGameManager() {}
    public boolean isForegroundGame() { return false; }
}
"""

stubs["stubs_src/com/samsung/android/gesture/SemMotionEventListener.java"] = """package com.samsung.android.gesture;

public interface SemMotionEventListener {
    void onMotionEvent(SemMotionRecognitionEvent event);
}
"""

stubs["stubs_src/com/samsung/android/gesture/SemMotionRecognitionEvent.java"] = """package com.samsung.android.gesture;

public class SemMotionRecognitionEvent {
    public int getMotion() { return 0; }
}
"""

stubs["stubs_src/com/samsung/android/gesture/SemMotionRecognitionManager.java"] = """package com.samsung.android.gesture;

public class SemMotionRecognitionManager {
    public SemMotionRecognitionManager() {}
    public void registerListener(SemMotionEventListener listener, int motion) {}
    public void unregisterListener(SemMotionEventListener listener) {}
}
"""

stubs["stubs_src/com/samsung/android/widget/SemTipPopup.java"] = """package com.samsung.android.widget;

import android.view.View;

public class SemTipPopup {
    public interface OnStateChangeListener {
        void onStateChanged(int state);
    }

    public SemTipPopup(View anchor) {}
    public void setMessage(CharSequence message) {}
    public void show(int direction) {}
    public void dismiss(boolean animate) {}
    public boolean isShowing() { return false; }
    public void setOnStateChangeListener(OnStateChangeListener listener) {}
}
"""

stubs["stubs_src/com/samsung/android/sdhms/SemAppRestrictionManager.java"] = """package com.samsung.android.sdhms;

import android.content.Context;

public class SemAppRestrictionManager {
    public static class RestrictionInfo {
        public int state = 0;
    }

    public SemAppRestrictionManager(Context context) {}

    public RestrictionInfo getRestrictionInfo(int type, String packageName, int uid) {
        return new RestrictionInfo();
    }
}
"""

stubs["stubs_src/com/samsung/android/graphics/SemGfxImageFilter.java"] = """package com.samsung.android.graphics;

import android.graphics.Bitmap;

public class SemGfxImageFilter {
    public SemGfxImageFilter() {}
    public void setSaturation(float saturation) {}
    public void setCurve(float[] curve) {}
    public void setBlurRadius(float radius) {}
    public Bitmap applyToBitmap(Bitmap bitmap) { return bitmap; }
}
"""

stubs["stubs_src/com/samsung/android/cover/CoverState.java"] = """package com.samsung.android.cover;

public class CoverState {
    public boolean getSwitchState() { return true; }
    public int getType() { return 0; }
}
"""

stubs["stubs_src/com/samsung/android/cover/ICoverManager.java"] = """package com.samsung.android.cover;

import android.os.Binder;
import android.os.IBinder;
import android.os.IInterface;

public interface ICoverManager extends IInterface {
    CoverState getCoverState();

    abstract class Stub extends Binder implements ICoverManager {
        public static ICoverManager asInterface(IBinder binder) {
            return null;
        }
    }
}
"""

stubs["stubs_src/com/samsung/android/cover/ICoverStateListenerCallback.java"] = """package com.samsung.android.cover;

import android.os.Binder;
import android.os.IBinder;
import android.os.IInterface;

public interface ICoverStateListenerCallback extends IInterface {
    abstract class Stub extends Binder implements ICoverStateListenerCallback {
        public static ICoverStateListenerCallback asInterface(IBinder binder) {
            return null;
        }
    }
}
"""

stubs["stubs_src/com/samsung/android/cover/ICoverManagerCallback.java"] = """package com.samsung.android.cover;

import android.os.Binder;
import android.os.IBinder;
import android.os.IInterface;

public interface ICoverManagerCallback extends IInterface {
    abstract class Stub extends Binder implements ICoverManagerCallback {
        public static ICoverManagerCallback asInterface(IBinder binder) {
            return null;
        }
    }
}
"""

stubs["stubs_src/com/samsung/android/cover/INfcLedCoverTouchListenerCallback.java"] = """package com.samsung.android.cover;

import android.os.Binder;
import android.os.IBinder;
import android.os.IInterface;

public interface INfcLedCoverTouchListenerCallback extends IInterface {
    abstract class Stub extends Binder implements INfcLedCoverTouchListenerCallback {
        public static INfcLedCoverTouchListenerCallback asInterface(IBinder binder) {
            return null;
        }
    }
}
"""

stubs["stubs_src/com/samsung/android/media/SemMediaResourceHelper.java"] = """package com.samsung.android.media;

public class SemMediaResourceHelper {
    public static SemMediaResourceHelper createInstance(int type, boolean flag) {
        return new SemMediaResourceHelper();
    }
    public int getMaxVideoCapacity() { return 10; }
    public int getRemainedVideoCapacity() { return 10; }
}
"""

stubs["stubs_src/com/samsung/android/media/SemMediaPlayer.java"] = """package com.samsung.android.media;

import android.graphics.Bitmap;

public class SemMediaPlayer {
    public static class TrackInfo {}
    public interface OnInitCompleteListener {
        void onInitComplete(SemMediaPlayer player, TrackInfo[] trackInfo);
    }
    public interface OnErrorListener {
        boolean onError(SemMediaPlayer mp, int what, int extra);
    }
    public interface OnInfoListener {
        boolean onInfo(SemMediaPlayer mp, int what, int extra);
    }
    public interface OnPlaybackCompleteListener {
        void onPlaybackComplete(SemMediaPlayer mp);
    }

    public SemMediaPlayer() {}
    public boolean isPlaying() { return false; }
    public Bitmap getCurrentFrame() { return null; }
    public void release() {}
}
"""

stubs["stubs_src/com/samsung/android/media/codec/SemVideoTranscoder.java"] = """package com.samsung.android.media.codec;

public class SemVideoTranscoder {
    public SemVideoTranscoder() {}
    public void setTrimTime(long start, long end) {}
    public void rewrite() {}
}
"""

stubs["stubs_src/com/samsung/android/media/codec/SemVideoTranscodingService.java"] = """package com.samsung.android.media.codec;

public class SemVideoTranscodingService {
    public interface ProgressCallback {
        void onProgressChanged(int progress);
    }
}
"""

for path, content in stubs.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(stubs)} stub Java source files.")
