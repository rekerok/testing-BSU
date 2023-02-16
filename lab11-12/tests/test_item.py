import pytest

from model.item import Item
from pages.cart import Cart_Page
from pages.item import Item_Page


def test_add_to_card(driver, environment):
    item = Item(environment["name_product"], environment["price_product"])
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    assert Cart_Page.check_item_in_cart(driver, item.get_name())


@pytest.mark.skip(reason="Не придумал как реализовать ожидание")
def test_multi_product(driver, environment):
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    result = Cart_Page.get_count_item_in_cart(driver)
    assert result == 2


@pytest.mark.parametrize("size,price", [("s_size", "157"), ("m_size", "192"), ("l_size", "259")])
def test_counter_new_price_for_size(driver, environment, size, price):
    Item_Page.set_size_product(driver, environment["url_product"], size)
    assert Item_Page.get_price_item(driver) == price
