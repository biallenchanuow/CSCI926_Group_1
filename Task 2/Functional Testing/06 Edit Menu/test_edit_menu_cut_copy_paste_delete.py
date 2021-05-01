from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Jupyter Notebook Functional Test
    Package: EditMenuCutCopyPasteDelete
    Test: Edit Menu - Cut Copy Paste Delete
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 04/27/2021, 06:37:16
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="Edit Menu - Cut Copy Paste Delete")
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

    # 6. Click 'Cut Cells'
    cut_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Cut Cells']")
    cut_cells.click()

    # 7. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 8. Click 'Paste Cells Above'
    paste_cells_above = driver.find_element(By.XPATH,
                                            "//span[. = 'Paste Cells Above']")
    paste_cells_above.click()

    # 9. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 10. Click 'Paste Cells Below'
    paste_cells_below = driver.find_element(By.XPATH,
                                            "//span[. = 'Paste Cells Below']")
    paste_cells_below.click()

    # 11. Click 'DIV4'
    div4 = driver.find_element(By.XPATH,
                               "//div[1]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div")
    div4.click()

    # 12. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 13. Click 'Cut CellsX'
    cut_cellsx = driver.find_element(By.XPATH,
                                     "//a[. = 'Cut CellsX']")
    cut_cellsx.click()

    # 14. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 15. Click 'Paste Cells & Replace'
    paste_cells_replace = driver.find_element(By.XPATH,
                                              "//a[. = 'Paste Cells & Replace']")
    paste_cells_replace.click()

    # 16. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 17. Click 'Cut CellsX'
    cut_cellsx = driver.find_element(By.XPATH,
                                     "//a[. = 'Cut CellsX']")
    cut_cellsx.click()

    # 18. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 19. Click 'Paste Cells & Replace'
    paste_cells_replace = driver.find_element(By.XPATH,
                                              "//a[. = 'Paste Cells & Replace']")
    paste_cells_replace.click()

    # 20. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 21. Click 'Copy Cells'
    copy_cells = driver.find_element(By.XPATH,
                                     "//span[. = 'Copy Cells']")
    copy_cells.click()

    # 22. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 23. Click 'Paste Cells Above'
    paste_cells_above = driver.find_element(By.XPATH,
                                            "//span[. = 'Paste Cells Above']")
    paste_cells_above.click()

    # 24. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 25. Click 'Paste Cells Below'
    paste_cells_below = driver.find_element(By.XPATH,
                                            "//span[. = 'Paste Cells Below']")
    paste_cells_below.click()