from pages import xpaths
from pages.base import Web_Page


class Cart_Page(Web_Page):

    def __init__(self, webdriver, url="https://bagland.by/cart/"):
        super().__init__(webdriver, url)

    def get_names_items_in_cart(self):
        items = super().find_elements_by_xpath(xpaths.cart.get("LIST_OF_PRODUCTS"))
        return items

    def get_total_price(self):
        price = super().find_element_by_xpath(xpaths.cart.get("TOTAL_PRICE"))
        return (price.text.split())[0]
