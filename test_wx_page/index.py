from selenium.webdriver.common.by import By

from pytest_1.test_wx_page.addmember import AddmemberPage
from pytest_1.test_wx_page.base_page import Base


class IndexPage(Base):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    def goto_addmember(self):
        self.find_element(By.CSS_SELECTOR, '.index_service_cnt.js_service_list>a:nth-child(1)').click()
        return AddmemberPage(self.driver)

    def goto_member(self):
        self.find_element(By.ID,'menu_contacts').click()
        return AddmemberPage(self.driver)
