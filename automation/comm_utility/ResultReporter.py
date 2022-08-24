import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")
import time
import datetime as dt
import unittest
from automation.comm_utility.ConfigParser import PASS, TRUE
from automation.comm_utility.Logger import *
from automation.comm_utility.Constants import DEFAULT_RESULT_FOLDER


def get_script_name():
    """ returns the script name"""

    # returns the script name
    return os.path.split(sys.argv[0])[1]


def generate_resultfile():
    """This method generates unique result file name"""

    # This returns script name appends with time
    temp = dt.datetime.now()

    return DEFAULT_RESULT_FOLDER + "/" + get_script_name() + "_" + temp.strftime("%Y_%m_%d_%H_%M") + ".txt"


def  initiate_script_enter():
    """ This function would be initiated script enter and gather all the system info """

    # Initialize the Script name
    GlobalVar.scriptname = get_script_name()

    # Initialize the Script Phase
    GlobalVar.runPhase = "Script Enter"

    # Initialize the Resultfile
    GlobalVar.resultfile = generate_resultfile()

    # Initialize the user name
    GlobalVar.StartTime = time.strftime("%Y-%m-%d %H:%M")




class Gen5BaseTestCase(unittest.TestCase):

    def setUp(self):
        print("Test Case Setup")
        # Print The Total Number testcase before execution of first testcase
        if (GlobalVar.TillRunningStatus == {}):
            GlobalVar.TotalNumberOfTCS = GlobalVar.Suite.countTestCases()
            print_res(GlobalVar.resultfile, "######################################################")
            print_res(GlobalVar.resultfile,
                      "### Total Number Of TestCases:" + str(GlobalVar.TotalNumberOfTCS) + "                    ###")
            print_res(GlobalVar.resultfile, "###################################################### \n\n")

        # Initialize the run state         
        GlobalVar.tcRunStatus = None
        GlobalVar.tcVerifyCountinueRunList = []

        # Initialize the testcase Name and enter to testcase enter State
        GlobalVar.testcasename = unittest.TestCase.id(self).replace("__main__.", "", 1)

        # Print the testcase name in the 
        tname = "TESTCASE NAME:" + str(GlobalVar.testcasename) + "\n\n"
        print_res(GlobalVar.resultfile, tname)

    def tearDown(self):
        print("Teardown")
        # Print the testcase passed or failed
        if (len(GlobalVar.tcVerifyCountinueRunList) != 0):
            if (GlobalVar.tcVerifyCountinueRunList.count("FAILED") > 0):
                GlobalVar.tcRunStatus = "FAILED"

        if (sys.exc_info()[0] != None):
            GlobalVar.tcRunStatus = "FAILED"
            tmpMessage = "FAILED  :  Error***" + str(sys.exc_type) + "***"
            print_res(GlobalVar.resultfile, tmpMessage)
            sys.exc_clear()

        res = "|||| TEST CASE RESULT : " + str(GlobalVar.tcRunStatus) + ""
        print_res(GlobalVar.resultfile,
                  "==============================================================================")
        print_res(GlobalVar.resultfile, res)
        print_res(GlobalVar.resultfile,
                  "==============================================================================")
        print_res(GlobalVar.resultfile, "\n")

        # Track for Summary Run 
        GlobalVar.TillRunningStatus[str(GlobalVar.testcasename)] = str(GlobalVar.tcRunStatus)

    @classmethod
    def get_script_name(self):
        """ returns the script name"""

        # returns the script name
        return os.path.split(sys.argv[0])[1]

    @classmethod
    def generate_resultfile(self):
        """This method generates unique result file name"""

        # This returns script name appends with time
        temp = dt.datetime.now()

        return DEFAULT_LOG_FOLDER + "/" + self.get_script_name() + "_" + temp.strftime("%Y_%m_%d_%H_%M") + ".txt"
        # return self.get_script_name() +"_"+ temp.strftime("%Y_%m_%d_%H_%M")+".txt"

    @classmethod
    def get_current_user(self):
        """ This returns the current user """
        user = os.getenv('USER')
        if user == None:
            user = "User"
        return user

    @classmethod
    def setUpClass(self):
        print("Setting up")
        # Initialize the Script name
        GlobalVar.scriptname = self.get_script_name()

        # Initialize the Script Phase
        GlobalVar.runPhase = "Script Enter"

        # Initialize the Resultfile
        GlobalVar.resultfile = self.generate_resultfile()
        print("###############")
        print(GlobalVar.resultfile)

        # Initialize the user name
        GlobalVar.User = self.get_current_user()
        GlobalVar.StartTime = time.strftime("%Y-%m-%d %H:%M")

        Res_Headings = Gen5Logger()

        # Print the system and script info
        # Res_Headings.ScriptInfo(GlobalVar.Machinename,GlobalVar.scriptname,GlobalVar.User,GlobalVar.StartTime,GlobalVar.OS,GlobalVar.Browser)
        Res_Headings.ScriptInfo(GlobalVar.scriptname, GlobalVar.User, GlobalVar.StartTime)

        # Kill the logging object
        Res_Headings.Kill()

    @classmethod
    def tearDownClass(self):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print("Inside TearDownClass")
        GlobalVar.EndTime = time.strftime("%Y-%m-%d %H:%M")
        NumberOfTestcasePassed = 0
        NumberOfTestcaseFailed = 0
        DidNotRun = 0
        ScriptRunDuration = 0
        StartTime = GlobalVar.StartTime
        EndTime = GlobalVar.EndTime

        # Calculate the pass
        # for item in GlobalVar.TillRunningStatus.itervalues():
        for item in GlobalVar.TillRunningStatus.values():

            if (str(item).upper().find('PASS') != -1):
                NumberOfTestcasePassed = NumberOfTestcasePassed + 1
            elif (str(item).upper().find('FAIL') != -1):
                NumberOfTestcaseFailed = NumberOfTestcaseFailed + 1
            else:
                DidNotRun = DidNotRun + 1

        print_res(GlobalVar.resultfile,
                  "******************************************************************************")
        print_res(GlobalVar.resultfile,
                  "\n\n***                      Script  Run Summary                               ***\n\n")
        print_res(GlobalVar.resultfile, str("***     Total No of Testcase: " + str(GlobalVar.TotalNumberOfTCS) + "\n"))
        print_res(GlobalVar.resultfile, str("***     Total Testcase Passed: " + str(NumberOfTestcasePassed) + "\n"))
        print_res(GlobalVar.resultfile, str("***     Total Testcase Failed: " + str(NumberOfTestcaseFailed) + "\n"))
        print_res(GlobalVar.resultfile, str("***     TestCase with no result: " + str(DidNotRun) + "\n"))
        print_res(GlobalVar.resultfile, str("***     Start Time :" + str(StartTime) + ""))
        print_res(GlobalVar.resultfile, str("***     End Time :" + str(EndTime) + ""))
        print_res(GlobalVar.resultfile,
                  "\n******************************************************************************\n\n")

    def verify(self, value, msg):

        if (value == PASS or value == TRUE):
            log = "\nPASSED : " + str(msg)
            print(log)
            GlobalVar.tcRunStatus = "PASS"
            print_res(GlobalVar.resultfile, "PASS  :  " + str(msg) + "")

        else:
            log = "\nFAILED : " + str(msg)
            print(log)
            GlobalVar.tcRunStatus = "FAILED"
            tmpMessage = "FAILED  :  Error***" + str(msg) + "***"
            print_res(GlobalVar.resultfile, tmpMessage)
            raise AssertionError(str(msg))

    def verify_continue(self, value, msg):
        try:
            if (value):
                log = "\nPASSED : " + str(msg)
                print(log)
                GlobalVar.tcRunStatus = "PASS"
                print_res(GlobalVar.resultfile, "PASS  :  " + str(msg) + "")
            else:
                log = "\nFAILED : " + str(msg)
                print(log)
                raise AssertionError(str(msg))

        except:
            GlobalVar.tcRunStatus = "FAILED"
            tmpMessage = "FAILED  :  Error***" + str(msg) + "***"
            print_res(GlobalVar.resultfile, tmpMessage)

            # Append the value in the  tcVerifyCountinueRunList
        GlobalVar.tcVerifyCountinueRunList.append(GlobalVar.tcRunStatus)


