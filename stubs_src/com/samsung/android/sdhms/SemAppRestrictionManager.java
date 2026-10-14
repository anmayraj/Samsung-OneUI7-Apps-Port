package com.samsung.android.sdhms;

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
