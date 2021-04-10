from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains,TouchActions
from selenium.webdriver.support import expected_conditions as Ec


class Base():
    # driver: WebDriver
    base_url = ''
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            self.option = webdriver.ChromeOptions()
            self.option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=self.option)
        else:
            self.driver = driver

        self.wait = WebDriverWait(self.driver,10)
        self.chains = ActionChains(self.driver)
        self.touch = TouchActions(self.driver)
        self.driver.implicitly_wait(5)
        if self.base_url != '':
            self.driver.get(self.base_url)
    def find_element(self,by,ele):
        return self.wait.until(Ec.presence_of_element_located((by,ele)))

    def find_elements(self,by,ele):
        return self.wait.until(Ec.presence_of_all_elements_located((by,ele)))