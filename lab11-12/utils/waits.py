from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class Waits:
    wait_time = 10

    @staticmethod
    def visibility_of_element_located(driver, xpath):
        Wait(driver, Waits.wait_time).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))

    @staticmethod
    def element_to_be_clickable(driver, xpath):
        Wait(driver, Waits.wait_time).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))

    @staticmethod
    def text_to_be_present_in_element(driver, xpath, text):
        Wait(driver, Waits.wait_time).until(
            EC.text_to_be_present_in_element((By.XPATH, xpath), text))
