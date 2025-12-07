from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    # Define capabilities using UiAutomator2Options (new Appium style)
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"  
    options.app_package = "com.google.android.calculator"
    options.app_activity = "com.android.calculator2.Calculator"
    options.no_reset = True
    options.full_reset = False

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        options=options,
    )

    driver.implicitly_wait(10)
    return driver
