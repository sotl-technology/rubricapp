import unittest
import time
import os
from signUpDriver import signUp
from createProjectDriver import createProject
from evaluationDriver import evaluation
from ratingDriver import rating
from sharingDriver import sharing

class configure:

    def configure_test_1_successOrExisted():
        (username, password) = ("instructor1@example.com", "abcdefgh")  
        return (username, password)
        
    def configure_test_3_CreateProject_Success():
        #both xlsx and json files have to be downloaded previously
        (username, password) = ("instructor1@example.com", "abcdefgh") 
        (projectname, projectdescription) =("Teamwork2", "A sample project using an ELPISSrubric for Teamwork2")  
        # (studentFile, jsonFile) = ("C:/Users/Wangj/Downloads/sample_roster.xlsx", "C:/Users/Wangj/Downloads/teamwork_scale3.json")     
        (studentFile, jsonFile) = (os.getcwd() + "/sample_roster.xlsx", os.getcwd() + "/teamwork_scale3.json")
        return (username, password, projectname, projectdescription, studentFile, jsonFile)


    def configure_test_Evaluations():
        (username, password) = ("instructor1@example.com", "abcdefgh") 
        (projectName, evaluationName) = ("Teamwork2", "Week 2")
        return (username, password, projectName, evaluationName)
    
    def configure_test_Rating():
        (username, password) = ("instructor1@example.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 2")
        groupName = "O"
        (level, checkbox1, checkbox2, checkbox3) = ("Sporadically", True,True,False)
        return (username, password, projectName, evaluationName,groupName, level, checkbox1, checkbox2, checkbox3)


    def configure_test_Rating_Another_Group():
        (username, password) = ("instructor1@example.com", "abcdefgh")
        (projectName, evaluationName) = ("Teamwork2", "Week 2")
        switchGroup = "F"
        (level, checkbox1, checkbox2, checkbox3) = ("Frequently", False, False, True) 
        return (username, password, projectName, evaluationName, switchGroup, level, checkbox1, checkbox2, checkbox3)
        
    # def configure_test_attendance():
        # (username, password) = ("instructor1@example.com", "abcdefgh")
        # (projectName, evaluationName) = ("Teamwork2", "Week 2")
        # studentGroup = "O"
        # studentNameToCheck = "Wickens, Hebe"
        
        # return (username, password, projectName, evaluationName, studentGroup, studentNameToCheck)    
    
    def configure_test_sharingAndDelete():
        (username, password, shareToUser) = ("instructor1@example.com", "abcdefgh", "ta@example.com")
        return (username, password, shareToUser)
        
    def configure_test_sharingAndModifySharing():
        (projectName, evaluationName) = ("Teamwork2", "Week 2")
        groupName = "F"
        (ratinglevel, checkbox1, checkbox2, checkbox3) = ("Rarely", False,True,True)
        return (projectName, evaluationName,groupName, ratinglevel, checkbox1, checkbox2, checkbox3)
        

