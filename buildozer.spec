[app]

# (str) Title of your application
title = Password Strength Checker

# (str) Package name
package.name = passwordchecker

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source directory where the app lives
source.dir = .

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pillow

# (list) Permissions
android.permissions = INTERNET

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Application android API to use
android.api = 33

# (list) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use ( Ye 25b sabse stable hai, aidl ka error nahi aayega )
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (bool) Use Android X
android.androidx = True

# (str) The Android arch to build for, in parallel
android.archs = arm64-v8a, armeabi-v7a


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact, local or absolute
bin_dir = ./bin
