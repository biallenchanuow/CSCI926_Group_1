from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Jupyter Notebook Functional Test
    Package: CellMenuCellType
    Test: Cell Menu - Cell Type
    Generated by: Jianpeng Chen (jc107@uowmail.edu.au)
    Generated on 05/05/2021, 11:26:34
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="fk3yOvlRsLLpCaaggFfMO8vEplPSx8qsdrnNiqcDOgM",
                              project_name="Jupyter Notebook Functional Test",
                              job_name="Cell Menu - Cell Type")
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

    # 6. Click 'Code'
    code = driver.find_element(By.XPATH,
                               "//span[. = 'Code']")
    code.click()

    # 7. Type 'Hello World' in 'TEXTAREA4'
    textarea4 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea4.send_keys("Hello World")

    # 8. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 9. Click 'Run Cells'
    run_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Run Cells']")
    run_cells.click()

    # 10. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 11. Click 'Run Cells'
    run_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Run Cells']")
    run_cells.click()

    # 12. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 13. Click 'Delete CellsD,D'
    delete_cellsd_d = driver.find_element(By.XPATH,
                                          "//a[. = 'Delete CellsD,D']")
    delete_cellsd_d.click()

    # 14. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 15. Click 'Markdown'
    markdown = driver.find_element(By.XPATH,
                                   "//span[. = 'Markdown']")
    markdown.click()

    # 16. Click '​6'
    _6 = driver.find_element(By.XPATH,
                             "//pre[. = '​']")
    _6.click()

    # 17. Type '")' in 'TEXTAREA7'
    textarea7 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea7.send_keys("\")")

    # 18. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 19. Click 'Run Cells'
    run_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Run Cells']")
    run_cells.click()

    # 20. Click 'I5'
    i5 = driver.find_element(By.XPATH,
                             "//div[2]/button/i")
    i5.click()

    # 21. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 22. Click 'Markdown'
    markdown = driver.find_element(By.XPATH,
                                   "//span[. = 'Markdown']")
    markdown.click()

    # 23. Click '​1'
    _1 = driver.find_element(By.XPATH,
                             "//pre[. = '​']")
    _1.click()

    # 24. Type 'print(int("Hello))' in 'TEXTAREA8'
    textarea8 = driver.find_element(By.XPATH,
                                    "//div[2]/div[2]/div[2]//textarea")
    textarea8.send_keys("print(int(\"Hello))")

    # 25. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 26. Click 'Run Cells'
    run_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Run Cells']")
    run_cells.click()

    # 27. Click 'print("Hello World")2'
    print_double_quote_hello_world_double_quote_2 = driver.find_element(By.XPATH,
                                                                        "//p[. = 'print(\"Hello World\")']")
    print_double_quote_hello_world_double_quote_2.click()

    # 28. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 29. Click 'Delete CellsD,D'
    delete_cellsd_d = driver.find_element(By.XPATH,
                                          "//a[. = 'Delete CellsD,D']")
    delete_cellsd_d.click()

    # 30. Click 'Edit1'
    edit1 = driver.find_element(By.CSS_SELECTOR,
                                "#editlink")
    edit1.click()

    # 31. Click 'Delete Cells'
    delete_cells = driver.find_element(By.XPATH,
                                       "//span[. = 'Delete Cells']")
    delete_cells.click()

    # 32. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 33. Click 'Raw NBConvert'
    raw_nbconvert = driver.find_element(By.XPATH,
                                        "//span[. = 'Raw NBConvert']")
    raw_nbconvert.click()

    # 34. Click '​6'
    _6 = driver.find_element(By.XPATH,
                             "//pre[. = '​']")
    _6.click()

    # 35. Type 'o World")' in 'TEXTAREA7'
    textarea7 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea7.send_keys("o World\")")

    # 36. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 37. Click 'Run Cells'
    run_cells = driver.find_element(By.XPATH,
                                    "//span[. = 'Run Cells']")
    run_cells.click()

    # 38. Click 'print("Hello World")3'
    print_double_quote_hello_world_double_quote_3 = driver.find_element(By.XPATH,
                                                                        "//span[. = 'print(\"Hello World\")']")
    print_double_quote_hello_world_double_quote_3.click()

    # 39. Click 'print(int("Hello")'
    print_int_double_quote_hello_double_quote_ = driver.find_element(By.XPATH,
                                                                     "//pre[. = 'print(int(\"Hello\")']")
    print_int_double_quote_hello_double_quote_.click()

    # 40. Type ')' in 'TEXTAREA7'
    textarea7 = driver.find_element(By.XPATH,
                                    "//textarea")
    textarea7.send_keys(")")

    # 41. Click 'Cell'
    cell = driver.find_element(By.CSS_SELECTOR,
                               "#celllink")
    cell.click()

    # 42. Click 'Run Cells⌃↩'
    run_cells_ = driver.find_element(By.XPATH,
                                     "//a[. = 'Run Cells⌃↩']")
    run_cells_.click()