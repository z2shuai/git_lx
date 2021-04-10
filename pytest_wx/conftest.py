import pytest
from pytest_1.test_wx_page.index import IndexPage

@pytest.fixture(scope='class')
def lindex():
    print("实例化初始页面")
    page = IndexPage().goto_member()
    yield page
    print("实例化结束")

