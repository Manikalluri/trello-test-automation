import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")
import unittest
import time
from automation.comm_utility.DriverUtility import DriverUtility
from automation.comm_utility.ResultReporter import Gen5BaseTestCase
from automation.comm_utility.Logger import print_log
from automation.comm_utility.trello_web_actions import TrelloWebApp
from automation.comm_utility.Constants import *
from automation.comm_utility.ConfigParser import WebAppConfigGlobal, TRUE, FALSE
from automation.verification.trello_homepage import WelcomeTrello


class TestTrello(Gen5BaseTestCase):
    def setUp(self):
        super().setUp()
        global webconsole_driver
        webconsole_driver = DriverUtility.initiate_firefox_driver(WebAppConfigGlobal.WebUrl)
        print_log("Logging into trello")
        TrelloWebApp.login_as_user(webconsole_driver, WebAppConfigGlobal.WebLoginName, WebAppConfigGlobal.WebloginPassword)
        webconsole_driver.implicitly_wait(5)
        time.sleep(3)
    def tearDown(self):
        super().tearDown()
        webconsole_driver.quit()

    def test1_verify_login(self):
        '''Test Case 1:  '''
        """ This method performs Test Case to Verify Trello Home page after login"""

        try:
            count = 0
            print_log("\n")
            if WelcomeTrello().verify_trello_home_label(webconsole_driver):
                print_log("Home Label after login is present")
                count = count + 1
            else:
                print_log("!!!!Home Label is not displayed")

            if count == 1:
                self.verify(TRUE, "Home Lable After Login verified")
            else:
                self.verify(FALSE, "Home Label not verified properly")

        finally:
            print_log("Entered finally")
            time.sleep(3)
    def test2_verify_workspace_creation(self):
        '''Test Case 2:  '''
        """ This test case is to verify the workspace creation"""
        try:
            count = 0
            print_log("\n")
            TrelloWebApp().create_work_space(webconsole_driver)
            if WelcomeTrello().verify_trello_work_space(webconsole_driver):
                print_log("Workspace created successfully")
                count = count + 1
            else:
                print_log("!!!!workspace not created")

            if count == 1:
                self.verify(TRUE, "Workspace creation successfully verified")
            else:
                self.verify(FALSE, "Workspace creation not verified properly")

        finally:
            print_log("Entered finally")
            time.sleep(3)




def main():
    TestCases = [
        'test1_verify_login',
        'test2_verify_workspace_creation'

    ]
    GlobalVar.Suite = unittest.TestSuite(map(TestTrello, TestCases))
    unittest.TextTestRunner(verbosity=2).run(GlobalVar.Suite)



if __name__ == '__main__':
    main()
    print("Completed")