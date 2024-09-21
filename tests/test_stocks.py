import unittest
from pages.google_finance import GoogleFinancePage
from utils.setup_teardown import BaseTest


class TestStockSymbols(BaseTest):

    def test_stock_symbols(self):
        given_data = ["NFLX", "MSFT", "TSLA"]
        # Step 1: Open the page
        finance_page = GoogleFinancePage(self.driver)
        finance_page.load_page()

        # Step 2: Verify page title
        finance_page.verify_page_title()

        # Step 3: Retrieve stock symbols
        retrieved_symbols = finance_page.get_stock_symbols()

        # Step 4: Compare results
        missing_in_ui = list(set(given_data) - set(retrieved_symbols))
        missing_in_given = list(set(retrieved_symbols) - set(given_data))

        # Step 5 and 6: Print
        print("Stock symbols missing in UI but present in test data:", missing_in_ui)
        print("Stock symbols present in UI but missing in test data:", missing_in_given)


if __name__ == "__main__":
    unittest.main()
