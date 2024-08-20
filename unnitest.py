import unittest
from unittest import TextTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
 
class TestStringMethods(unittest.TestCase):
 
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
        return
 
    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())
       
 
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
 
class TestMathMethods(unittest.TestCase):
 
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
 
    def test_subtraction(self):
        self.assertEqual(4 - 2, 2)
class TestLoginPage(unittest.TestCase):
    def setUp(self) -> None:
        
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver= webdriver.Chrome(options=options)
         
    def test_LoginPage(self):
        
        self.driver.get("https://www.facebook.com/login")
        time.sleep(10)
                 
        username=self.driver.find_element(By.ID,"email")
        username.send_keys('username')
        
        mypassword = self.driver.find_element(By.ID, "pass")
        mypassword.send_keys("password")
        mypassword.send_keys(Keys.RETURN)

        title1=self.driver.title
        title2="Ingia kwenye Facebook"

        self.assertEqual(title1, title2, "Mismatch")






        

 
if __name__ == '__main__':
    unittest.main()
   
    # suite = unittest.TestSuite()
    # suite.addTest(TestStringMethods())
    # suite.addTest(TestMathMethods())
    # suite.addTest((TestLoginPage()))

    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestStringMethods))
    # suite.addTest(unittest.makeSuite(TestMathMethods))
    # suite.addTest(unittest.makeSuite(TestLoginPage))
 
    # runner = TextTestRunner().run(suite)
    