from selenium.webdriver import Chrome
from loginDriver import LogIn
from ratingDriver import Rating
import time



class Sharing:
    def __init__(self):
        self.driver = Chrome()
    
    def Close(self):
        self.driver.quit()
    
    def manageProject(self):
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Manage Projects"))
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[text()='Manage']").click()
        self.driver.implicitly_wait(5)
    
    def shareProject(self, shareToUser):
        self.driver.find_element_by_xpath("//*[text()='Create new Permission to Share your Rubric']").click()
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_name("username").send_keys(shareToUser)
        self.driver.find_element_by_css_selector("#CNP > div > div > div.modal-footer > button.btn.btn-primary").click()
        self.driver.implicitly_wait(5)

    def deleteSharing(self):
        self.driver.find_element_by_xpath("//input[@value='delete']").click()
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.implicitly_wait(5)

    def logout(self):
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Manage Projects"))
        self.driver.implicitly_wait(5)

        
    def sharingProjectAndDelete(self, username, password, shareToUser):
        #one user shares the project to another user
        
        #login
        LogIn.login(self, username, password)
        self.driver.implicitly_wait(5)
        
        #Manage Projects
        Sharing.manageProject(self)
                
        #share the project
        Sharing.shareProject(self, shareToUser)
        
        #obtain the successText of sharing
        successText = self.driver.find_element_by_xpath("//*[text()='Permission successfully created']").text
        
        
        #delete the sharing
        Sharing.deleteSharing(self)
        
        #obtain the deleteSuccess text
        deleteText = self.driver.find_element_by_xpath("//*[text()='successfully delete permission']").text
        
        Sharing.Close(self)
        
        return (successText, deleteText)

    def sharingProjectAndCheck(self, username, password, sharedUser, sharedUserPw, projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3):
        #Share the project and modify from the sharedUser
        
        #Firstly share the project from one user -- (username, password) to (sharedUser, sharedUserPw)
        #login
        LogIn.login(self, username, password)
        self.driver.implicitly_wait(5)
        
        #Manage Projects
        Sharing.manageProject(self)
        
        
        #share the project
        Sharing.shareProject(self, sharedUser)
        
        #obtain the successText of sharing
        successText = self.driver.find_element_by_xpath("//*[@id='feedback']").text
        
        #logout
        Sharing.logout(self)
        
        #login as the user who receives the shared project - (sharedUser, sharedUserPw)
        LogIn.login(self, sharedUser, sharedUserPw)
        
        # self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_css_selector("body > div.middle > div > div > div.w3-bar > h1:nth-child(2) > button"))
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_xpath("//*[text()='Shared project']"))
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text("Teamwork2"))    
        
        #rate as a sharedUser
        (statusA, statusB, statusC) = Rating.Rate_Group(self, username, password, projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3)

        
        #delete the sharing:
        
        #login as the (username, password) again to delete the sharing - ensure to run for another time won't fail
        LogIn.login(self, username, password)
        self.driver.implicitly_wait(5)        
        #Manage Projects
        Sharing.manageProject(self)
        #delete the sharing
        Sharing.deleteSharing(self)
        
        
        Sharing.Close(self)
        
        return (statusA, statusB, statusC)
    
    
    
    
    
    
    
    
        
        
        