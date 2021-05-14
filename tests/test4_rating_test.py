import unittest
import time
import os
from signUpDriver import SignUp
from createProjectDriver import CreateProject
from evaluationDriver import Evaluation
from ratingDriver import Rating


class Configure:
    def configure_test_1_successOrExisted():
        (username, password) = \
            ("sampleuser13@mailinator.com", "abcdefgh")
        return (username, password)

    def configure_test_3_CreateProject_Success():
        # both xlsx and json files have to be downloaded previously
        (username, password) = \
            ("sampleuser13@mailinator.com", "abcdefgh")
        (projectname, projectdescription) =\
            ("Teamwork2",
             "A sample project using an "
             "ELPISSrubric for Teamwork2")
        (studentFile, jsonFile) = (os.getcwd() + "/sample_roster.xlsx",
                                   os.getcwd() + "/teamwork_scale3.json")
        return (username, password, projectname,
                projectdescription, studentFile, jsonFile)

    def configure_test_Evaluations():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        return (username, password, projectName, evaluationName)

    def configure_test_Rating():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        (metagroupName, groupName) = ("b", "O")
        (level, checkbox1, checkbox2, checkbox3) = \
            ("Sporadically", True, True, False)
        return (username, password, projectName,
                evaluationName, metagroupName, groupName,
                level, checkbox1, checkbox2, checkbox3)

    def configure_test_Rating_Another_Group():
        (username, password) = \
            ("sampleuser13@mailinator.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        (metagroupName, groupName) = ("b", "F")
        (level, checkbox1, checkbox2, checkbox3) = \
            ("Frequently", False, False, True)
        return (username, password, projectName,
                evaluationName, metagroupName, groupName,
                level, checkbox1, checkbox2, checkbox3)

    def configure_test_attendance():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        (metagroupName, groupName) = ("b", "O")
        studentNameToCheck = "Wickens, Hebe"

        return (username, password, projectName,
                evaluationName, metagroupName, groupName, studentNameToCheck)


class TestRating(unittest.TestCase):

    def test_1_sign_up_existed(self):
        # sign up
        test_sign_up = SignUp()
        (username, password) = Configure.configure_test_1_successOrExisted()
        (url_current, alert_info) = test_sign_up.sign_up(username, password)

    def test_3_create_project_success(self):
        # create project

        (username, password, project_name, project_description,
         student_file, json_file) = \
            Configure.configure_test_3_CreateProject_Success()
        create_p = CreateProject()

        (url_current, alert_info) = create_p.\
            create_project_attempt(username, password, project_name,
                                   project_description,
                                   student_file, json_file)

    def test_Evaluations(self):
        # create evaluation
        (username, password, projectName, evaluationName) =\
            Configure.configure_test_Evaluations()
        create_e = Evaluation()

        (project_url, alert_info) = create_e.\
            create_evaluation_attempt(username, password,
                                      projectName, evaluationName)

    def test_RatingTwoGroups(self):
        # select one group to rate; then select the 2nd group to rate

        (username, password, project_name,
         evaluation_name, metagroup_name, group_name,
         level, checkbox1, checkbox2, checkbox3) =\
            Configure.configure_test_Rating()

        create_r = Rating()
        (statusA, statusB, statusC) = create_r.\
            rating_one_group(username, password, project_name, evaluation_name,
                             metagroup_name, group_name, level,
                             checkbox1, checkbox2, checkbox3)
        if checkbox1:
            self.assertTrue(statusA)
        if checkbox2:
            self.assertTrue(statusB)
        if checkbox3:
            self.assertTrue(statusC)

        # rate another group
        create_r = Rating()
        (username, password, project_name, evaluation_name,
         metagroup_name, group_name, level,
         checkbox1, checkbox2, checkbox3) = \
            Configure.configure_test_Rating_Another_Group()
        (statusA, statusB, statusC) = create_r.\
            rating_one_group(username, password, project_name, evaluation_name,
                             metagroup_name, group_name, level,
                             checkbox1, checkbox2, checkbox3)
        if checkbox1:
            self.assertTrue(statusA)
        if checkbox2:
            self.assertTrue(statusB)
        if checkbox3:
            self.assertTrue(statusC)

    def test_Attendance(self):
        # test checkbox of the attendance

        (username, password, project_name, evaluation_name,
         metagroup_name, group_name, student_name_to_check) = \
            Configure.configure_test_attendance()

        create_r = Rating()
        response = create_r.\
            rate_attendance(username, password, project_name,
                            evaluation_name, metagroup_name, group_name,
                            student_name_to_check)

        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
