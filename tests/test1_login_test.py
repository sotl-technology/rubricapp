import unittest
from signUpDriver import SignUp
from loginDriver import LogIn

class Configure:
    def configure_test_2_0_successOrExisted():
        (username, password) = ("sampleuser_Login@mail.com", "abcdefgh")  
        return (username, password)
        
    def configure_test_2_1_LoginFailure_by_user_not_exist():
        (username, password) = ("Wronginput@gmail.com","abcdefgh") 
        return (username, password)
        
    def configure_test_2_2_LoginFailure_by_invalid_password():
        (username, password) = ("sampleuser_Login@mail.com","a"*7)
        return (username, password)
        
    def configure_test_2_3_LoginFailure_by_invalid_email():
        (username, password) = ("Wronginput.gmail.com","a"*7) 
        return (username, password)
        
    def configure_test_2_4_LoginFailure_by_incorrect_password():
        (username, password) = ("sampleuser_Login@mail.com","a"*8)
        return (username, password)
    

class TestLogin(unittest.TestCase):
    
    
    
    def test_1_SignUp_Existed(self):
        #sign up        
        testSignUp = SignUp()
        (username, password) = Configure.configure_test_2_0_successOrExisted()
        (urlCurrent, alertInfo) = testSignUp.sign_up(username, password)
    
    def test_signUpLink(self):
        #test the signUp link on login page
        
        logInPage = LogIn()
        signUpUrl = logInPage.Login_signUpLink()
        
        isLoginUrl = signUpUrl == "http://localhost:5000/signup"
        
        self.assertTrue(isLoginUrl)
    
    
    def test_2_0_LoginSuccess(self):
        #successfully login - with correct username and password
        
        logInPage = LogIn()
        (username, password) = Configure.configure_test_2_0_successOrExisted()
        currentUrl = logInPage.LoginAttempt(username, password)
        
        IsLoginSuccess = (currentUrl == "http://localhost:5000/instructor_project")
        
        self.assertTrue(IsLoginSuccess)   
    
    def test_2_1_LoginFailure_by_user_not_exist(self):
        #failed login due to "user doesn't exist"
        
        logInPage = LogIn()
        (username, password) = Configure.configure_test_2_1_LoginFailure_by_user_not_exist()
        alertInfo = logInPage.getUserExistAlert(username, password)
        IsAlert = alertInfo == "user doesn't exist"        
        self.assertTrue(IsAlert)
        
    
    def test_2_2_LoginFailure_by_invalid_password(self):
        #failed login due to password too short or too long(should be between 8 - 80)
        
        logInPage = LogIn()
        (username, password) = Configure.configure_test_2_2_LoginFailure_by_invalid_password()
        alertInfo = logInPage.getPasswordAlert(username, password)

        IsAlert = alertInfo == "Field must be between 8 and 80 characters long."
        
        self.assertTrue(IsAlert)
     
    def test_2_3_LoginFailure_by_invalid_email(self):
        #failed login due to invalid email (no @), along with password too short 
        
        logInPage = LogIn()
        (username, password) = Configure.configure_test_2_3_LoginFailure_by_invalid_email()
        (alert1, alert2) = logInPage.getInvalidEmailAlert(username, password)
        
        IsAlert1 = alert1 == "Invalid email"
        IsAlert2 = alert2 == "Field must be between 8 and 80 characters long."
            
        self.assertTrue(IsAlert1 and IsAlert2)    
    
    def test_2_4_LoginFailure_by_incorrect_password(self):
        #failed login due to incorrect password 
        
        logInPage = LogIn()
        (username, password) = Configure.configure_test_2_4_LoginFailure_by_incorrect_password()
        alertInfo = logInPage.getIncorrectPasswordAlert(username, password)

        IsAlert = alertInfo == "password not correct"
        
        self.assertTrue(IsAlert)
    
    
if __name__ == '__main__':
    unittest.main()    