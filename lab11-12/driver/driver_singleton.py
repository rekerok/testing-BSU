from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Driver_Singleton:
    __webdriver = None

    @staticmethod
    def get_webdriver(browser):
        if not Driver_Singleton.__webdriver:
            if browser == "chrome":
                chrome_options = Options()
                # chrome_options.add_argument("--headless")
                chrome_options.add_argument("start-maximized")
                Driver_Singleton.__webdriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                                                options=chrome_options)
            elif browser == "firefox":
                Driver_Singleton.__webdriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return Driver_Singleton.__webdriver

    @staticmethod
    def quit():
        Driver_Singleton.__webdriver.quit()
        Driver_Singleton.__webdriver = None
