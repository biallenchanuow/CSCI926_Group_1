from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Jupyter Notebook Functional Test
    Package: InsertMenu
    Test: Insert Menu
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 05/01/2021, 02:02:39
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="Insert Menu")
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

    # 2. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 3. Click 'functional test folder'
    functional_test_folder = driver.find_element(By.XPATH,
                                                 "//span[. = 'functional test folder']")
    functional_test_folder.click()

    # 4. Click 'New
    #
    #               ...'
    new_ = driver.find_element(By.CSS_SELECTOR,
                               "#new-dropdown-button")
    new_.click()

    # 5. Click 'Python 3'
    python_3 = driver.find_element(By.XPATH,
                                   "//a[. = 'Python 3']")
    python_3.click()

    # 6. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 7. Click 'Insert'
    insert = driver.find_element(By.CSS_SELECTOR,
                                 "#insertlink")
    insert.click()

    # 8. Click 'Insert Cell Above'
    insert_cell_above = driver.find_element(By.XPATH,
                                            "//span[. = 'Insert Cell Above']")
    insert_cell_above.click()

    # 9. Click 'Insert'
    insert = driver.find_element(By.CSS_SELECTOR,
                                 "#insertlink")
    insert.click()

    # 10. Click 'Insert Cell Below1'
    insert_cell_below1 = driver.find_element(By.XPATH,
                                             "//span[. = 'Insert Cell Below']")
    insert_cell_below1.click()

    # 11. Click 'Insert'
    insert = driver.find_element(By.CSS_SELECTOR,
                                 "#insertlink")
    insert.click()

    # 12. Click 'Insert Cell Above'
    insert_cell_above = driver.find_element(By.XPATH,
                                            "//span[. = 'Insert Cell Above']")
    insert_cell_above.click()

    # 13. Click '​4'
    _4 = driver.find_element(By.XPATH,
                             "//div[1]/div[1]/div[2]/div[2]//pre[. = '​']")
    _4.click()

    # 14. Click 'Insert'
    insert = driver.find_element(By.CSS_SELECTOR,
                                 "#insertlink")
    insert.click()

    # 15. Click 'Insert Cell Below1'
    insert_cell_below1 = driver.find_element(By.XPATH,
                                             "//span[. = 'Insert Cell Below']")
    insert_cell_below1.click()