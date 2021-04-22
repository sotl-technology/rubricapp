import unittest
from signUpDriver import signUp

class configure:
    def configure_test_1_successOrExisted():
        (username, password) = ("sampleuser_SignUp@mail.com", "abcdefgh")  
        return (username, password)
    def configure_test_2_checkPassword():
        (username, password, checkPassword) = ("sampleuser_SignUp@mail.com", "abcdefgh", "abc")
        return (username, password, checkPassword)

class TestSignUp(unittest.TestCase):
    
    
    def test_SignUp_successOrExisted(self):
        #This test would work for both first time creating a new user and duplicate creation. The duplicate running would assert the error message.
        
        #data input
        (username, password) = configure.configure_test_1_successOrExisted()
        
        #This only prints out when there is an error
        print("\n\nTesting SignUp\n\n")  
        
        #test function
        testSignUp = signUp()                        
        (urlCurrent, alertInfo) = testSignUp.Driver_SignUp(username, password)
        testSignUp.Close()
        
        IsSignUpSuccess = urlCurrent == "http://localhost:5000/login"
        IsSignUpFailed = urlCurrent == "http://localhost:5000/signup"
        IsAlertInfo = alertInfo == "That email address is already associated with an account"
        
        self.assertTrue(IsSignUpSuccess or (IsSignUpFailed and IsAlertInfo))
        

    def test_signUp_loginLink(self):
        
        testSignUp = signUp()
        loginUrl = testSignUp.Driver_SignUp_loginLink()
        
        isLoginUrl = loginUrl == "http://localhost:5000/login"
        
        self.assertTrue(isLoginUrl)
    

    def test_signUp_checkPassword(self):
        
        (username, password, checkPassword) = configure.configure_test_2_checkPassword()
        
        testSignUp = signUp()  
        (alert1, alert2) = testSignUp.Driver_SignUp_InvalidCheckPassword(username, password, checkPassword)
        
        IsAlert1 = alert1 == "Passwords must match"
        IsAlert2 = alert2 == "Field must be between 8 and 80 characters long."
        
        self.assertTrue(IsAlert1 and IsAlert2, alert1)
    
    
    
    
        
if __name__ == '__main__':
    unittest.main()