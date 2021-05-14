import unittest
from signUpDriver import SignUp


class Configure:
    def configure_test_1_successOrExisted():
        (username, password) = \
            ("sampleuser_SignUp@mail.com", "abcdefgh")
        return (username, password)

    def configure_test_2_checkPassword():
        (username, password, checkPassword) = \
            ("sampleuser_SignUp@mail.com", "abcdefgh", "abc")
        return (username, password, checkPassword)


class TestSignUp(unittest.TestCase):

    def test_SignUp_successOrExisted(self):
        # Sign up - either success or duplicate user error message

        # data input
        (username, password) = Configure.configure_test_1_successOrExisted()

        # test signUp
        testSignUp = SignUp()
        (urlCurrent, alertInfo) = testSignUp.SignUp(username, password)

        IsSignUpSuccess = urlCurrent == "http://localhost:5000/login"
        IsSignUpFailed = urlCurrent == "http://localhost:5000/signup"
        IsAlertInfo = alertInfo \
            == "That email address is already associated with an account"

        self.assertTrue(IsSignUpSuccess or (IsSignUpFailed and IsAlertInfo))

    def test_signUp_loginLink(self):
        testSignUp = SignUp()
        loginUrl = testSignUp.SignUp_loginLink()

        isLoginUrl = loginUrl == "http://localhost:5000/login"

        self.assertTrue(isLoginUrl)

    def test_signUp_checkPassword(self):
        # 1st: error message will be shown due to unmatching password
        # 2nd: error also with checking password too short

        (username, password, checkPassword) \
            = Configure.configure_test_2_checkPassword()

        testSignUp = SignUp()
        (alert1, alert2) = \
            testSignUp.SignUp_InvalidCheckPassword(username, password, checkPassword)

        IsAlert1 = alert1 == "Passwords must match"
        IsAlert2 = alert2 == "Field must be between 8 and 80 characters long."

        self.assertTrue(IsAlert1 and IsAlert2, alert1)


if __name__ == '__main__':
    unittest.main()
