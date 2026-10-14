package com.samsung.android.util;

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
