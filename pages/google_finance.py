from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleFinancePage:
    # Locator for the stock symbols
    STOCK_SYMBOLS_LOCATOR = (By.XPATH, "//div[@class='COaKTb']")

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.get("https://www.google.com/finance")

    def verify_page_title(self):
        """Verify the page title"""
        WebDriverWait(self.driver, 10).until(EC.title_contains("Google Finance"))

    def get_stock_symbols(self):
        """Retrieve stock symbols"""
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.STOCK_SYMBOLS_LOCATOR))
        elements = self.driver.find_elements(*self.STOCK_SYMBOLS_LOCATOR)
        return [element.text for element in elements]
