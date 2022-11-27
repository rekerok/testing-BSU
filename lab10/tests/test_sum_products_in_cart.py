from pages.cart import Cart_Page
from pages.item import Item_Page


def test_add_to_card(driver):
    url_item_first = "https://bagland.by/katalog/kreslo-komfort/komfort-velvet/"
    url_item_second = "https://bagland.by/katalog/kreslo-mjach/ball-barcelona/"
    price_products = "286"
    item_page = Item_Page(driver, url_item_first)
    item_page.add_item_to_cart()
    item_page.get(url_item_second)
    item_page.add_item_to_cart()
    cart_page = Cart_Page(driver)
    result = cart_page.get_sum_price_in_cart()
    assert result == price_products