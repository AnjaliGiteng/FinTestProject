import unittest
from selenium import webdriver
from pages.google_finance import GoogleFinancePage


class GoogleFinanceTest(unittest.TestCase):
    def setUp(self):
        """Set up the WebDriver and initialize the Page Object."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.google_finance_page = GoogleFinancePage(self.driver)

    def test_compare_stock_symbols(self):
        """Test to compare stock symbols retrieved from the UI with the given test data."""
        # Given test data
        given_data = ["NFLX", "MSFT", "TSLA"]

        # Step 1: Load the Google Finance page
        self.google_finance_page.load_page()

        # Step 2: Verify the page is loaded
        self.google_finance_page.verify_page_loaded()

        # Step 3: Retrieve stock symbols from the UI
        retrieved_symbols = self.google_finance_page.get_stock_symbols()

        # Step 4: Compare and print results
        missing_in_ui = list(set(given_data) - set(retrieved_symbols))
        missing_in_given = list(set(retrieved_symbols) - set(given_data))

        # Step 5 and 6: Print
        print("Stock symbols missing in UI but present in test data:", missing_in_ui)
        print("Stock symbols present in UI but missing in test data:", missing_in_given)

    def tearDown(self):
        """Tear down the WebDriver."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
