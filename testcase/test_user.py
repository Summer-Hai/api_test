#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/9 14:34
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : test_user.py
# @Software: PyCharm
import allure
import pytest

from api.user import User
from common.get_log import log


@allure.epic("企业微信后台接口自动化测试")
@allure.feature("成员信息数据模块")
class TestUser():

    user = User()
    access_token = user.get_token()
    user_id = user.load_yaml('datas/user/get_user_data.yml', 'data')
    user_data = user.load_yaml('datas/user/create_user_data.yml', 'data')
    userid_data = user.load_yaml('datas/user/batchdelete_user_data.yml', 'data')
    simplelist_data = user.load_yaml('datas/user/simplelist_data.yml', 'data')


    @allure.story("添加成员信息")
    @pytest.mark.parametrize('userid,name,department,mobile,email,ids', user_data)
    def test_create_user(self, userid, name, department, mobile, email, ids):

        log.info("-------开始测试创建成员信息查询接口数据-------")
        res = self.user.create_user(userid, name, department, mobile, email, self.access_token)
        log.info(f"打印响应结果: code: {res['errcode']}, msg: {res['errmsg']}")
        # assert ids in res['errmsg']
        log.info("-------测试结束-------")



    @allure.story("成员信息查询")
    @pytest.mark.parametrize('userid', user_id)
    def test_get_user(self, userid):

        log.info("-------开始测试获取成员信息查询接口数据-------")
        res = self.user.get_user(userid, self.access_token)
        assert userid == res['userid']
        log.info(f"打印响应结果: code: {res['errcode']}, msg: {res['errmsg']}")
        log.info("-------测试结束-------")


    @allure.story("删除成员信息")
    @pytest.mark.parametrize('userid', user_id)
    def test_delete_user(self, userid):

        log.info("-------开始测试删除成员信息查询接口数据-------")
        res = self.user.delete_user(userid, self.access_token)
        log.info(f"打印响应结果: code: {res['errcode']}, msg: {res['errmsg']}")
        assert res['errmsg'] == 'deleted'
        log.info("-------测试结束-------")


    @allure.story("批量删除成员信息")
    @pytest.mark.parametrize('userid1,userid2', userid_data)
    def test_batchdelete_user(self, userid1, userid2):

        log.info("-------开始测试批量删除成员信息查询接口数据-------")
        res = self.user.batchdelete_user(userid1, userid2, self.access_token)
        log.info(f"打印响应结果: code: {res['errcode']}, msg: {res['errmsg']}")
        assert res['errmsg'] == 'deleted'
        log.info("-------测试结束-------")

    @allure.story("获取部门成员信息")
    @pytest.mark.parametrize('department_id,fetch_child', simplelist_data)
    def test_simplelist_user(self, department_id, fetch_child):

        log.info("-------开始测试获取部门成员信息接口数据-------")
        res = self.user.simplelist_user(department_id, fetch_child, self.access_token)
        log.info(f"打印响应结果: code: {res['errcode']}, msg: {res['errmsg']}")
        assert res['userlist'][0]['userid'] == 'LiHaiQiang'
        log.info("-------测试结束-------")





