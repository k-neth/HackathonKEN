import unittest
from selenium import webdriver

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        
    def test_login_page_title(self):
        self.driver.get("https://www.facebook.com/login")
        title1 = self.driver.title
        title2 = "Ingia kwenye Facebook"
        self.assertEqual(title1, title2, "Title does not match the expected value")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
