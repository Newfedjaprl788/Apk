[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Минимальная версия SDK
android.minapi = 24
android.sdk = 34
android.ndk = 25b
android.arch = armeabi-v7a, arm64-v8a, x86_64
permissions = INTERNET
