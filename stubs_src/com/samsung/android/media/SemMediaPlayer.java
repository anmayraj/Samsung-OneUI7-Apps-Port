package com.samsung.android.media;

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
