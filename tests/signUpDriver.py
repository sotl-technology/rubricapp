#This class is for the driver setup of signUp

from selenium.webdriver import Chrome
import time


class signUp:   
    
    def __init__(self):
        
        self.driver = Chrome() 
        self.driver.get("http://localhost:5000")
        self.driver.find_element_by_link_text("Sign up").click()
    
    def setUpUser(self, username, password, checkPw):
        self.driver.find_element_by_id("email").send_keys(username) 
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("checkpassword").send_keys(checkPw)
        self.driver.find_element_by_css_selector(".btn").click()        
        self.driver.implicitly_wait(5)
    
    def Driver_SignUp(self, username, password):
        
        #setup user
        signUp.setUpUser(self, username, password, password) #password and checkPw should be the same in this case
                
        #obtain current url
        urlCurrent = self.driver.current_url 
        
        #obtain error message if duplicate username happens
        alertInfo = self.driver.find_element_by_class_name("alert-info").text
        
        signUp.Close(self)
         
        return (urlCurrent, alertInfo)
        
    def Driver_SignUp_loginLink(self):
        #check the link to login page
        self.driver.find_element_by_link_text("Already have an account? Log in.").click()
        loginUrl = self.driver.current_url
        signUp.Close(self)
        
        return loginUrl
    
    
    def Driver_SignUp_InvalidCheckPassword(self, username, password, checkPw):
    
        #setup user
        signUp.setUpUser(self, username, password, checkPw)   
        
        alert1 = self.driver.find_element_by_xpath("//*[text()='Passwords must match']").text
        alert2 = self.driver.find_element_by_xpath("//*[text()='Field must be between 8 and 80 characters long.']").text  
        signUp.Close(self)
        
        return (alert1, alert2)
        
    
    
    
    
    
    def Close(self):
        self.driver.quit()