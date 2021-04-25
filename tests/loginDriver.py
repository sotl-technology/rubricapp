
from selenium.webdriver import Chrome
import time


class logIn:


    def __init__(self):
        
        self.driver = Chrome() 

    def Driver_Login(self, username, password):
        
        self.driver.get("http://localhost:5000")
        self.driver.find_element_by_link_text("Login").click()    
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)       
        
        rememberButton = self.driver.find_element_by_id("remember")     
        if not rememberButton.is_selected():
            rememberButton.click()
        
        self.driver.find_element_by_css_selector(".btn").click()
    
    def Driver_Login_signUpLink(self):
        self.driver.get("http://localhost:5000")
        self.driver.find_element_by_link_text("Login").click()
        self.driver.find_element_by_link_text("Don't yet have an account? Sign up.").click()
        signUpUrl = self.driver.current_url
        return signUpUrl
        
            
    def LoginAttempt(self, username, password): 
        #successful login
        self.Driver_Login(username, password)
        urlCurrent = self.driver.current_url
        logIn.Close(self)
        return urlCurrent
    
    def Close(self):
        self.driver.quit()
        
        
    def getUserExistAlert(self, username, password):  #1
        #failed login due to "user doesn't exist"
        
        # the "text() = user doesn\'t exist" somehow cannot work -- maybe due to "doesn't" in there
        self.Driver_Login(username, password)
        alert1 = self.driver.find_element_by_xpath("//*[text()[contains(.,'user doesn')]]").text
        logIn.Close(self)
        return alert1
        
    def getPasswordAlert(self,username, password): #2
        #failed login due to password too short or too long(should be between 8 - 80)
        self.Driver_Login(username, password)
        alertInfo = self.driver.find_element_by_xpath("//*[text()='Field must be between 8 and 80 characters long.']").text        
        logIn.Close(self)
        return alertInfo
        
    def getInvalidEmailAlert(self, username, password): #3
        #failed login due to invalid email (no @), along with password too short 
        self.Driver_Login(username, password)
        alert1 = self.driver.find_element_by_xpath("//*[text()='Invalid email']").text 
        alert2 = self.driver.find_element_by_xpath("//*[text()='Field must be between 8 and 80 characters long.']").text 
        logIn.Close(self)       
        return (alert1, alert2)
        
    def getIncorrectPasswordAlert(self, username, password): #4
        #failed login due to incorrect password 
        self.Driver_Login(username, password)
        alertInfo = self.driver.find_element_by_xpath("//*[text()='password not correct']").text 
        logIn.Close(self)
        return alertInfo
        