from selenium.common import NoSuchElementException

from pages.base import Web_Page
from pages.xpaths import Cart_Page_Xpaths
from utils.waits import Waits


class Cart_Page:
    url = "https://bagland.by/cart/"

    @staticmethod
    def get_total_price_in_cart(driver):
        if driver.current_url != Cart_Page.url:
            Web_Page.get(driver, Cart_Page.url)
        price = Web_Page.find_element_by_xpath(driver, Cart_Page_Xpaths.XPATH_TOTAL_PRICE.value).text
        return price.split(" ")[0]

    @staticmethod
    def open_cart_page(driver):
        driver.get(Cart_Page.url)

    @staticmethod
    def get_names_items_in_cart(driver):
        if driver.current_url != Cart_Page.url:
            Web_Page.get(driver, Cart_Page.url)
        Waits.visibility_of_element_located(driver, Cart_Page_Xpaths.XPATH_CHECKOUT_BUTTON.value)
        items = Web_Page.find_elements_by_xpath(driver, Cart_Page_Xpaths.XPATH_ELEMENTS.value)
        print(items)
        return items

    @staticmethod
    def check_item_in_cart(driver, name):
        if driver.current_url != Cart_Page.url:
            Web_Page.get(driver, Cart_Page.url)
        all_items = Cart_Page.get_names_items_in_cart(driver)
        all_items = list(map(lambda x: x.text, all_items))
        return True if name in all_items else False

    @staticmethod
    def get_count_item_in_cart(driver):
        if driver.current_url != Cart_Page.url:
            Web_Page.get(driver, Cart_Page.url)
        count_of_products = 0
        if Cart_Page.cart_is_clear(driver):
            return count_of_products
        else:
            Waits.element_to_be_clickable(driver, Cart_Page_Xpaths.XPATH_COUNT_PRODUCT.value)
            return int(Web_Page.find_element_by_xpath(driver, Cart_Page_Xpaths.XPATH_COUNT_PRODUCT.value).get_attribute(
                "value"))

    @staticmethod
    def delete_item_from_cart(driver):
        if driver.current_url != Cart_Page.url:
            Web_Page.get(driver, Cart_Page.url)
        else:
            Web_Page.get(driver, Cart_Page.url)
        button_delete = Web_Page.find_element_by_xpath(driver, Cart_Page_Xpaths.XPATH_BUTTON_DELETE.value)
        button_delete.click()

    @staticmethod
    def cart_is_clear(driver):
        if driver.current_url != Cart_Page.url:
            Web_Page.get(driver, Cart_Page.url)
        try:
            Waits.visibility_of_element_located(driver, Cart_Page_Xpaths.XPATH_CLEAR_TITLE.value)
            return True
        except NoSuchElementException:
            return False
