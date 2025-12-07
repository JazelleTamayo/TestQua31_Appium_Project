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

