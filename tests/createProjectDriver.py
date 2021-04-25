
from loginDriver import logIn
from selenium.webdriver import Chrome

import time

class createProject:


    def __init__(self):
        self.driver = Chrome()
    
    def Close(self):
        self.driver.quit()
    
    def setprojectDescription(self, projectDescription, projectpassword):

        self.driver.find_element_by_id("project_name").send_keys(projectDescription)
        self.driver.find_element_by_id("project_description").send_keys(projectpassword)
    
    def download(self):
        self.driver.find_element_by_link_text("(Download a sample roster files)").click()
        self.driver.implicitly_wait(10)
    
    def setRoster(self, studentFile):

        self.driver.find_element_by_id("student_file").send_keys(studentFile)
    
    def setRubrics(self, jsonFile):
        self.driver.find_element_by_id("json_file").send_keys(jsonFile)
    
    def driver_createProject(self, username, password, projectDescription, projectpassword, 
        studentFile, jsonFile):
        
        logIn.Driver_Login(self,username, password) #login first
        self.driver.implicitly_wait(5)
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Create New Project"))        
        self.driver.implicitly_wait(5)

        createProject.setprojectDescription(self, projectDescription, projectpassword)
        
        #createProject.download(self) #the xlsx file should be downloaded previously
        #time.sleep(2) #this step is necessary to download the file      
        

        
        createProject.setRoster(self, studentFile)        

        createProject.setRubrics(self, jsonFile) 
        
        
        #This is for submission
        self.driver.find_element_by_css_selector(".w3-button").click()
        self.driver.implicitly_wait(5)

    
    
    def createProject_attempt(self, username, password, projectDescription, projectpassword, studentFile, jsonFile): # if run the 2nd time, the control flow would go to duplicate username

        self.driver_createProject(username, password, projectDescription, projectpassword, studentFile, jsonFile)  
      
        urlCurrent = self.driver.current_url
        
        try:
            #these error messages are not showing right now, change later to robust xpath
            if self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/form/div[1]/p").text != None:
                alertInfo = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/form/div[1]/p").text
        except:
            alertInfo = "no error"
        createProject.Close(self)
        
        return (urlCurrent, alertInfo)
        
        
    def getProjectNameAndDescriptionAlert(self, username, password, projectDescription, projectpassword, studentFile, jsonFile):
        self.driver_createProject(username, password, projectDescription, projectpassword, studentFile, jsonFile) 
        alert1 = self.driver.find_element_by_xpath("//*[text()='Field must be between 3 and 150 characters long.']").text
        alert2 = self.driver.find_element_by_xpath("//*[text()='Field must be between 0 and 255 characters long.']").text
        self.driver.implicitly_wait(5)
        createProject.Close(self)
        return (alert1, alert2)
        
    def getInvalidFileAlert(self, username, password, projectDescription, projectpassword, studentFile, jsonFile):
        self.driver_createProject(username, password, projectDescription, projectpassword, studentFile, jsonFile)
        #these error messages are not showing right now, change later to robust xpath
        alert1 = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/form/div[3]/p").text
        alert2 = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/form/div[4]/p").text
        self.driver.implicitly_wait(5)
        createProject.Close(self)
        return (alert1, alert2)
    
    
    
    def testRubricFileDriver(self, username, password):
    
        logIn.Driver_Login(self, username, password) #login first        
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Create New Project"))
        self.driver.implicitly_wait(5)
        
        
        url = self.driver.current_url
        window_before = self.driver.window_handles[0]
        #This would open a new window
        self.driver.find_element_by_xpath("//*[text()='(Browse sample rubric files)']").click()
        # time.sleep(5)
        self.driver.implicitly_wait(5)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)

    def testRubricFile_teamwork(self, username, password):

        createProject.testRubricFileDriver(self, username, password)
        self.driver.find_element_by_xpath("//*[text()='teamwork']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[text()='teamwork_scale3.json']").click()
        urlRubric = self.driver.current_url 
        createProject.Close(self)
        return urlRubric
    
    def testRubricFile_infoProcess(self, username, password):
        
        createProject.testRubricFileDriver(self, username, password)
        self.driver.find_element_by_xpath("//*[text()='information_processing']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[text()='information_processing.json']").click()
        url = self.driver.current_url
        createProject.Close(self)       
        return url
    
    def testRubricFile_communication(self, username, password):
        
        createProject.testRubricFileDriver(self, username, password)        
        self.driver.find_element_by_xpath("//*[text()='interpersonal_communication']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[text()='interpersonal_communication_scale3.json']").click()
        url = self.driver.current_url
        
        createProject.Close(self)
        return url
    
    
    
    
    
    
    
    
    