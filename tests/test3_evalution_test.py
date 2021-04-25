import unittest
import time
import os
from signUpDriver import signUp
from createProjectDriver import createProject
from evaluationDriver import evaluation

class configure:
    def configure_test_1_successOrExisted():
        (username, password) = ("sampleuser_CreateEvaluation@mail.com", "abcdefgh")  
        return (username, password)
        
    def configure_test_3_CreateProject_Success():
        #both xlsx and json files are downloaded in the selenium/tests directory
        (username, password) = ("sampleuser_CreateEvaluation@mail.com", "abcdefgh") 
        (projectname, projectdescription) =("Informational Processing1", "A sample project using an ELPISSrubric for Informational Processing") 
        (studentFile, jsonFile) = (os.getcwd() + "/sample_roster.xlsx", os.getcwd() + "/interpersonal_communication_scale3.json")
        return (username, password, projectname, projectdescription, studentFile, jsonFile)
    
    def configure_test_Evaluations():
        (username, password) = ("sampleuser_CreateEvaluation@mail.com", "abcdefgh") 
        (projectName, evaluationName) = ("Informational Processing", "Week 1")
        return (username, password, projectName, evaluationName)

class TestEvalution(unittest.TestCase):
    
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
        # success or duplicate evaluation

        (username, password, projectName, evaluationName) = configure.configure_test_Evaluations()
        createE = evaluation()
        
        (projectURL, alertInfo) = createE.driver_createEvaluation_attempt(username, password, projectName, evaluationName)
        
        IsAtEvalCreatePage = projectURL == "http://localhost:5000/load_project/" + username + username + projectName + "full/noAlert"
        
        IsAlertInfo = alertInfo == "The evaluation_name has been used before"
        IsNoError = alertInfo == "no error"
        
        msg = alertInfo
        
        self.assertTrue((not IsAtEvalCreatePage and IsNoError) or (IsAtEvalCreatePage and IsAlertInfo, msg))
    