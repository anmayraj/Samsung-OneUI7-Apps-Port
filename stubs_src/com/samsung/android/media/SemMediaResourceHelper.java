package com.samsung.android.media;

public class SemMediaResourceHelper {
    public static SemMediaResourceHelper createInstance(int type, boolean flag) {
        return new SemMediaResourceHelper();
    }
    public int getMaxVideoCapacity() { return 10; }
    public int getRemainedVideoCapacity() { return 10; }
}
