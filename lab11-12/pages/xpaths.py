import enum


class Cart_Page_Xpaths(enum.Enum):
    XPATH_CHECKOUT_BUTTON = "//a[@class='green_button']"
    XPATH_TOTAL_PRICE = "//p[@class='total_pay']"
    XPATH_ELEMENTS = "//div[@class='after_clear cart_product_wrap']//h1"
    XPATH_COUNT_PRODUCT = "//input[@id='count']"
    XPATH_BUTTON_DELETE = "//a[@class='delete_product']"
    XPATH_CLEAR_TITLE = "//div[@class='container' and @id='content']//p[text()='В корзине пусто']"


class Item_Page_Xpaths(enum.Enum):
    XPATH_HEADER_COUNT = "//div[contains(@class, 'menu_cart')]//p[@class='good_snumber']"
    XPATH_BUTTON_TO_INCREASE_THE_NUMBER = "//span[@class='arrow-plus counter-button']"
    XPATH_BUTTON_ADD_TO_CARD = "//a[@id='cart_button']"
    XPATH_PRICE = "//p[text()=' бел. руб.']/span"


class Catalog_Page_Xpaths(enum.Enum):
    XPATH_ALL_PRODUCTS = "//p[@class='popular_title']"
