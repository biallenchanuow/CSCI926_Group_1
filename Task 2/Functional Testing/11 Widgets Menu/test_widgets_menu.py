from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Jupyter Notebook Functional Test
    Package: WidgetsMenu
    Test: Widgets Menu
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 05/05/2021, 12:07:12
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="Widgets Menu")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "http://localhost:8888/tree"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'functional test folder'
    functional_test_folder = driver.find_element(By.XPATH,
                                                 "//span[. = 'functional test folder']")
    functional_test_folder.click()

    # 3. Click 'test_editor_02.ipynb1'
    test_editor_02_ipynb1 = driver.find_element(By.XPATH,
                                                "//span[. = 'test_editor_02.ipynb']")
    test_editor_02_ipynb1.click()

    # 4. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 5. Type 'Hello World' in 'TEXTAREA4'
    textarea4 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea4.send_keys("Hello World")

    # 6. Click 'Widgets'
    widgets = driver.find_element(By.XPATH,
                                  "//a[. = 'Widgets']")
    widgets.click()

    # 7. Click 'Save Notebook Widget State'
    save_notebook_widget_state = driver.find_element(By.XPATH,
                                                     "//a[. = 'Save Notebook Widget State']")
    save_notebook_widget_state.click()

    # 8. Close window with index '1'
    driver.close()

    # 9. Switch to window '0'
    driver.switch_to.window(driver.window_handles[0])

    # 10. Click 'test_editor_02.ipynb1'
    test_editor_02_ipynb1 = driver.find_element(By.XPATH,
                                                "//span[. = 'test_editor_02.ipynb']")
    test_editor_02_ipynb1.click()

    # 11. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 12. Click 'Widgets'
    widgets = driver.find_element(By.XPATH,
                                  "//a[. = 'Widgets']")
    widgets.click()

    # 13. Click 'Clear Notebook Widget State'
    clear_notebook_widget_state = driver.find_element(By.XPATH,
                                                      "//a[. = 'Clear Notebook Widget State']")
    clear_notebook_widget_state.click()

    # 14. Close window with index '1'
    driver.close()

    # 15. Switch to window '0'
    driver.switch_to.window(driver.window_handles[0])

    # 16. Click 'test_editor_02.ipynb1'
    test_editor_02_ipynb1 = driver.find_element(By.XPATH,
                                                "//span[. = 'test_editor_02.ipynb']")
    test_editor_02_ipynb1.click()

    # 17. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 18. Click 'Widgets'
    widgets = driver.find_element(By.XPATH,
                                  "//a[. = 'Widgets']")
    widgets.click()

    # 19. Click 'Download Widget State'
    download_widget_state = driver.find_element(By.XPATH,
                                                "//a[. = 'Download Widget State']")
    download_widget_state.click()

    # 20. Click 'Widgets'
    widgets = driver.find_element(By.XPATH,
                                  "//a[. = 'Widgets']")
    widgets.click()

    # 21. Click 'Embed Widgets'
    embed_widgets = driver.find_element(By.XPATH,
                                        "//a[. = 'Embed Widgets']")
    embed_widgets.click()

    # 22. Click 'Copy to Clipboard'
    copy_to_clipboard = driver.find_element(By.XPATH,
                                            "//button[. = 'Copy to Clipboard']")
    copy_to_clipboard.click()
