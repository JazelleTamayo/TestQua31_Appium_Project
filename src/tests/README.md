MEMBER 2 
TEST CODE:
1.	Install required software (Member 1’s Task)
2.	Prepare the emulator 
    •	Open Android Studio → Virtual Device Manager
    •	Start your emulator (e.g. Pixel device).
    •	Make sure the Calculator app is installed:
    •	Use the default Google Calculator (usually already there).
    
3.	Start Appium server
    •	Open Appium Server GUI
    •	Set:
        Host: 0.0.0.0
        Port: 4723
        Path: /wd/hub
    •	Click Start Server.
    •	Keep this running while you test.

4.	Create the project folder
    
    <project-root>/
└─ src/
   └─ tests/
      ├─ __init__.py 
      ├─ requirements.txt
      ├─ test_addition.py
      ├─ test_clear_button.py
      ├─ test_multiplication.py
      └─ __pycache__/   # (auto-created by Python)
   ├─ venv/             # (created later – Python virtual environment)
   └─ __pycache__/      # (auto-created by Python)
   ├─ driver_setup.py
   └─ .pytest_cache_/   # (auto-created by Python)

5.	Add dependencies
Open requirements.txt and put:
    Appium-Python-Client
    pytest


6.	Create + activate virtual environment
Open a terminal inside scr :
 
    python -m venv venv

Activate it:
Windows:

    C:\Users\Jasmin Jeminez\OneDrive\Desktop\src>venv\Scripts\activate

 
You should see (venv) at the start of the line.

    (venv)  C:\Users\Jasmin Jeminez\OneDrive\Desktop\src>

 
7.	Install Python packages

    pip install -r requirements.txt
 
8.	Configure driver_setup.py

Open driver_setup.py and add:

from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    # Define capabilities using UiAutomator2Options (new Appium style)
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"  # D
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


This connects Appium → emulator → Calculator app.


9.	Test 1 – Addition (7 + 8 = 15)

Create/tests/test_addition.py:

from time import sleep

from driver_setup import create_driver
from appium.webdriver.common.appiumby import AppiumBy


def get_result_field(driver):
    
    possible_ids = [
        "com.google.android.calculator:id/result_final",
        "com.google.android.calculator:id/result_preview",
        "com.google.android.calculator:id/formula",
        "com.google.android.calculator:id/result",
    ]

    for rid in possible_ids:
        try:
            return driver.find_element(AppiumBy.ID, rid)
        except Exception:
            continue

    raise Exception(f"Could not find result field. Tried: {possible_ids}")


def test_addition_7_plus_8_equals_15():
    driver = create_driver()

    try:
        btn_7 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_7")
        btn_8 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_8")
        btn_plus = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add")
        btn_equals = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq")

        # 7 + 8 =
        btn_7.click()
        btn_plus.click()
        btn_8.click()
        btn_equals.click()

        sleep(1)
        result_field = get_result_field(driver)
        result = result_field.text
        print("Addition result:", repr(result))

        assert "15" in result, f"Expected 15 in result, but got {result!r}"

        driver.get_screenshot_as_file("screenshots/addition_7_plus_8.png")

    finally:
        driver.quit()


10.	Test 2 – Clear Button

Create/tests/test_clear_button.py:

from driver_setup import create_driver
from appium.webdriver.common.appiumby import AppiumBy


def get_result_field(driver):
    possible_ids = [
        "com.google.android.calculator:id/result_final",
        "com.google.android.calculator:id/result_preview",
        "com.google.android.calculator:id/formula",
        "com.google.android.calculator:id/result",
    ]
    for rid in possible_ids:
        try:
            return driver.find_element(AppiumBy.ID, rid)
        except Exception:
            continue
    raise Exception(f"Could not find result field. Tried: {possible_ids}")


def test_clear_button_clears_result():
    driver = create_driver()

    try:
        btn_9 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_9")
        btn_plus = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add")
        btn_1 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_1")
        btn_equals = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq")
        btn_clear = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/clr")
        result_field = get_result_field(driver)

        # 9 + 1 =
        btn_9.click()
        btn_plus.click()
        btn_1.click()
        btn_equals.click()

        # Clear the result
        btn_clear.click()

        result = result_field.text
        print("Result after clear:", repr(result))

        normalized = result.strip()
        assert normalized in ("", "0"), f"Expected empty or 0 after clear, but got {result!r}"

        driver.get_screenshot_as_file("screenshots/clear_button.png")

    finally:
        driver.quit()

11.	Test 3 – Multiplication (6 × 7 = 42)

Create/tests/test_multiplication.py:

from time import sleep

from driver_setup import create_driver
from appium.webdriver.common.appiumby import AppiumBy


def get_result_field(driver):
    possible_ids = [
        "com.google.android.calculator:id/result_final",
        "com.google.android.calculator:id/result_preview",
        "com.google.android.calculator:id/formula",
        "com.google.android.calculator:id/result",
    ]
    for rid in possible_ids:
        try:
            return driver.find_element(AppiumBy.ID, rid)
        except Exception:
            continue
    raise Exception(f"Could not find result field. Tried: {possible_ids}")


def test_multiplication_6_times_7_equals_42():
    driver = create_driver()

    try:
        btn_6 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_6")
        btn_7 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_7")
        btn_multiply = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_mul")
        btn_equals = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq")

        # 6 × 7 =
        btn_6.click()
        btn_multiply.click()
        btn_7.click()
        btn_equals.click()

        sleep(1)
        result_field = get_result_field(driver)
        result = result_field.text
        print("Multiplication result:", repr(result))

        assert "42" in result, f"Expected 42 in result, but got {result!r}"

        driver.get_screenshot_as_file("screenshots/multiplication_6_times_7.png")

    finally:
        driver.quit()

12.	Start everything

    •	Start Android emulator
    •	Start Appium Server GUI
    •	Make sure venv is active


13.	Run all tests
From inside scr:

    Microsoft Windows [Version 10.0.26200.7171]
    (c) Microsoft Corporation. All rights reserved.

    C:\Users\Jasmin Jeminez\OneDrive\Desktop\src>pytest -v

 
You should see:
    •	Emulator automatically opens Calculator
    •	Buttons press themselves
    •	Results appear
    •	All 3 tests show PASSED
    •	PNG screenshots created inside screenshots/ 

 
