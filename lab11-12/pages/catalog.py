from pages.base import Web_Page
from pages.xpaths import Catalog_Page_Xpaths


class Catalog:
    @staticmethod
    def get_all_product_on_page(driver, url):
        if driver.current_url != url:
            Web_Page.get(driver, url)
        products = Web_Page.find_elements_by_xpath(driver, Catalog_Page_Xpaths.XPATH_ALL_PRODUCTS.value)
        return list(map(lambda x: x.text, products))
