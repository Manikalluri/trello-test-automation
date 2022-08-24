from enum import Enum
import os
import sys

""" Global Datatype module contains all datatype,Constant declaration """
""" Prime Drive and Path Section  """
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../../"
USER_CONFIG_PATH = PROJECT_DIR + "/UserConfig.ini"
DEFAULT_LOG_FOLDER = PROJECT_DIR + "/debug_logs"
DEFAULT_RESULT_FOLDER = DEFAULT_LOG_FOLDER
PASS = 1
FAIL = 0
FAILURE = '100%'
SUCCESS = '0%'
FALSE = 0
TRUE = 1


class GlobalVar:
    """"""
    Machinename = None
    testcasename = None
    scriptname = None
    runPhase = None
    resultfile = None
    OS = None
    Browser = None
    User = None
    StartTime = None
    EndTime = None
    tcRunStatus = None
    tcVerifyCountinueRunList = []
    wMainwin = None
    TestcaseRemark = None
    testlinkUploadFile = None
    CallSetFlag = None
    HtmlPreAppSetFlag = None
    Driver = None
    TotalNumberOfTCS = None
    TillRunningStatus = {}
    Suite = None
    CompatibilityViewSetting = None


