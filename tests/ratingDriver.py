
from selenium.webdriver import Chrome
from loginDriver import LogIn

import time



class Rating:
    def __init__(self):
        self.driver = Chrome()
    
    def Close(self):
        self.driver.quit()
    
    def getTimeCreationOfEvaluation(self):
        html = self.driver.page_source        
        str1 = "grade by"
        a = html.find(str1)
        timeCreation = html[(a-21):(a-2)]
        return timeCreation
    
    def usernameToCssUsername(username):
        css = "#"
        for s in username:
            if s == '@':
                css = css + "\@"
            elif s == ".":
                css = css + "\."
            else:
                css = css + s
        return css
    
    def getCssUsernameAndTimeCreateOfEvaluation(self, username):
        # both css-username and creation time are used for locating elements
        
        #get time creation of the evaluation
        timeCreation = Rating.getTimeCreationOfEvaluation(self)
        #set username in css format
        css = Rating.usernameToCssUsername(username)
        return (timeCreation, css)
    
    
    
    def rateInteractingLevel(self, css, timeCreation, level):
        switcher = {
            "N/A"         : "1",
            "No evidence" : "2",
            "Rarely"      : "3",
            "Sporadically": "4",
            "Frequently"  : "5"
        }
        self.driver.find_element_by_css_selector(css + timeCreation + "\|Interacting0 .w3-parallel-box:nth-child(" 
                  + switcher.get(level, "None") + ") .L-labels").click()
    
    def rateInteractingCheckbox(self, username, timeCreation, choice):
        #choice is limited to "a", "b", "c"
        rate = self.driver.find_element_by_id(username + timeCreation + "|Interacting|Observed Characteristics|" + choice)
        
        if not rate.is_selected():
            rate.click()
        status =  rate.is_selected()
        return status
    
    
    def rateInteracting(self, css, username, timeCreation, level, choice1=False, choice2=False, choice3=False):
        #Rate the level in Interacting category - here the choice is "Sporadically"
        
        # click the dropdown for rating Interacting:
        self.driver.find_element_by_css_selector("#Interacting\|" + css[1:] + timeCreation +"\|panel-heading .cateNames").click()
        
        #Rate the level
        Rating.rateInteractingLevel(self, css, timeCreation, level)
        
        #Rate the checkboxes:
        status1=status2=status3 = False
        #here rate checkbox "a"
        if choice1:   status1 = Rating.rateInteractingCheckbox(self, username, timeCreation, "a")
        #here rate checkbox "b"
        if choice2:   status2 = Rating.rateInteractingCheckbox(self, username, timeCreation, "b")
        #here rate checkbox "c"
        if choice3:   status3 = Rating.rateInteractingCheckbox(self, username, timeCreation, "c")
        
        #Save the rating
        self.driver.find_element_by_id("button").click()
        self.driver.implicitly_wait(5)

        return (status1, status2, status3)
    
    def switchGroup(self, groupName):
        
        # For now (0425) there is an issue - duplicate code existing on rating page.
        self.driver.find_elements_by_css_selector("#" + groupName +"> li")[1].click()

        self.driver.switch_to.alert.accept()
    
    def selectProject(self, projectName):
        self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text(projectName))
        self.driver.implicitly_wait(5)
    
    def selectEvaluation(self, metagroupName): 
        self.driver.find_element_by_link_text(metagroupName).click()  
        self.driver.implicitly_wait(5)
    
    def Rate_Group(self, username, password, projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1=False, checkbox2=False, checkbox3=False):
        # rate group as desired. For now it's limited to rate "Interacting" only
        
        #Select evaluation and the metagroup to rate  
        Rating.selectEvaluation(self, metagroupName)
        self.driver.implicitly_wait(5)
        
        #select group to rate
        Rating.switchGroup(self, groupName)
        
        # obtain creation time of the evaluation, and css version of username for locating element
        (timeCreation, css) = Rating.getCssUsernameAndTimeCreateOfEvaluation(self, username)
        
        #Rate the interacting category
        (statusA, statusB, statusC) = Rating.rateInteracting(self, css, username, timeCreation, ratinglevel, checkbox1, checkbox2, checkbox3)
        
        return (statusA, statusB, statusC)
    
    
    def Rating_One_Group(self, username, password, projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1=False, checkbox2=False, checkbox3=False):
        
        #login
        LogIn.Login(self, username, password)

        # Select project
        Rating.selectProject(self, projectName)
        
        # Rate group
        (statusA, statusB, statusC) = Rating.Rate_Group(self, username, password, projectName, evaluationName, metagroupName, groupName, ratinglevel, checkbox1, checkbox2, checkbox3)
        
        Rating.Close(self)
        return (statusA, statusB, statusC)
        
        
    def test_attendance(self, username, password, projectName, evaluationName, metagroupName, groupName, studentNameToCheck):
        #login
        LogIn.Login(self, username, password)
        
        # Select project
        Rating.selectProject(self, projectName)
        
        #Select evaluation and the metagroup to rate  
        Rating.selectEvaluation(self, metagroupName)
        
        #Select the group to rate
        Rating.switchGroup(self, groupName)
        
        # Expand the "attendance" dropdown
        self.driver.find_element_by_css_selector("body > div.middle > div.middle-left > div:nth-child(2) > button:nth-child(5)").click()
        
        # Check the attendance for the student in the argument
        # For now (0425) there is an issue - duplicate code existing on rating page.
        responseList = self.driver.find_elements_by_xpath("//input[@value='" + studentNameToCheck + "']")
        self.driver.implicitly_wait(5)
        response = responseList[1]  
        
        if not response.is_selected():
            response.click()
        self.driver.find_element_by_id("AttendenceButton").click()
        self.driver.implicitly_wait(5)
        isResponse = response.is_selected()
        
        Rating.Close(self)
        
        return isResponse
        
        
        






    
        

    