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
        test_sign_up = SignUp()
        (url_current, alert_info) = test_sign_up.sign_up(username, password)

        is_sign_up_success = url_current == "http://localhost:5000/login"
        is_sign_up_failed = url_current == "http://localhost:5000/signup"
        is_alert_info = alert_info \
            == "That email address is already associated with an account"

        self.assertTrue(is_sign_up_success
                        or (is_sign_up_failed and is_alert_info))

    def test_signUp_loginLink(self):
        test_sign_up = SignUp()
        login_url = test_sign_up.sign_up_login_link()

        is_login_url = login_url == "http://localhost:5000/login"

        self.assertTrue(is_login_url)

    def test_signUp_checkPassword(self):
        # 1st: error message will be shown due to unmatching password
        # 2nd: error also with checking password too short

        (username, password, checkPassword) \
            = Configure.configure_test_2_checkPassword()

        test_sign_up = SignUp()
        (alert1, alert2) = test_sign_up.\
            invalid_check_password(username, password, checkPassword)

        is_alert1 = alert1 == "Passwords must match"
        is_alert2 = alert2 == "Field must be between 8 and 80 characters long."

        self.assertTrue(is_alert1 and is_alert2, alert1)


if __name__ == '__main__':
    unittest.main()
