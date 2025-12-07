<<<<<<< HEAD
Environment & Tools Setup – TestQua31 Final Project
(ctr + shift + V)

Member 1 – Environment & Tools Lead

This document contains the full setup process for Appium, Android Studio, the Android Emulator, ADB, and Desired Capabilities used for mobile test automation in the Calculator app.

It serves as the technical foundation for Member 2’s automation scripts and Member 3’s documentation.

1. System Requirements

    -Windows 10/11

    -8GB RAM minimum

    -20GB free storage

Stable internet connection for SDK and package downloads

2. Python Installation

Download Python from:
    https://www.python.org/downloads/

Steps:

    1. Run the installer

    2. Check the option: Add Python to PATH

    3. Verify installation:

        python --version
        pip --version


Install Appium Python Client:

    pip install Appium-Python-Client


3. Node.js Installation

Download Node.js from:
    https://nodejs.org

Verify installation:

    node -v
    npm -v


4. Appium Server GUI Installation

    1. Download Appium Server GUI from:
        https://github.com/appium/appium-desktop/releases

    2. Install version 1.22.3

    3. Start the server with default settings:

        -Host: 0.0.0.0

        -Port: 4723

Verify server started by checking logs:

    Appium REST http interface listener started


5. Android Studio & Emulator Setup

    1. Install Android Studio

    2. Install Android SDK, Platform Tools, and Emulator

    3. Create a new Virtual Device

        -Device: Pixel 8

        -API Level: 34 (Android 14, Google Play Image)

        -CPU/ABI: x86_64

Start the emulator and wait for it to fully boot.


6. ADB Configuration

Add platform-tools to PATH:

    C:\Users\<YourUser>\AppData\Local\Android\Sdk\platform-tools


Verify emulator connection:

    adb devices


Expected output:

    emulator-5554   device


7. Installing Calculator App

If Calculator is missing, install it using Google Play Store.

Verify installation:

    adb shell pm list packages | findstr calculator


Expected:

    package:com.google.android.calculator


8. Appium Inspector Setup

    1. Install Appium Inspector

    2. Connect using:

        -Remote Host: 127.0.0.1

        -Port: 4723

        -Remote Path: /wd/hub

    3. Load the desired capabilities (see next section).

    4. Save the capability set using the Save As… button.


9. Desired Capabilities for Google Calculator

    {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "emulator-5554",
        "appium:appPackage": "com.google.android.calculator",
        "appium:appActivity": "com.android.calculator2.Calculator",
        "appium:noReset": true,
        "appium:fullReset": false
    }


These capabilities successfully launch the Google Calculator app in Appium Inspector.

⚠️ Note on appActivity

Sometimes different Android versions use a different Calculator activity name.If the app does not launch, verify the correct appActivity using:

    adb shell dumpsys window | findstr mCurrentFocus


This command will show the currently focused app window.
Use the output to update the value of:

"appium:appActivity": "<correct activity here>"


10. Inspector Verification

A successful session shows:

    -Calculator app automatically opens on the emulator

    -UI hierarchy loads in Inspector

    -Elements are selectable for Member 2's script writing

11. Notes for Group Members

    -Member 2 uses these capabilities in test scripts

    -Member 3 includes this documentation in the final project report

    -Emulator and Appium server must both be running before tests

12. Project Folder / Repository Setup

Main project folder: AutomatedMobileAppTesting_Appium_Python/

Shared storage:

    -Option A: GitHub repo (shared with all members)

    -Option B: Google Drive / OneDrive shared folder

Subfolders:

    -src/ – test scripts (Member 2)

    -docs/ – report, test cases (Member 3)

=======
Environment & Tools Setup – TestQua31 Final Project
(ctr + shift + V)

Member 1 – Environment & Tools Lead

This document contains the full setup process for Appium, Android Studio, the Android Emulator, ADB, and Desired Capabilities used for mobile test automation in the Calculator app.

It serves as the technical foundation for Member 2’s automation scripts and Member 3’s documentation.

1. System Requirements

    -Windows 10/11

    -8GB RAM minimum

    -20GB free storage

Stable internet connection for SDK and package downloads

2. Python Installation

Download Python from:
    https://www.python.org/downloads/

Steps:

    1. Run the installer

    2. Check the option: Add Python to PATH

    3. Verify installation:

        python --version
        pip --version


Install Appium Python Client:

    pip install Appium-Python-Client


3. Node.js Installation

Download Node.js from:
    https://nodejs.org

Verify installation:

    node -v
    npm -v


4. Appium Server GUI Installation

    1. Download Appium Server GUI from:
        https://github.com/appium/appium-desktop/releases

    2. Install version 1.22.3

    3. Start the server with default settings:

        -Host: 0.0.0.0

        -Port: 4723

Verify server started by checking logs:

    Appium REST http interface listener started


5. Android Studio & Emulator Setup

    1. Install Android Studio

    2. Install Android SDK, Platform Tools, and Emulator

    3. Create a new Virtual Device

        -Device: Pixel 8

        -API Level: 34 (Android 14, Google Play Image)

        -CPU/ABI: x86_64

Start the emulator and wait for it to fully boot.


6. ADB Configuration

Add platform-tools to PATH:

    C:\Users\<YourUser>\AppData\Local\Android\Sdk\platform-tools


Verify emulator connection:

    adb devices


Expected output:

    emulator-5554   device


7. Installing Calculator App

If Calculator is missing, install it using Google Play Store.

Verify installation:

    adb shell pm list packages | findstr calculator


Expected:

    package:com.google.android.calculator


8. Appium Inspector Setup

    1. Install Appium Inspector

    2. Connect using:

        -Remote Host: 127.0.0.1

        -Port: 4723

        -Remote Path: /wd/hub

    3. Load the desired capabilities (see next section).

    4. Save the capability set using the Save As… button.


9. Desired Capabilities for Google Calculator

    {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "emulator-5554",
        "appium:appPackage": "com.google.android.calculator",
        "appium:appActivity": "com.android.calculator2.Calculator",
        "appium:noReset": true,
        "appium:fullReset": false
    }


These capabilities successfully launch the Google Calculator app in Appium Inspector.

⚠️ Note on appActivity

Sometimes different Android versions use a different Calculator activity name.If the app does not launch, verify the correct appActivity using:

    adb shell dumpsys window | findstr mCurrentFocus


This command will show the currently focused app window.
Use the output to update the value of:

"appium:appActivity": "<correct activity here>"


10. Inspector Verification

A successful session shows:

    -Calculator app automatically opens on the emulator

    -UI hierarchy loads in Inspector

    -Elements are selectable for Member 2's script writing

11. Notes for Group Members

    -Member 2 uses these capabilities in test scripts

    -Member 3 includes this documentation in the final project report

    -Emulator and Appium server must both be running before tests

12. Project Folder / Repository Setup

Main project folder: AutomatedMobileAppTesting_Appium_Python/

Shared storage:

    -Option A: GitHub repo (shared with all members)

    -Option B: Google Drive / OneDrive shared folder

Subfolders:

    -src/ – test scripts (Member 2)

    -docs/ – report, test cases (Member 3)

>>>>>>> 4081c466a72acf09a7777b0da79e8fe6b0ab2e44
    -screenshots/, video/, slides/ – for final submission