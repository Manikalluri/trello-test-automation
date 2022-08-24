
class WelcomeTrello():

    @staticmethod
    def verify_trello_home_label(driver):
        """This method will check the Home lable on home screen is displayed or not"""
        element = driver.find_element_by_css_selector(".P2YtVJyxrOCJp6 > span:nth-child(2)")
        count = 0
        if element.is_displayed():
            assert True
            count = count + 1
            return count
        else:
            assert False
            
    @staticmethod
    def verify_trello_work_space(driver):
        """This method will check the created workspace enabled or not"""
        element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/main/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/ul/li[1]/a")
        print("element")
        count = 0
        if element.is_displayed():
            assert True
            count = count + 1
            return count
        else:
            assert False





  