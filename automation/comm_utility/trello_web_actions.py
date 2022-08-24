import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from automation.comm_utility.ConfigParser import WebAppConfigGlobal
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from automation.comm_utility.Logger import print_log


class TrelloWebApp():

    @staticmethod
    def login_as_user(driver, userid, password):
        driver.find_element_by_id("user").send_keys(userid)
        driver.find_element_by_id("login").click()
        time.sleep(5)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/button/span").click()
        time.sleep(5)
        driver.implicitly_wait(10)

    @staticmethod
    def press_enter_keyboard_button(driver):
        ActionChains(driver).key_down(Keys.ENTER).perform()
        print("Pressed Enter keyboard button ")
        time.sleep(2)

    @staticmethod
    def create_work_space(driver):
        print_log("clicking on create button")
        driver.find_element_by_xpath("//p[@class='uJFM1WfH-EGEiT']").click()
        driver.implicitly_wait(10)
        time.sleep(5)
        print_log("clicking on create workspace button")
        driver.find_element_by_xpath("/html/body/div[3]/div/section/div/nav/ul/li[3]/button/span[2]").click()
        driver.implicitly_wait(10)
        time.sleep(3)
        print_log("Sending workspace Name")
        driver.find_element_by_css_selector("body > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > input:nth-child(4)").send_keys("Test4")
        time.sleep(3)
        driver.implicitly_wait(5)
        print_log("Selecting Drop Down Menu")
        driver.find_element_by_css_selector(".css-191o3mb").click()
        driver.implicitly_wait(5)
        time.sleep(3)
        TrelloWebApp().press_enter_keyboard_button(driver)
        driver.implicitly_wait(5)
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.implicitly_wait(5)
        time.sleep(3)
        print_log("clicking dismiss icon")
        driver.find_element_by_xpath("//span[@class='nch-icon zb2xH7sIF-ak3S eF-AbDKCv1rLl4']//span[@aria-label='CloseIcon']").click()
        print_log("Workspace created Successfully")
        print_log("Navigating to Home Page")
        driver.get("https://trello.com/")
        time.sleep(5)




    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)