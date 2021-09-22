import unittest
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        url = "http://www.python.org/"
        driver.get(url)
        self.assertIn("Python", driver.title)
        element = driver.find_element_by_name("q")
        element.clear()
        element.send_keys("pycon")
        element.send_keys(Keys.RETURN)
        assert "No results were found." not in driver.page_source
    Keys.sed
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
