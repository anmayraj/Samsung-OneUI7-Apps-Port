import os
import re

found = set()
for root, dirs, files in os.walk("decompiled_clock"):
    for f in files:
        if f.endswith(".smali"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                for line in fp:
                    if "Landroid/os/Build$VERSION;->SEM_" in line or "Landroid/os/Build;->SEM_" in line:
                        found.add(line.strip())

print(f"Found SEM fields on Build: {len(found)}")
for l in sorted(list(found)):
    print(" ", l)
