import time

from pages.base import Web_Page


class Item_Page:
    @staticmethod
    def add_item_to_cart(driver, url, count=1):
        if driver.current_url != url:
            Web_Page.get(driver, url)
        if count > 1:
            XPATH_BUTTON_TO_INCREASE_THE_NUMBER = "//span[@class='arrow-plus counter-button']"
            for i in range(count - 1):
                # Wait(driver, 10).until(EC.element_to_be_selected((By.XPATH, "//a[@id='cart_button']")))
                Web_Page.find_element_by_xpath(driver, XPATH_BUTTON_TO_INCREASE_THE_NUMBER).click()
        add_to_card_button = Web_Page.find_element_by_xpath(driver, "//a[@id='cart_button']")
        add_to_card_button.click()

    @staticmethod
    def set_size_product(driver, url, size="s_size"):
        Web_Page.get(driver, url)
        XPATH_INPUT_COUNT = f"//div[contains(@class, '{size}')]"
        size = Web_Page.find_element_by_xpath(driver, XPATH_INPUT_COUNT)
        size.click()

    @staticmethod
    def get_price_item(driver):
        XPATH_PRICE = "//p[text()=' бел. руб.']/span"
        time.sleep(1.5)
        return Web_Page.find_element_by_xpath(driver, XPATH_PRICE).text
