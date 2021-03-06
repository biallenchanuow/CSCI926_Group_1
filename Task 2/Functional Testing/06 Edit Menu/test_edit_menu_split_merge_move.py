from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Jupyter Notebook Functional Test
    Package: EditMenuSplitMergeMove
    Test: Edit Menu - Split Merge Move
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 04/27/2021, 06:37:58
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="Edit Menu - Split Merge Move")
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

    # 3. Click 'test_editor_01.ipynb1'
    test_editor_01_ipynb1 = driver.find_element(By.XPATH,
                                                "//span[. = 'test_editor_01.ipynb']")
    test_editor_01_ipynb1.click()

    # 4. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 5. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 6. Click 'Split Cell'
    split_cell = driver.find_element(By.XPATH,
                                     "//span[. = 'Split Cell']")
    split_cell.click()
