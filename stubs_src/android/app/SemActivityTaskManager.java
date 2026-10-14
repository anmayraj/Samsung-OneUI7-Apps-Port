package android.app;

public class SemActivityTaskManager {
    private static final SemActivityTaskManager sInstance = new SemActivityTaskManager();

    public static SemActivityTaskManager getInstance() {
        return sInstance;
    }

    public int getCameraCutoutSetting(int userId, String packageName) {
        return 0;
    }
}
