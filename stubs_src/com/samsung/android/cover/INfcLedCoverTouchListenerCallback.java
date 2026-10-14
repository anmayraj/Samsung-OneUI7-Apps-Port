package com.samsung.android.cover;

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
