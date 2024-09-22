import unittest
from pages.google_finance import GoogleFinancePage
from utils.setup_teardown import BaseTest


class TestStockSymbols(BaseTest):

    def setUp(self):
        super().setUp()
        self.finance_page = GoogleFinancePage(self.driver)
        self.finance_page.load_page()
        self.given_data = ["NFLX", "MSFT", "TSLA"]

    def test_stock_symbols(self):
        """Full test case to compare all symbols."""
        # Step 2: Verify page title
        self.finance_page.verify_page_title()

        # Step 3: Retrieve stock symbols
        retrieved_symbols = self.finance_page.get_stock_symbols()

        # Step 4: Compare results
        missing_in_given = list(set(retrieved_symbols) - set(self.given_data))
        missing_in_ui = list(set(self.given_data) - set(retrieved_symbols))

        # Step 5 and 6: Print
        print("Stock symbols present in UI but missing in given test data:", missing_in_given)
        print("Stock symbols missing in UI but present in given test data:", missing_in_ui)

    def test_case_5(self):
        """Test case 5: Print symbols in UI but missing in given test data."""
        self.assertIn("Google Finance", self.driver.title)
        retrieved_symbols = self.finance_page.get_stock_symbols()

        missing_in_given = list(set(retrieved_symbols) - set(self.given_data))
        print("Stock symbols present in UI but missing in given test data:", missing_in_given)

    def test_case_6(self):
        """Test case 6: Print symbols in given test data but missing in UI."""
        self.assertIn("Google Finance", self.driver.title)
        retrieved_symbols = self.finance_page.get_stock_symbols()

        missing_in_ui = list(set(self.given_data) - set(retrieved_symbols))
        print("Stock symbols missing in UI but present in given test data:", missing_in_ui)


if __name__ == "__main__":
    unittest.main()
