package com.samsung.android.cover;

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
