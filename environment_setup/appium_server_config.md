Appium Server Configuration – TestQua31 Final Project

This document contains the Appium Server GUI settings used for running mobile automation tests in this project.
Member 2 will use this configuration to execute Python test scripts.

1. Appium Version

We are using:

    Appium Server GUI 1.22.3


This is the recommended stable version for Appium Inspector and UiAutomator2.

Download link:
    https://github.com/appium/appium-desktop/releases


2. Server Host and Port

Appium server was started with default settings:

Setting	        Value
Host	        0.0.0.0
Port	        4723
Remote Path	    /wd/hub

These settings must match the Python test script and Appium Inspector connection.


3. Starting the Appium Server
Using Appium Server GUI
    1. Open Appium Server GUI
    2. Click Start Server
    3. Wait until the logs show:
        Appium REST http interface listener started on 0.0.0.0:4723

This confirms the server is ready and listening.


4. Verifying the Server is Running
Option A — Using Appium GUI Logs

Look for:

    [Appium] Welcome to Appium v1.22.3
    [Appium] Appium REST http interface listener started on 0.0.0.0:4723

Option B — Using Web Browser

Open:

    http://0.0.0.0:4723/wd/hub/status

You should see:

    "status": 0

or “Appium is running”.


5. Required Settings for UiAutomator2
No extra configuration needed.

Appium automatically loads:
    -UiAutomator2 driver
    -Android platform tools

Just ensure:
    -Emulator is running
    -ADB is connected
    -Appium Server GUI is started before running Python tests

6. Notes for Group Members
    -Start Appium Server before opening Appium Inspector or running test scripts.
    -Server must stay open during the entire test execution.
    -If another app is using port 4723, Appium will fail to start — close the conflicting program.
    -If the host or port changes, update the Python test scripts accordingly.


7. Example Python Connection (for Member 2)

This is the expected connection setup:

    from appium import webdriver

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        desired_capabilities=desired_caps
    )


This matches the exact server settings from this configuration file.