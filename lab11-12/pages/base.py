from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class Web_Page:
    @staticmethod
    def get(driver, url):
        driver.get(url)

    @staticmethod
    def find_element_by_xpath(driver, xpath):
        Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return driver.find_element(By.XPATH, xpath)

    @staticmethod
    def find_elements_by_xpath(driver, xpath):
        return driver.find_elements(By.XPATH, xpath)

    @staticmethod
    def go_back(driver):
        driver.back()

    @staticmethod
    def refresh(driver):
        driver.refresh()

    @staticmethod
    def screenshot(driver, file_name='screenshot.png'):
        driver.save_screenshot(file_name)
