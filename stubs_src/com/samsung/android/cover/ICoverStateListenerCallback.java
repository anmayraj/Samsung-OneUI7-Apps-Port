package com.samsung.android.cover;

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
