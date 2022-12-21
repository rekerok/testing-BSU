import pytest

from pages.cart import Cart_Page
from pages.item import Item_Page


def test_delete_from_cart(driver, environment):
    Item_Page.add_item_to_cart(driver, environment["url_product"])
    Cart_Page.open_cart_page(driver)
    Cart_Page.delete_item_from_cart(driver)
    assert Cart_Page.cart_is_clear(driver)


@pytest.mark.parametrize("count,price", [(1, "155"), (3, "464"), (6, "927")])
def test_calculating_the_amount_for_the_quantity(driver, environment, count, price):
    Item_Page.add_item_to_cart(driver, environment["url_product"], count)
    assert Cart_Page.get_total_price_in_cart(driver) == price
