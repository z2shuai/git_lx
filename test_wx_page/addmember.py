from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pytest_1.test_wx_page.base_page import Base


class AddmemberPage(Base):
    def click_addmember(self):
        locator = (By.CSS_SELECTOR, '.ww_operationBar:nth-child(1)>a:nth-child(2)')

        def wait_for_next(x):
            try:
                x.find_element(*locator).click()
                return self.find_element(By.ID, 'username')
            except:
                return False

        self.wait.until(wait_for_next)

    def set_member(self, name, user, phone):
        # 添加联系人
        self.find_element(By.ID, 'username').send_keys(name)
        self.find_element(By.ID, 'memberAdd_acctid').send_keys(user)
        self.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find_element(By.CSS_SELECTOR, '.member_colRight_operationBar.ww_operationBar:nth-child(1)>a').click()

    def get_member(self, value):
        self.find_element(By.CSS_SELECTOR, '.jstree-anchor.jstree-clicked').click()
        total_list = []
        while True:
            # sleep(0.1)
            eles = self.find_elements(By.CSS_SELECTOR, 'tr>.member_colRight_memberTable_td:nth-child(2)')
            eleList = [ele.get_attribute('title') for ele in eles]
            total_list += eleList
            if value in total_list:
                return value
            result: str = self.find_element(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = result.split('/')
            if int(num) == int(total):
                return value
            else:  # 点击下一页
                self.find_element(By.CSS_SELECTOR,'.js_next_page').click()
