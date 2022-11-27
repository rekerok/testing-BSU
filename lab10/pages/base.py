import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class Web_Page:
    _web_driver = None

    def __init__(self, web_driver: webdriver, url=''):
        self._web_driver = web_driver
        self.get(url)

    def get(self, url):
        self._web_driver.get(url)

    def find_element_by_xpath(self, xpath):
        Wait(self._web_driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return self._web_driver.find_element(By.XPATH, xpath)

    def find_elements_by_xpath(self, xpath):
        return self._web_driver.find_elements(By.XPATH, xpath)

    def open_cart(self):
        self.get("https://bagland.by/cart/")
        time.sleep(5)

    def go_back(self):
        self._web_driver.back()



    def refresh(self):
        self._web_driver.refresh()

    def screenshot(self, file_name='screenshot.png'):
        self._web_driver.save_screenshot(file_name)

    def get_sum_price_in_cart(self):
        price = self.find_element_by_xpath(
            "//nav[@class='menu_top navbar navbar-default']//p[@class='cart_price']").text
        return price.split()[0]
