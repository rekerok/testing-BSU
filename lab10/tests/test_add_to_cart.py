from pages.cart import Cart_Page
from pages.item import Item_Page


def test_add_to_card(driver):
    url_item = "https://bagland.by/katalog/kreslo-komfort/komfort-velvet/"
    name_item = "КОМФОРТ БАРХАТ"
    item_page = Item_Page(driver, url_item)
    item_page.add_item_to_cart()
    cart_page = Cart_Page(driver)
    result = cart_page.get_names_items_in_cart()[0].text
    assert result == name_item
