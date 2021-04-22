from selenium.webdriver import Chrome
from loginDriver import logIn
from ratingDriver import rating
import time



class sharing:
    def __init__(self):
        self.driver = Chrome()
    
    def Close(self):
        self.driver.quit()
    
    def manageProject(self):
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Manage Projects"))
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text("Manage").click()
        self.driver.implicitly_wait(5)
    
    def shareProject(self, shareToUser):
        self.driver.find_element_by_css_selector("body > div.middle > div.container.w3-row-padding > div > div:nth-child(5) > div:nth-child(2) > table > tbody > tr > td:nth-child(3) > button").click()
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_name("username").send_keys(shareToUser)
        self.driver.find_element_by_css_selector("#CNP > div > div > div.modal-footer > button.btn.btn-primary").click()
        self.driver.implicitly_wait(5)

    def deleteSharing(self):
        self.driver.find_element_by_css_selector("body > div.middle > div.container.w3-row-padding > div > div:nth-child(5) > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").click()
        self.driver.switch_to.alert.accept()

    def logout(self):
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Manage Projects"))
        self.driver.implicitly_wait(5)

        
    def sharingProjectAndDelete(self, username, password, shareToUser):
        #login
        logIn.Driver_Login(self,username, password) 
        self.driver.implicitly_wait(5)
        
        #Manage Projects
        sharing.manageProject(self)
        
        
        #share the project
        sharing.shareProject(self, shareToUser)
        
        #obtain the successText of sharing
        successText = self.driver.find_element_by_xpath("//*[@id='feedback']").text
        
        #delete the sharing
        sharing.deleteSharing(self)
        
        #obtain the deleteSuccess text
        deleteText = self.driver.find_element_by_xpath("//*[@id='feedback']").text
        
        return (successText, deleteText)

    def sharingProjectAndCheck(self, username, password, sharedUser, sharedUserPw, projectName, evaluationName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3):
        
        #Firstly share the project from one user -- (username, password) to (sharedUser, sharedUserPw)
        #login
        logIn.Driver_Login(self,username, password) 
        self.driver.implicitly_wait(5)
        
        #Manage Projects
        sharing.manageProject(self)
        
        
        #share the project
        sharing.shareProject(self, sharedUser)
        
        #obtain the successText of sharing
        successText = self.driver.find_element_by_xpath("//*[@id='feedback']").text
        
        #logout
        sharing.logout(self)
        
        #login as the user who receives the shared project - (sharedUser, sharedUserPw)
        logIn.Driver_Login(self, sharedUser, sharedUserPw) 
        
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_css_selector("body > div.middle > div > div > div.w3-bar > h1:nth-child(2) > button"))
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Teamwork2"))
        # time.sleep(3)       
        
        
        (metaGroupURL, statusA, statusB, statusC) = rating.Rate_Group(self, username, password, projectName, evaluationName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3)

        # time.sleep(5)
        
        #delete the sharing:
        
        #login as the (username, password) again to delete the sharing - ensure to run for another time won't fail
        logIn.Driver_Login(self,username, password) 
        self.driver.implicitly_wait(5)
        
        #Manage Projects
        sharing.manageProject(self)

        #delete the sharing
        sharing.deleteSharing(self)
        
        return (statusA, statusB, statusC)
    
    
    
    
    
    
    
    
        
        
        