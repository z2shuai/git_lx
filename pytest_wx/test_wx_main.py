from time import sleep

import yaml

from pytest_1.test_wx_page.index import IndexPage
import pytest


class TestWx():

    @pytest.mark.parametrize('name,user,phone',yaml.safe_load(open('./data.yml')))
    # @pytest.mark.parametrize('name,user,phone',
    #                          [['zgd_gd2131', 'gd01210131', 14100992399], ['zgd_gd2232', 'gd01020132', 14120993299]])
    def test_addmember(self, name, user, phone, lindex):
        lindex.click_addmember()
        sleep(1)
        lindex.set_member(name, user, phone)


    @pytest.mark.parametrize('name,user,phone', yaml.safe_load(open('./data.yml')))
    def test_assert_name(self, name, user, phone, lindex):
        assert name == lindex.get_member(name)
        # sleep(1)

