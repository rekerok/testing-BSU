from pages.catalog import Catalog


def test_get_all_product_on_page(driver, environment):
    products = ['КОМФОРТ',
                'КОМФОРТ СЕТ',
                'КОМФОРТ БАРХАТ',
                'КОМФОРТ АПЕЛЬСИН',
                'КОМФОРТ АУТА',
                'КОМФОРТ ФОРТЕ',
                'КОМФОРТ КЛАССИК',
                'КОМФОРТ ПЛУТОН',
                'КОМФОРТ БЕЛЫЙ',
                'КОМФОРТ РЫЖИЙ',
                'КОМФОРТ КРАСНЫЙ',
                'КОМФОРТ РОМБИК'].sort()
    assert products == Catalog.get_all_product_on_page(driver, environment['url_catalog']).sort()
