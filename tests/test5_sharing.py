import unittest
import time
import os
from signUpDriver import SignUp
from createProjectDriver import CreateProject
from evaluationDriver import Evaluation
from ratingDriver import Rating
from sharingDriver import Sharing

class Configure:

    def configure_test_1_successOrExisted():
        (username, password) = ("instructor1@example.com", "abcdefgh")  
        return (username, password)
        
    def configure_test_3_CreateProject_Success():
        #both xlsx and json files are downloaded in the selenium/tests directory
        (username, password) = ("instructor1@example.com", "abcdefgh") 
        (projectname, projectdescription) =("Teamwork2", "A sample project using an ELPISSrubric for Teamwork2")       
        (studentFile, jsonFile) = (os.getcwd() + "/sample_roster.xlsx", os.getcwd() + "/teamwork_scale3.json")
        return (username, password, projectname, projectdescription, studentFile, jsonFile)


    def configure_test_Evaluations():
        (username, password) = ("instructor1@example.com", "abcdefgh") 
        (projectName, evaluationName) = ("Teamwork2", "Week 2")
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
        
    
    def configure_test_sharingAndDelete():
        (username, password, shareToUser) = ("instructor1@example.com", "abcdefgh", "ta@example.com")
        return (username, password, shareToUser)
        
    def configure_test_sharingAndModifySharing():
        (projectName, evaluationName) = ("Teamwork2", "Week 2")
        (metagroupName, groupName) = ("b", "F")
        (ratinglevel, checkbox1, checkbox2, checkbox3) = ("Rarely", False,True,True)
        return (projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3)
        

class TestSharing(unittest.TestCase):

    def test_1_SignUp_Existed(self):
        #sign up
        testSignUp = SignUp()
        (username, password) = Configure.configure_test_1_successOrExisted()
        (urlCurrent, alertInfo) = testSignUp.sign_up(username, password)
      
    def test_2_CreateProject_Success(self):
        #create project        

        (username, password, projectname, projectdescription, studentFile, jsonFile) = Configure.configure_test_3_CreateProject_Success()
        createP = CreateProject()
        
        (urlCurrent, alertInfo)= createP.create_project_attempt(username, password, projectname, projectdescription, studentFile, jsonFile)

        
    
    def test_3_Evaluations(self):
        #create evalution
        
        (username, password, projectName, evaluationName) = Configure.configure_test_Evaluations()
        createE = Evaluation()
        
        (projectURL, alertInfo) = createE.create_evaluation_attempt(username, password, projectName, evaluationName)
   
    
    def test_4_RatingTwoGroups(self):
        # select one group to rate; then select the 2nd group to rate

        (username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3) = Configure.configure_test_Rating()
        
        createR = Rating()
        (statusA, statusB, statusC) = createR.rating_one_group(username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3)
        if checkbox1: self.assertTrue(statusA)
        if checkbox2: self.assertTrue(statusB)
        if checkbox3: self.assertTrue(statusC)
        
        #rate another group
        createR = Rating()
        (username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3) = Configure.configure_test_Rating_Another_Group()
        (statusA, statusB, statusC) = createR.rating_one_group(username, password, projectName, evaluationName, metagroupName, groupName, level, checkbox1, checkbox2, checkbox3)
        if checkbox1: self.assertTrue(statusA)
        if checkbox2: self.assertTrue(statusB)
        if checkbox3: self.assertTrue(statusC)
    

    
    def test_7_sharingAndDelete(self):
        # share the project and then delete the sharing
        
        (username, password, shareToUser) = Configure.configure_test_sharingAndDelete()
        
        createS = Sharing()
        
        (successText, deleteText) = createS.sharingProjectAndDelete(username, password, shareToUser)
        IsSuccessText = successText == "Permission successfully created"
        IsDeleteText = deleteText == "successfully delete permission"
        
        
        self.assertTrue(IsSuccessText and IsDeleteText, deleteText)

    def test_8_sharingAndModifySharing(self):
        # share the project and modify the rating from the sharedUser
        
        (username, password, shareToUser, sharedUserPw) = ("instructor1@example.com", "abcdefgh", "ta@example.com", "abcdefgh")
                
        (projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3) = Configure.configure_test_sharingAndModifySharing()
        
        createS = Sharing()
        
        (statusA, statusB, statusC) = createS.sharingProjectAndCheck(username, password, shareToUser, sharedUserPw, projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3)
        

        if checkbox1: self.assertTrue(statusA)
        if checkbox2: self.assertTrue(statusB)
        if checkbox3: self.assertTrue(statusC)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    