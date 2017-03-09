import unittest
from selenium import webdriver
from config_loader.ConfigLoader import ConfigLoader


class ExampleTest(unittest.TestCase):

    def setUp(self):
        self.config = ConfigLoader()
        self.webdriver = webdriver.Firefox()

    def tearDown(self):
        self.webdriver.quit()

    def testSomething(self):
        self.webdriver.get('https://www.google.com')

