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
