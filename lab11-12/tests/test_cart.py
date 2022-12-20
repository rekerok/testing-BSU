import pytest

from model.item import Item
from pages.cart import Cart_Page
from pages.item import Item_Page


def test_add_to_card(driver, environment):
    item = Item(environment["name_product"], environment["price_product"])
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    assert Cart_Page.check_item_in_cart(driver, item.get_name())


def test_delete_from_cart(driver, environment):
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    Cart_Page.open_cart_page(driver)
    Cart_Page.delete_item_from_cart(driver)
    assert Cart_Page.cart_is_clear(driver)


def test_multi_product(driver, environment):
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    assert Cart_Page.get_count_item_in_cart(driver) == 2


@pytest.mark.parametrize("count,price", [(1, "155"),(3, "464"), (6, "927")])
def test_calculating_the_amount_for_the_quantity(driver, environment, count, price):
    Item_Page.add_item_to_cart(driver, environment["url_product"], count)
    assert Cart_Page.get_total_price_in_cart(driver) == price
