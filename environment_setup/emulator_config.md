<<<<<<< HEAD
Android Emulator Configuration – TestQua31 Final Project

This document contains the exact emulator settings used for running Appium mobile automation tests on the Calculator app.
Member 2 will rely on this configuration when running and debugging test scripts.

1. Emulator Details
Setting	                Value
Device Name	            Pixel 8
Android Version	        Android 14
API Level	            API 34
System Image	        Google Play (x86_64)
Orientation	            Portrait
Skin	                Default Pixel skin
RAM / VM Heap	        Default (auto-assigned)

2. AVD Name
    Pixel_8_API_34


ADB identifier:

    emulator-5554


Matches desired capabilities:

    "appium:deviceName": "emulator-5554"


3. Emulator Settings

    -Cold Boot every time: OFF

    -Graphics: Automatic

    -Device Frame: ON

    -Use Host GPU: ON

    -Keyboard Input: Enabled

    -Internal Storage: Default

    -SD Card: Not required


4. How to Start the Emulator

    1. Open Device Manager in Android Studio

    2. Click ▶ Play next to Pixel_8_API_34

    3. Wait until fully booted


5. Verify with ADB (via CMD)

Open Command Prompt (CMD):

    adb devices

Expected:

    emulator-5554   device


6. Notes for Group Members

    -Emulator must be fully booted before running tests

    -Keep it open during Appium Inspector and Python test execution

    -Use the same emulator name and ADB ID for consistency


7. (Optional) Verify Calculator Installation

To confirm the Google Calculator app exists, run:

    adb shell pm list packages | findstr calculator

Expected:

    package:com.google.android.calculator


=======
Android Emulator Configuration – TestQua31 Final Project

This document contains the exact emulator settings used for running Appium mobile automation tests on the Calculator app.
Member 2 will rely on this configuration when running and debugging test scripts.

1. Emulator Details
Setting	                Value
Device Name	            Pixel 8
Android Version	        Android 14
API Level	            API 34
System Image	        Google Play (x86_64)
Orientation	            Portrait
Skin	                Default Pixel skin
RAM / VM Heap	        Default (auto-assigned)

2. AVD Name
    Pixel_8_API_34


ADB identifier:

    emulator-5554


Matches desired capabilities:

    "appium:deviceName": "emulator-5554"


3. Emulator Settings

    -Cold Boot every time: OFF

    -Graphics: Automatic

    -Device Frame: ON

    -Use Host GPU: ON

    -Keyboard Input: Enabled

    -Internal Storage: Default

    -SD Card: Not required


4. How to Start the Emulator

    1. Open Device Manager in Android Studio

    2. Click ▶ Play next to Pixel_8_API_34

    3. Wait until fully booted


5. Verify with ADB (via CMD)

Open Command Prompt (CMD):

    adb devices

Expected:

    emulator-5554   device


6. Notes for Group Members

    -Emulator must be fully booted before running tests

    -Keep it open during Appium Inspector and Python test execution

    -Use the same emulator name and ADB ID for consistency


7. (Optional) Verify Calculator Installation

To confirm the Google Calculator app exists, run:

    adb shell pm list packages | findstr calculator

Expected:

    package:com.google.android.calculator


>>>>>>> 4081c466a72acf09a7777b0da79e8fe6b0ab2e44
If missing, install it via the Play Store on the emulator.