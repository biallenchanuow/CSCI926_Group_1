from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Jupyter Notebook Functional Test
    Package: CellMenuCurrentOutputs
    Test: Cell Menu - Current Outputs
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 05/05/2021, 11:43:49
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="Cell Menu - Current Outputs")
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

    # 3. Click 'test_editor_02.ipynb'
    test_editor_02_ipynb = driver.find_element(By.XPATH,
                                               "//span[. = 'test_editor_02.ipynb']")
    test_editor_02_ipynb.click()

    # 4. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 5. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 6. Click 'Toggle'
    toggle = driver.find_element(By.XPATH,
                                 "//span[. = 'Toggle']")
    toggle.click()

    # 7. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 8. Click 'Toggle Scrolling'
    toggle_scrolling = driver.find_element(By.XPATH,
                                           "//span[. = 'Toggle Scrolling']")
    toggle_scrolling.click()

    # 9. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 10. Click 'Clear'
    clear = driver.find_element(By.XPATH,
                                "//li[10]//a[. = 'Clear']")
    clear.click()

    # 11. Type 'Hello World' in 'TEXTAREA4'
    textarea4 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea4.send_keys("Hello World")

    # 12. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 13. Click 'Toggle'
    toggle = driver.find_element(By.XPATH,
                                 "//span[. = 'Toggle']")
    toggle.click()

    # 14. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 15. Click 'Toggle Scrolling'
    toggle_scrolling = driver.find_element(By.XPATH,
                                           "//span[. = 'Toggle Scrolling']")
    toggle_scrolling.click()

    # 16. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 17. Click 'Clear'
    clear = driver.find_element(By.XPATH,
                                "//li[10]//a[. = 'Clear']")
    clear.click()

    # 18. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 19. Click 'Run Cells'
    run_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Run Cells']")
    run_cells.click()

    # 20. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 21. Click 'Toggle'
    toggle = driver.find_element(By.XPATH,
                                 "//span[. = 'Toggle']")
    toggle.click()

    # 22. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 23. Click 'Toggle'
    toggle = driver.find_element(By.XPATH,
                                 "//span[. = 'Toggle']")
    toggle.click()

    # 24. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 25. Click 'Toggle Scrolling'
    toggle_scrolling = driver.find_element(By.XPATH,
                                           "//span[. = 'Toggle Scrolling']")
    toggle_scrolling.click()

    # 26. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 27. Click 'Clear'
    clear = driver.find_element(By.XPATH,
                                "//li[10]//a[. = 'Clear']")
    clear.click()

    # 28. Type 'Hello' in 'TEXTAREA4'
    textarea4 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea4.send_keys("Hello")

    # 29. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 30. Click 'Toggle'
    toggle = driver.find_element(By.XPATH,
                                 "//span[. = 'Toggle']")
    toggle.click()

    # 31. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 32. Click 'Toggle Scrolling'
    toggle_scrolling = driver.find_element(By.XPATH,
                                           "//span[. = 'Toggle Scrolling']")
    toggle_scrolling.click()

    # 33. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 34. Click 'Clear'
    clear = driver.find_element(By.XPATH,
                                "//li[10]//a[. = 'Clear']")
    clear.click()

    # 35. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 36. Click 'Run Cells'
    run_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Run Cells']")
    run_cells.click()

    # 37. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 38. Click 'Toggle'
    toggle = driver.find_element(By.XPATH,
                                 "//span[. = 'Toggle']")
    toggle.click()

    # 39. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 40. Click 'Toggle'
    toggle = driver.find_element(By.XPATH,
                                 "//span[. = 'Toggle']")
    toggle.click()

    # 41. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 42. Click 'Toggle Scrolling'
    toggle_scrolling = driver.find_element(By.XPATH,
                                           "//span[. = 'Toggle Scrolling']")
    toggle_scrolling.click()

    # 43. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 44. Click 'Clear'
    clear = driver.find_element(By.XPATH,
                                "//li[10]//a[. = 'Clear']")
    clear.click()
