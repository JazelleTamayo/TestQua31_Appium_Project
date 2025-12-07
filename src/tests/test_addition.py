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
