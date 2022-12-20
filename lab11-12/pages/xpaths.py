import enum


class Cart_Page_Xpaths(enum.Enum):
    XPATH_CHECKOU_BUTTON = "//a[@class='green_button']"
    XPATH_TOTAL_PRICE = "//p[@class='total_pay']"
    XPATH_ELEMENTS = "//div[@class='after_clear cart_product_wrap']//h1"
    XPATH_COUNT_PRODUCT = "//input[@id='count']"
    XPATH_BUTTON_DELETE = "//a[@class='delete_product']"
    XPATH_CLEAR_TITLE = "//div[@class='container' and @id='content']//p[text()='В корзине пусто']"
