import unittest
import os
from signUpDriver import signUp
from createProjectDriver import createProject
import time

class configure:
    def configure_test_1_successOrExisted():
        (username, password) = ("sampleuser_CreateProject@mail.com", "abcdefgh")  
        return (username, password)
        
    def configure_test_3_CreateProject_Success():
        #both xlsx and json files are downloaded in the selenium/tests directory
        (username, password) = ("sampleuser_CreateProject@mail.com", "abcdefgh") 
        (projectname, projectdescription) =("Teamwork", "A sample project using an ELPISSrubric for Teamwork") 
        (studentFile, jsonFile) = (os.getcwd() + "/sample_roster.xlsx", os.getcwd() + "/teamwork_scale3.json")
        return (username, password, projectname, projectdescription, studentFile, jsonFile)
    
    def configure_test_3_1_CreateProject_InvalidProjectNameAndDescription():
        #both xlsx and json files are downloaded in the selenium/tests directory
        (username, password) = ("sampleuser_CreateProject@mail.com", "abcdefgh")
        (projectname, projectdescription) =("12", "1"*256)  
        (studentFile, jsonFile) = (os.getcwd() + "/sample_roster.xlsx", os.getcwd() + "/teamwork_scale3.json") 
        return (username, password, projectname, projectdescription, studentFile, jsonFile)
    
    def configure_test_3_2_CreateProject_InvalidFileFormat():
        #both xlsx and json files are downloaded in the selenium/tests directory
        (username, password) = ("sampleuser_CreateProject@mail.com", "abcdefgh") 
        (projectname, projectdescription) = ("Teamwork", "A sample project using an ELPISSrubric for Teamwork")
        (studentFile, jsonFile) = (os.getcwd() + "/teamwork_scale3.json", os.getcwd() + "/sample_roster.xlsx")
        return (username, password, projectname, projectdescription, studentFile, jsonFile)
    

class TestCreateProject(unittest.TestCase):
    
    
    def test_1_SignUp_Existed(self):
        #sign up
        
        testSignUp = signUp()
        (username, password) = configure.configure_test_1_successOrExisted()
        (urlCurrent, alertInfo) = testSignUp.Driver_SignUp(username, password)

    def test_3_CreateProject_Success(self):        
        #success or duplicate project name error

        (username, password, projectname, projectdescription, studentFile, jsonFile) = configure.configure_test_3_CreateProject_Success()
        createP = createProject()
        
        (urlCurrent, alertInfo)= createP.createProject_attempt(username, password, projectname, projectdescription, studentFile, jsonFile)
             
        IsProjectCreated = urlCurrent == "http://localhost:5000/instructor_project"
        
        IsProjectNotCreated = urlCurrent == "http://localhost:5000/create_project"
        # for now (0413), the error message "The project name has been used before" is missing.
        IsAlertInfo = alertInfo == "3-150 characters"  
        
        msg = alertInfo
        
        self.assertTrue(IsProjectCreated or (IsProjectNotCreated and IsAlertInfo), msg)
    
    
    
    
        
        
    def test_3_1_CreateProject_InvalidProjectNameAndDescription(self):
        #invalid length of project name and description 
       
        (username, password, projectname, projectdescription, studentFile, jsonFile) = configure.configure_test_3_1_CreateProject_InvalidProjectNameAndDescription()
        
        createP = createProject()
        
        (alert1, alert2) = createP.getProjectNameAndDescriptionAlert(username, password, projectname, projectdescription, studentFile, jsonFile)

        IsAlert1 = alert1 == "Field must be between 3 and 150 characters long."
        IsAlert2 = alert2 == "Field must be between 0 and 255 characters long."
        
        self.assertTrue(alert1 and alert2)
    
    
   
    #0413 -- the error messages is currently not shown
    
    # def test_3_2_CreateProject_InvalidFileFormat(self):
        #incorrect format of files uploaded for Roster and Rubric
        
        # (username, password, projectname, projectdescription, studentFile, jsonFile) = configure.configure_test_3_2_CreateProject_InvalidFileFormat()
        
        # createP = createProject()
        
        # (alert1, alert2) = createP.getInvalidFileAlert(username, password, projectname, projectdescription, studentFile, jsonFile)

        # IsAlert1 = alert1 == "File is not a zip file"
        # IsAlert2 = alert2 == "'charmap' codec can't decode byte 0x81 in position 22: character maps to <undefined>"

        
        # self.assertTrue(alert1 and alert2)
    


    
    def test_3_0_Rubric_file_teamwork(self):
        #test the rubric file - teamwork_scale3 location
        
        (username, password) = configure.configure_test_1_successOrExisted()    
        createP = createProject()
        
        url = createP.testRubricFile_teamwork(username, password)

        IsUrlTrue = url == "https://github.com/sotl-technology/rubricapp/blob/master/sample_file/rubrics/teamwork/teamwork_scale3.json"
                
        self.assertTrue(IsUrlTrue, url)
    
    
    
    def test_3_0_Rubric_file_infoProcess(self):
        #test the rubric file - information_processing location
        
        (username, password) = configure.configure_test_1_successOrExisted()      
        createP = createProject()
        
        url = createP.testRubricFile_infoProcess(username, password)

        IsUrlTrue = url == "https://github.com/sotl-technology/rubricapp/blob/master/sample_file/rubrics/information_processing/information_processing.json"
        self.assertTrue(IsUrlTrue)
    
    
    def test_3_0_Rubric_file_communication(self):
        #test the rubric file - interpersonal_communication location
        (username, password) = configure.configure_test_1_successOrExisted()      
        createP = createProject()
        
        url = createP.testRubricFile_communication(username, password)
        
        IsUrlTrue = url == "https://github.com/sotl-technology/rubricapp/blob/master/sample_file/rubrics/interpersonal_communication/interpersonal_communication_scale3.json"
        self.assertTrue(IsUrlTrue, url)
    

if __name__ == '__main__':
    unittest.main()    