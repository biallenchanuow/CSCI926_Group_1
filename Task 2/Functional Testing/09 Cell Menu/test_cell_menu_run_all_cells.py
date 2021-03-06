from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Jupyter Notebook Functional Test
    Package: CellMenuRunAllCells
    Test: Cell Menu - Run All Cells
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 05/01/2021, 02:03:59
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="Cell Menu - Run All Cells")
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

    # 6. Click 'Run All'
    run_all = driver.find_element(By.XPATH,
                                  "//a[. = 'Run All']")
    run_all.click()

    # 7. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[6]/div[1]/div/div")
    div2.click()

    # 8. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 9. Click 'Run All'
    run_all = driver.find_element(By.XPATH,
                                  "//a[. = 'Run All']")
    run_all.click()

    # 10. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[6]/div[1]/div/div")
    div2.click()

    # 11. Type 'Hello' in 'TEXTAREA4'
    textarea4 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea4.send_keys("Hello")

    # 12. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 13. Click 'Run All'
    run_all = driver.find_element(By.XPATH,
                                  "//a[. = 'Run All']")
    run_all.click()

    # 14. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 15. Click 'Delete Cells'
    delete_cells = driver.find_element(By.XPATH,
                                       "//span[. = 'Delete Cells']")
    delete_cells.click()

    # 16. Type 'Hello World' in 'TEXTAREA4'
    textarea4 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea4.send_keys("Hello World")

    # 17. Click 'I5'
    i5 = driver.find_element(By.XPATH,
                             "//div[2]/button/i")
    i5.click()

    # 18. Click 'DIV3'
    div3 = driver.find_element(By.XPATH,
                               "//div[2]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div")
    div3.click()

    # 19. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 20. Click 'Run All'
    run_all = driver.find_element(By.XPATH,
                                  "//a[. = 'Run All']")
    run_all.click()

    # 21. Type ')' in 'TEXTAREA2'
    textarea2 = driver.find_element(By.XPATH,
                                    "//div[1]/div[1]/div[2]/div[2]//textarea")
    textarea2.send_keys(")")

    # 22. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 23. Click 'Run All'
    run_all = driver.find_element(By.XPATH,
                                  "//a[. = 'Run All']")
    run_all.click()

    # 24. Type ' World' in 'TEXTAREA2'
    textarea2 = driver.find_element(By.XPATH,
                                    "//div[1]/div[1]/div[2]/div[2]//textarea")
    textarea2.send_keys(" World")

    # 25. Click 'PRE2'
    pre2 = driver.find_element(By.XPATH,
                               "//div[3]/pre")
    pre2.click()

    # 26. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 27. Click 'Run All'
    run_all = driver.find_element(By.XPATH,
                                  "//a[. = 'Run All']")
    run_all.click()

    # 28. Type ')' in 'TEXTAREA2'
    textarea2 = driver.find_element(By.XPATH,
                                    "//div[1]/div[1]/div[2]/div[2]//textarea")
    textarea2.send_keys(")")

    # 29. Type '123)' in 'TEXTAREA3'
    textarea3 = driver.find_element(By.XPATH,
                                    "//div[2]/div[1]/div[2]//textarea")
    textarea3.send_keys("123)")

    # 30. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 31. Click 'Run All'
    run_all = driver.find_element(By.XPATH,
                                  "//a[. = 'Run All']")
    run_all.click()
