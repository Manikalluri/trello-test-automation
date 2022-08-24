""" This module is developed for all type of result logging features """

""" Include Section """
import logging
from automation.comm_utility.Constants import *

def print_res(Filename, Namelist):
    """ This function write in the result file"""
    FHandle = open(Filename, "a")

    # Write all the lines at once:
    FHandle.writelines(Namelist + "\n")

    # Close the file
    FHandle.close()

@staticmethod
def print_log(log):
    print(log)
    print_res(GlobalVar.resultfile, log)

class Gen5Logger:
    """ This class contains all methods to interact with result file"""

    logger = None
    Fhandle = None
    formatter = None

    def __init__(self):
        """Constructor - This constructor would initiate """

        # Instantiate the logger class and set the 
        self.logger = logging.getLogger(GlobalVar.runPhase)

        # create file handler and set level to debug
        self.Fhandle = logging.FileHandler(GlobalVar.resultfile)

        self.Set_default_formatter()

    def Set_default_formatter(self):
        """ This private method set the default formating"""

        # set level to debug 
        self.logger.setLevel(logging.INFO)
        self.Fhandle.setLevel(logging.INFO)

        # create default formatter
        formatter = logging.Formatter('%(message)s')

        # add formatter to fhandle and add fhandle to logger
        self.Fhandle.setFormatter(formatter)
        self.logger.addHandler(self.Fhandle)

    def Kill(self):
        """ Kill the own object and release the memory"""

        del self

    def Info(self, msg):
        """ This method is for debuging the script  """

        # set level to debug 
        self.logger.setLevel(logging.DEBUG)
        self.Fhandle.setLevel(logging.DEBUG)

        # create default formatter
        self.formatter = logging.Formatter('%(message)s')

        # add formatter to fhandle and add fhandle to logger
        self.Fhandle.setFormatter(self.formatter)
        self.logger.addHandler(self.Fhandle)

        # Print with debug quotes

        self.logger.debug(msg)

    def ResPrint(self, msg):
        """ This method would simply print the message in the result file  """

        # set level to debug
        # self.logger.setLevel(logging.INFO)
        # self.Fhandle.setLevel(logging.INFO)

        ## create default formatter
        # self.formatter = logging.Formatter('%(message)s')

        ## add formatter to fhandle and add fhandle to logger
        # self.Fhandle.setFormatter(self.formatter)
        # self.logger.addHandler(self.Fhandle)

        # Print with info quotes

        self.logger.info(msg)

    def ScriptInfo(self, SName, Uname, Time):
        """ This method would print the script info """

        self.ResPrint("******************************************************************************")
        self.ResPrint("***     Script Name: " + SName)
        self.ResPrint("***     User Name:" + Uname)
        self.ResPrint("***     Time script run :" + Time)
        self.ResPrint(" ")
        self.ResPrint("******************************************************************************")
        self.ResPrint(" ")
        self.ResPrint(" ")
        self.ResPrint(" ")
        self.ResPrint(" ")
