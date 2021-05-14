import unittest
import time
import os
from signUpDriver import SignUp
from createProjectDriver import CreateProject
from evaluationDriver import Evaluation


class Configure:
    def configure_test_1_successOrExisted():
        (username, password) = \
            ("sampleuser_CreateEvaluation@mail.com", "abcdefgh")
        return (username, password)

    def configure_test_3_CreateProject_Success():
        # both xlsx and json files are downloaded in the selenium/tests
        (username, password) = \
            ("sampleuser_CreateEvaluation@mail.com", "abcdefgh")
        (projectname, projectdescription) = \
            ("Informational Processing1",
             "A sample project using an ELPISSrubric "
             "for Informational Processing")
        (studentFile, jsonFile) = \
            (os.getcwd() + "/sample_roster.xlsx",
             os.getcwd() + "/interpersonal_communication_scale3.json")
        return (username, password, projectname,
                projectdescription, studentFile, jsonFile)

    def configure_test_Evaluations():
        (username, password) = \
            ("sampleuser_CreateEvaluation@mail.com", "abcdefgh")
        (projectName, evaluationName) = ("Informational Processing", "Week 1")
        return (username, password, projectName, evaluationName)


class TestEvalution(unittest.TestCase):

    def test_1_SignUp_Existed(self):
        # sign up
        test_sign_up = SignUp()
        (username, password) = Configure.configure_test_1_successOrExisted()
        (url_current, alert_info) = test_sign_up.sign_up(username, password)

    def test_3_CreateProject_Success(self):
        # create project
        (username, password, project_name,
         project_description, student_file, json_file) \
            = Configure.configure_test_3_CreateProject_Success()
        create_p = CreateProject()
        (url_current, alert_info) = create_p.\
            create_project_attempt(username, password,
                                   project_name, project_description,
                                   student_file, json_file)

    def test_Evaluations(self):
        # success or duplicate evaluation
        (username, password, projectName, evaluationName) =\
            Configure.configure_test_Evaluations()
        create_e = Evaluation()

        (projectURL, alert_info) = create_e.\
            create_evaluation_attempt(username, password,
                                      projectName, evaluationName)
        std_url = "http://localhost:5000/load_project/" + \
            username + username + projectName + "full/noAlert"
        is_at_eval_create_page = projectURL == std_url

        is_alert_info = alert_info == "The evaluation_name has been used before"
        is_no_error = alert_info == "no error"

        msg = alert_info

        self.assertTrue((not is_at_eval_create_page and is_no_error)
                        or (is_at_eval_create_page and is_alert_info, msg))
