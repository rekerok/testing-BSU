from pages.base import Web_Page


class Cart_Page(Web_Page):

    def __init__(self, webdriver, url="https://bagland.by/cart/"):
        super().__init__(webdriver, url)

    def get_names_items_in_cart(self):
        items = super().find_elements_by_xpath(
            "//div[@class='after_clear cart_product_wrap']//h1")
        return items

    def get_total_price(self):
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, "html")))
        price = super().find_element_by_xpath("//p[@class='total_pay']")
        return price.text
