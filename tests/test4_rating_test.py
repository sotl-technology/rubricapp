import unittest
import time
import os
from signUpDriver import signUp
from createProjectDriver import createProject
from evaluationDriver import evaluation
from ratingDriver import rating

class configure:
    def configure_test_1_successOrExisted():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh")  
        return (username, password)
        
    def configure_test_3_CreateProject_Success():
        #both xlsx and json files have to be downloaded previously
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh") 
        (projectname, projectdescription) =("Teamwork2", "A sample project using an ELPISSrubric for Teamwork2")    
        (studentFile, jsonFile) = (os.getcwd() + "/sample_roster.xlsx", os.getcwd() + "/teamwork_scale3.json")
        return (username, password, projectname, projectdescription, studentFile, jsonFile)


    def configure_test_Evaluations():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh") 
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        return (username, password, projectName, evaluationName)
    
    def configure_test_Rating():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        (metagroupName, groupName) = ("b", "O")
        (level, checkbox1, checkbox2, checkbox3) = ("Sporadically", True,True,False)
        return (username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3)


    def configure_test_Rating_Another_Group():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        (metagroupName, groupName) = ("b", "F")
        (level, checkbox1, checkbox2, checkbox3) = ("Frequently", False, False, True) 
        return (username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3)
        
    def configure_test_attendance():
        (username, password) = ("sampleuser13@mailinator.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 1")
        (metagroupName, groupName) = ("b", "O")
        studentNameToCheck = "Wickens, Hebe"
        
        return (username, password, projectName, evaluationName, metagroupName, groupName, studentNameToCheck)
        
        
        

class TestRating(unittest.TestCase):
    '''
    def test_1_SignUp_Existed(self):
        #sign up
        testSignUp = signUp()
        (username, password) = configure.configure_test_1_successOrExisted() 
        (urlCurrent, alertInfo) = testSignUp.Driver_SignUp(username, password)


      
    
      
    def test_3_CreateProject_Success(self):
        #create project
        
        (username, password, projectname, projectdescription, studentFile, jsonFile) = configure.configure_test_3_CreateProject_Success()
        createP = createProject()
        
        (urlCurrent, alertInfo)= createP.createProject_attempt(username, password, projectname, projectdescription, studentFile, jsonFile)
        
        
    
    def test_Evaluations(self):
        #create evaluation

        (username, password, projectName, evaluationName) = configure.configure_test_Evaluations()
        createE = evaluation()
        
        (projectURL, alertInfo) = createE.driver_createEvaluation_attempt(username, password, projectName, evaluationName)
    '''
    
    
    def test_RatingTwoGroups(self):
        # select one group to rate; then select the 2nd group to rate

        (username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3) = configure.configure_test_Rating()
        
        createR = rating()        
        (statusA, statusB, statusC) = createR.driver_Rating_One_Group(username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3)
        if checkbox1: self.assertTrue(statusA)
        if checkbox2: self.assertTrue(statusB)
        if checkbox3: self.assertTrue(statusC)
        
        #rate another group
        createR = rating() 
        (username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3) = configure.configure_test_Rating_Another_Group()
        (statusA, statusB, statusC) = createR.driver_Rating_One_Group(username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3)
        if checkbox1: self.assertTrue(statusA)
        if checkbox2: self.assertTrue(statusB)
        if checkbox3: self.assertTrue(statusC)

    '''    
    

    def test_Attendance(self):        
        #test checkbox of the attendance
        
        (username, password, projectName, evaluationName, metagroupName, groupName, studentNameToCheck) = configure.configure_test_attendance()
        
        createR = rating()        
        response = createR.test_attendance(username, password, projectName, evaluationName, metagroupName, groupName, studentNameToCheck)
        
        self.assertTrue(response)
    '''
    
if __name__ == '__main__':
    unittest.main()  