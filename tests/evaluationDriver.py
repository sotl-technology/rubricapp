
from selenium.webdriver import Chrome
from loginDriver import LogIn

import time

class Evaluation:
    
    def __init__(self):
        self.driver = Chrome()
    
    def Close(self):
        self.driver.quit()
        
    def CreateEvaluation_attempt(self, username, password, projectName, evaluationName):
        
        LogIn.login(self, username, password)
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text(projectName))
        self.driver.implicitly_wait(5)        
        projectURL = self.driver.current_url
        
        self.driver.find_element_by_link_text("Create a New Evaluation").click()
        self.driver.find_element_by_id("evaluation_name").send_keys(evaluationName)
        self.driver.find_element_by_id("evaluation_submit").click()
        
        
        try:
            alertInfo = self.driver.find_element_by_xpath("//*[text()='The evaluation_name has been used before']").text
        except:
            alertInfo = "no error"
        
        self.driver.implicitly_wait(5)
        Evaluation.Close(self)
        
        return (projectURL,alertInfo)
