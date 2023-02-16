import time

from pages.base import Web_Page
from pages.xpaths import Item_Page_Xpaths
from utils.waits import Waits


class Item_Page:
    @staticmethod
    def get_count_in_header(driver):
        count = Web_Page.find_element_by_xpath(driver, Item_Page_Xpaths.XPATH_HEADER_COUNT.value)
        count = int(count.text.split(" ")[0])
        return count

    @staticmethod
    def add_item_to_cart(driver, url, count=1):
        Web_Page.get(driver, url)
        if count > 1:
            for i in range(count - 1):
                Waits.element_to_be_clickable(driver, Item_Page_Xpaths.XPATH_BUTTON_TO_INCREASE_THE_NUMBER.value)
                Web_Page.find_element_by_xpath(driver,
                                               Item_Page_Xpaths.XPATH_BUTTON_TO_INCREASE_THE_NUMBER.value).click()
        Waits.element_to_be_clickable(driver, Item_Page_Xpaths.XPATH_BUTTON_ADD_TO_CARD.value)
        add_to_card_button = Web_Page.find_element_by_xpath(driver, Item_Page_Xpaths.XPATH_BUTTON_ADD_TO_CARD.value)
        add_to_card_button.click()

    @staticmethod
    def set_size_product(driver, url, size="s_size"):
        Web_Page.get(driver, url)
        XPATH_INPUT_COUNT = f"//div[contains(@class, '{size}')]"
        size = Web_Page.find_element_by_xpath(driver, XPATH_INPUT_COUNT)
        size.click()

    @staticmethod
    def get_price_item(driver):
        time.sleep(1.5)
        return Web_Page.find_element_by_xpath(driver, Item_Page_Xpaths.XPATH_PRICE.value).text
