#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/02/16 11:22
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : user.py
# @Software: PyCharm
import os

from api.base_api import BaseApi
from common.config import cf
from common.get_log import log


class User(BaseApi):

    """
        实现了所有公共类API的需要的东西,是其他API的父类

        ip：测试环境的ip地址
        Base_Path：项目的根路径
        """

    # 通过配置文件获取测试的环境的ip地址
    ip = cf.get_key("test_env", "formal_ip")
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = 'datas/user/user.yml'


    def get_user(self, userid, access_token):
        """
        用户信息查询
        :param p_data: 用户信息查询接口参数
        :param path: 用户信息查询接口模板
        """
        log.info(f'传入参数：{userid}')
        p_data = {
            'userid': userid, 'ip': self.ip, 'access_token': access_token
        }
        res = self.send_api_data(self.path, p_data, 'get_user')

        return res


    def create_user(self, userid, name, department, mobile, email, access_token):

        p_data = {
            'userid': userid, 'name': name, 'mobile': mobile, 'email': email, 'ip': self.ip,
            'department': department, 'access_token': access_token
        }
        res = self.send_api_data(self.path, p_data, 'add_user')

        return res

    def delete_user(self, userid, access_token):


        p_data = {
            'userid': userid, 'access_token': access_token, 'ip': self.ip
        }
        res = self.send_api_data(self.path, p_data, 'delete_user')

        return res

    def batchdelete_user(self, userid1, userid2, access_token):

        p_data = {
            'userid1': userid1, 'userid2': userid2, 'ip': self.ip, 'access_token': access_token
        }
        res = self.send_api_data(self.path, p_data, 'batchdelete')

        return res

    def simplelist_user(self, department_id, fetch_child, access_token):


        p_data = {
            'ip': self.ip, 'department_id': department_id, 'access_token': access_token, 'fetch_child': fetch_child
        }
        res = self.send_api_data(self.path, p_data, 'simplelist')

        return res






