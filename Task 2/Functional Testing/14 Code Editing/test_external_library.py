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
    Package: TestProject.Generated.Tests.JupyterNotebookFunctionalTest
    Test: External Library
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 05/06/2021, 09:58:40
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="External Library")
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

    # 3. Click 'SPAN'
    span = driver.find_element(By.XPATH,
                               "//div/div/div/div/div[1]/div[1]/div[2]/div/div[1]/button/span[2]")
    span.click()

    # 4. Click 'Python 3'
    python_3 = driver.find_element(By.XPATH,
                                   "//a[. = 'Python 3']")
    python_3.click()

    # 5. Switch to window '1'
    driver.switch_to.window(driver.window_handles[1])

    # 6. Click 'Untitled6'
    untitled6 = driver.find_element(By.CSS_SELECTOR,
                                    "#notebook_name")
    untitled6.click()

    # 7. Type 'test_editor_07' in 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//input")
    input1.send_keys("test_editor_07")

    # 8. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 9. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[6]/div[1]/div/div")
    div2.click()

    # 10. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 11. Type 'import numpy as np' in 'TEXTAREA4'
    textarea4 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea4.send_keys("import numpy as np")

    # 12. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 13. Type '10' in 'TEXTAREA3'
    textarea3 = driver.find_element(By.XPATH,
                                    "//div[2]/div[1]/div[2]//textarea")
    textarea3.send_keys("10")

    # 14. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 15. Type '5' in 'TEXTAREA5'
    textarea5 = driver.find_element(By.XPATH,
                                    "//div[3]//textarea")
    textarea5.send_keys("5")

    # 16. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 17. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 18. Type '2' in 'TEXTAREA5'
    textarea5 = driver.find_element(By.XPATH,
                                    "//div[3]//textarea")
    textarea5.send_keys("2")

    # 19. Click 'DIV13'
    div13 = driver.find_element(By.XPATH,
                                "//div[4]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div")
    div13.click()