class TestSharing(unittest.TestCase):
    
    def test_1_SignUp_Existed(self):
        #If this is not the first time of running this code, then the username would be existed
        
        testSignUp = signUp()
        print("\n\nTesting SignUp\n\n") 
        
        (username, password) = configure.configure_test_1_successOrExisted() 
        (urlCurrent, alertInfo) = testSignUp.Driver_SignUp(username, password)
        
        testSignUp.Close()

      
    
      
    def test_2_CreateProject_Success(self):
        #if first time run, this test will create a project; if not the first time, there won't be duplicate projects created
        
        print("\n\nTesting createProject\n\n")  #somehow this is not printed
        

        (username, password, projectname, projectdescription, studentFile, jsonFile) = configure.configure_test_3_CreateProject_Success()
        createP = createProject()
        
        (urlCurrent, alertInfo)= createP.createProject_attempt(username, password, projectname, projectdescription, studentFile, jsonFile)
        
        createP.Close()
        
    
    def test_3_Evaluations(self):
        # This evaluation will test for either successfully creating evaluation or fail due to existed evaluation name

        (username, password, projectName, evaluationName) = configure.configure_test_Evaluations()
        createE = evaluation()
        
        (projectURL, alertInfo) = createE.driver_createEvaluation_attempt(username, password, projectName, evaluationName)
        createE.Close()
        
    
    
    
    def test_4_Rating_One_Group(self):
        # Here is only my hardcoding work
        # due to Out-Of-Index problem, I created a new rubric called "Teamwork1" with one evalution as "Week 2"
        # in addition, almost all the elements on the page is associated with my userid and the time of the creation of the evaluation
        

        (username, password, projectName, evaluationName, groupName, level, checkbox1, checkbox2, checkbox3) = configure.configure_test_Rating()
        
        createR = rating()        
        (projectURL, metaGroupURL, statusA, statusB, statusC) = createR.driver_Rating_One_Group(username, password, projectName, evaluationName, groupName, level, checkbox1, checkbox2, checkbox3)
        createR.Close()
        
        # IsProject = projectURL == "http://localhost:5000/load_project/instructor1@example.cominstructor1@example.comTeamwork1full/noAlert"
        
        # IsMetaGroup = metaGroupURL == "http://localhost:5000/jump_to_evaluation_page/instructor1@example.cominstructor1@example.comTeamwork1full/Week%201/b/***None***/noAlert"
 
        #self.assertTrue(IsProject and IsMetaGroup)
        if checkbox1: self.assertTrue(statusA)
        if checkbox2: self.assertTrue(statusB)
        if checkbox3: self.assertTrue(statusC)
    
    
    
    def test_5_Rating_Another_Group(self):
        # Here is only my hardcoding work
        # due to Out-Of-Index problem, I created a new rubric called "Teamwork1" with one evalution as "Week 2"
        # in addition, almost all the elements on the page is associated with my userid and the time of the creation of the evaluation
        

        (username, password, projectName, evaluationName, switchGroup, level, checkbox1, checkbox2, checkbox3) = configure.configure_test_Rating_Another_Group()
        
        createR = rating()        
        (projectURL, metaGroupURL, secondGroupURL, statusA, statusB, statusC) = createR.driver_Switch_and_Rate_Another_Group(username, password, projectName, evaluationName, switchGroup, level, checkbox1, checkbox2, checkbox3)
        createR.Close()
        
        # IsProject = projectURL == "http://localhost:5000/load_project/instructor1@example.cominstructor1@example.comTeamwork1full/noAlert"
        
        # IsMetaGroup = metaGroupURL == "http://localhost:5000/jump_to_evaluation_page/instructor1@example.cominstructor1@example.comTeamwork1full/Week%201/b/***None***/noAlert"
        
        # IsSecondGroup = secondGroupURL == "http://localhost:5000/jump_to_evaluation_page/instructor1@example.cominstructor1@example.comTeamwork1full/Week%201/b/O/Connected%20to%20groupO"
        
        # self.assertTrue(IsProject and IsMetaGroup and IsSecondGroup)
        self.assertTrue(statusC)
    
    

    
    def test_7_sharingAndDelete(self):
        
        # (username, password, shareToUser) = ("instructor1@example.com", "abcdefgh", "ta@example.com")
        (username, password, shareToUser) = configure.configure_test_sharingAndDelete()
        
        createS = sharing()
        
        (successText, deleteText) = createS.sharingProjectAndDelete(username, password, shareToUser)
        IsSuccessText = successText == "Permission successfully created"
        IsDeleteText = deleteText == "successfully delete permission"
        
        
        self.assertTrue(IsSuccessText and IsDeleteText, deleteText)
       
    def test_8_sharingAndModifySharing(self):
        (username, password, shareToUser, sharedUserPw) = ("instructor1@example.com", "abcdefgh", "ta@example.com", "abcdefgh")
        
        
        
        (projectName, evaluationName,groupName, ratinglevel, checkbox1, checkbox2, checkbox3) = configure.configure_test_sharingAndModifySharing()
        
        createS = sharing()
        
        (statusA, statusB, statusC) = createS.sharingProjectAndCheck(username, password, shareToUser, sharedUserPw, projectName, evaluationName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3)
        

        if checkbox1: self.assertTrue(statusA)
        if checkbox2: self.assertTrue(statusB)
        if checkbox3: self.assertTrue(statusC)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    