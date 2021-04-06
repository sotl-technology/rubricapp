import unittest
from signUpDriver import signUp

class configure:
    def configure_test_1_successOrExisted():
        (username, password) = ("sampleuser_SignUp@mail.com", "abcdefgh")  
        return (username, password)



class TestSignUp(unittest.TestCase):
    
    def test_1_SignUp_successOrExisted(self):
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
        IsAlertInfo = alertInfo == "Warning !!! The email has been used"
        
        self.assertTrue(IsSignUpSuccess or (IsSignUpFailed and IsAlertInfo))
        
        
        
if __name__ == '__main__':
    unittest.main()