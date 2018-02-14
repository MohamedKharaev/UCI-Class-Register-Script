##TODO

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def open_webreg() -> None:
    '''Creates an automated Chrome browser and goes to the webreg website'''
    global driver
    driver = webdriver.Chrome(executable_path = "chromedriver.exe")
    driver.get("https://www.reg.uci.edu/cgi-bin/webreg-redirect.sh")
    
def login_webreg(login: str, passw: str) -> None:
    '''Inputs the userid and password until the user successfuly logs in'''
    global driver
    ucinetid = driver.find_element_by_id('ucinetid')
    ucinetid.clear()
    ucinetid.send_keys(login)
    password = driver.find_element_by_id('password')
    password.clear()
    password.send_keys(passw)
    password.send_keys(Keys.RETURN)
    if 'Quarter Menu' not in driver.page_source:
        ActionChains(driver).click(driver.find_element_by_xpath("/html/body/center[1]/table[@id='webreg-login-box']/tbody/tr/td/center/form/input")).perform()
        login_webreg(login, passw)
        
def enter_enrollment_menu() -> None:
    '''Navigates the Chrome browser to the enrollment menu page'''
    global driver
    enrollmenu = driver.find_element_by_xpath("/html/body/center[1]/table[@class='WebRegNavBar']/tbody/tr/td[@class='vertButtons']/form[1]/input[@class='WebRegButton']")
    enrollmenu.send_keys(Keys.RETURN)

    
def add_or_del_class(class_code: str, status: str):
    '''Adds or deletes a class code to the user's schedule. Status will either be "add" or "del"'''
    global driver
    coursecode = driver.find_element_by_xpath("/html/body/center[1]/form[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input")
    coursecode.clear()
    coursecode.send_keys(class_code)
    status = driver.find_element_by_xpath("/html/body/center[1]/form[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/input[@id='add']") \
                if status == 'add' else driver.find_element_by_xpath("/html/body/center[1]/form[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/input[@id='drop']")
    sendrequest = driver.find_element_by_xpath("/html/body/center[1]/form[2]/table/tbody/tr[1]/td/input[3]")
    ActionChains(driver).click(status).click(sendrequest).perform()


def add_all_classes(classes: [[int]]) -> int:
    '''Adds the list of classes the user inputed into the main classes section. The returned value is the amount of classes that failed to be added'''
    global driver
    aclass_counter = 0
    for c in classes:
        current_counter = aclass_counter
        for class_code in c:
            if class_code != '':
                add_or_del_class(class_code, 'add')
                if 'You have TENTATIVELY ADDED' not in driver.page_source and 'you have added' not in driver.page_source:
                    if current_counter == aclass_counter:
                        aclass_counter += 1
                    for class_code in c:
                        if class_code != '':
                            add_or_del_class(class_code, 'remove')
                    break
    return aclass_counter
    
def add_all_alt_classes(aclasses: [[int]], aclass_counter: int):
    '''Adds aclass_counter amount of classes from the alternate classes list'''
    global driver
    for ac in aclasses:
        current_counter = aclass_counter
        if aclass_counter != 0:
            all_added = True
            for class_code in ac:
                if class_code != '':
                    add_or_del_class(class_code, 'add')
                    if 'You have TENTATIVELY ADDED' not in driver.page_source and 'you have added' not in driver.page_source:
                        all_added = False
                        for class_code in ac:
                            if class_code != '':
                                add_or_del_class(class_code, 'remove')
                        break
                if all_added:
                    aclass_counter -= 1

    
    
    
