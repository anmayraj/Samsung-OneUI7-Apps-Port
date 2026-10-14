import os

# Update SemGfxImageFilter.java
with open("stubs_src/com/samsung/android/graphics/SemGfxImageFilter.java", "w", encoding="utf-8") as f:
    f.write("""package com.samsung.android.graphics;

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
""")

# Update SemTipPopup.java
with open("stubs_src/com/samsung/android/widget/SemTipPopup.java", "w", encoding="utf-8") as f:
    f.write("""package com.samsung.android.widget;

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
    public void setExpanded(boolean expanded) {}
    public void setTargetPosition(int x, int y) {}
    public void update() {}
}
""")

# Update SemStatusBarManager.java
with open("stubs_src/android/app/SemStatusBarManager.java", "w", encoding="utf-8") as f:
    f.write("""package android.app;

public class SemStatusBarManager {
    public SemStatusBarManager() {}
    public void collapsePanels() {}
    public void expandNotificationsPanel() {}
    public void disable(int state) {}
}
""")

# Update CoverState.java
with open("stubs_src/com/samsung/android/cover/CoverState.java", "w", encoding="utf-8") as f:
    f.write("""package com.samsung.android.cover;

import android.graphics.Rect;

public class CoverState {
    public boolean getSwitchState() { return true; }
    public int getType() { return 0; }
    public String getSmartCoverAppUri() { return null; }
    public Rect getVisibleRect() { return new Rect(); }
}
""")

# Update SemMediaPlayer.java
with open("stubs_src/com/samsung/android/media/SemMediaPlayer.java", "w", encoding="utf-8") as f:
    f.write("""package com.samsung.android.media;

import android.graphics.Bitmap;
import android.media.AudioAttributes;
import android.view.Surface;
import java.io.FileDescriptor;

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
    public boolean isLooping() { return false; }
    public void setLooping(boolean looping) {}
    public Bitmap getCurrentFrame() { return null; }
    public Bitmap getCurrentFrame(int w, int h) { return null; }
    public int getCurrentPosition() { return 0; }
    public int getDuration() { return 0; }
    public void init(FileDescriptor fd) {}
    public void init(FileDescriptor fd, long offset, long length) {}
    public void pause() {}
    public void release() {}
    public void seekTo(int msec, int mode) {}
    public void setAudioAttributes(AudioAttributes attributes) {}
    public void setOnErrorListener(OnErrorListener listener) {}
    public void setOnInfoListener(OnInfoListener listener) {}
    public void setOnInitCompleteListener(OnInitCompleteListener listener) {}
    public void setOnPlaybackCompleteListener(OnPlaybackCompleteListener listener) {}
    public boolean setParameter(int key, int value) { return true; }
    public void setPlaybackRange(int start, int end) {}
    public void setSurface(Surface surface) {}
    public void setVolume(float left, float right) {}
    public void start() {}
}
""")

# Update SemVideoTranscoder.java
with open("stubs_src/com/samsung/android/media/codec/SemVideoTranscoder.java", "w", encoding="utf-8") as f:
    f.write("""package com.samsung.android.media.codec;

public class SemVideoTranscoder {
    public SemVideoTranscoder() {}
    public void setTrimTime(long start, long end) {}
    public void rewrite() {}
    public void encode() {}
    public void initialize(String inPath, int outWidth, int outHeight, String outPath) {}
    public void setVideoTranscodingServiceCallback(SemVideoTranscodingService.ProgressCallback callback) {}
    public void stop() {}
}
""")

print("Updated all stub Java sources.")
