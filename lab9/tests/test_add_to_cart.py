from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


def test_add_to_card(driver):
    url = "https://bagland.by/katalog/kreslo-komfort/komfort-velvet/"
    driver.get(url)
    button_add_to_cart = driver.find_element(by=By.ID, value="cart_button")
    button_add_to_cart.click()
    wait_element = Wait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="top"]/div/div[2]/div/div/div[2]/nav/div[2]/a/p[1]'), "1 товар(ов)"))
