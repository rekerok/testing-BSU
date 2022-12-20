import pytest

from pages.item import Item_Page


@pytest.mark.parametrize("size,price", [("s_size", "155"), ("m_size", "189"), ("l_size", "255")])
def test_counter_new_price_for_size(driver, environment, size, price):
    Item_Page.set_size_product(driver, environment["url_product"], size)
    assert Item_Page.get_price_item(driver) == price
