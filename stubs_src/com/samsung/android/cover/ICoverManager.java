package com.samsung.android.cover;

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
