# 1. Patch AndroidManifest.xml
with open("decompiled_clock/AndroidManifest.xml", "r", encoding="utf-8") as f:
    manifest = f.read()

manifest = manifest.replace(
    '<uses-native-library android:name="libagifencoder.quram.so" android:required="true"/>',
    '<uses-native-library android:name="libagifencoder.quram.so" android:required="false"/>'
)

with open("decompiled_clock/AndroidManifest.xml", "w", encoding="utf-8") as f:
    f.write(manifest)
print("Patched AndroidManifest.xml uses-native-library to required=false")

# 2. Patch QuramAGIFDecoder.smali
dec_path = "decompiled_clock/smali/com/quramsoft/agifDecoder/QuramAGIFDecoder.smali"
with open(dec_path, "r", encoding="utf-8") as f:
    dec = f.read()
dec = dec.replace(".catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0",
                  ".catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0")
with open(dec_path, "w", encoding="utf-8") as f:
    f.write(dec)
print("Patched QuramAGIFDecoder.smali")

# 3. Patch QuramAGIFEncoder.smali
enc_path = "decompiled_clock/smali/com/quramsoft/agifEncoder/QuramAGIFEncoder.smali"
with open(enc_path, "r", encoding="utf-8") as f:
    enc = f.read()
enc = enc.replace(".catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0",
                  ".catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0")
with open(enc_path, "w", encoding="utf-8") as f:
    f.write(enc)
print("Patched QuramAGIFEncoder.smali")