class ScriptEnter():
    """ This Class would be call at the beginning of the script enter"""

    def __init__(self):
        """Constructor"""

    # Initialize all the global variable or constant
    initiate_script_enter()

    # if TestLink Upload is true than print the plan and Build Name
    # TestLinkHeadingData = "{'TestPlan':'"+str(TESTLINK_PLAN_NAME)+ "','BuildName':'"+str(BUILD_NAME)+"'}"
    # if (TESTLINK_UPLOAD):
    # print_res(GlobalVar.testlinkUploadFile,TestLinkHeadingData)


class ScriptExit():
    """ This Class would be call at the beginning of the script enter"""

    def __init__(self):
        """Constructor"""
        GlobalVar.EndTime = time.strftime("%Y-%m-%d %H:%M")
        NumberOfTestcasePassed = 0
        NumberOfTestcaseFailed = 0
        DidNotRun = 0
        ScriptRunDuration = 0
        StartTime = GlobalVar.StartTime
        EndTime = GlobalVar.EndTime

        # Calculate the pass
        for item in GlobalVar.TillRunningStatus.itervalues():

            if (str(item).upper().find('PASS') != -1):
                NumberOfTestcasePassed = NumberOfTestcasePassed + 1
            elif (str(item).upper().find('FAIL') != -1):
                NumberOfTestcaseFailed = NumberOfTestcaseFailed + 1
            else:
                DidNotRun = DidNotRun + 1

        # calculate the time difference

        print_res(GlobalVar.resultfile,
                  "******************************************************************************")
        print_res(GlobalVar.resultfile,
                  "\n\n***                      Script  Run Summary                               ***\n\n")
        print_res(GlobalVar.resultfile, str("***     Total No of Testcase: " + str(GlobalVar.TotalNumberOfTCS) + "\n"))
        print_res(GlobalVar.resultfile, str("***     Total Testcase Passed: " + str(NumberOfTestcasePassed) + "\n"))
        print_res(GlobalVar.resultfile, str("***     Total Testcase Failed: " + str(NumberOfTestcaseFailed) + "\n"))
        print_res(GlobalVar.resultfile, str("***     TestCase with no result: " + str(DidNotRun) + "\n"))
        print_res(GlobalVar.resultfile, str("***     Start Time :" + str(StartTime) + ""))
        print_res(GlobalVar.resultfile, str("***     End Time :" + str(EndTime) + ""))
        print_res(GlobalVar.resultfile,
                  "\n******************************************************************************\n\n")
