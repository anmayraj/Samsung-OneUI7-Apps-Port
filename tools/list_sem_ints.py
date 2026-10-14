import os
import re

found = []
for root, dirs, files in os.walk("decompiled_clock"):
    for f in files:
        if f.endswith(".smali"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                for line in fp:
                    if "SEM_INT" in line or "SEM_PLATFORM_INT" in line or "SEM_FIRST_SDK_INT" in line:
                        found.append((f, line.strip()))

print(f"Total SEM Build lines: {len(found)}")
for f, l in found:
    print(f, "->", l)
