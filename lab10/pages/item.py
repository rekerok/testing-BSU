from pages.base import Web_Page
from pages import xpaths


class Item_Page(Web_Page):

    def __init__(self, webdriver, url):
        super().__init__(webdriver, url)

    def add_item_to_cart(self):
        add_to_card_button = super().find_element_by_xpath(xpaths.item.get("ADD_TO_CART"))
        add_to_card_button.click()
