from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
