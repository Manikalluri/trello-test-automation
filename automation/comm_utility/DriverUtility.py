from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
current_drivers = {}

class DriverUtility:

    @staticmethod
    def initiate_firefox_driver(url):
        #driver_firefox = webdriver.Firefox(executable_path =r'C:\Users\kmanikanta\AppData\Local\Programs\Python\Python310\geckodriver.exe')
        driver_firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver_firefox.get(url)
        return driver_firefox
