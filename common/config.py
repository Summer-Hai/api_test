#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/02/16 11:22
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : config.py
# @Software: PyCharm
import configparser
import os


class ConFigIni():

    """
    获取配置文件

    BASE_PATH: 获得当前项目的绝对路径
    config_file_path:获取当前配置文件的路径，相当于根路径
    """

    # 获得当前项目的绝对路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 获取当前配置文件的路径，相当于根路径,读取config.ini配置文件
    config_file_path = os.path.join(BASE_PATH, "config.ini")

    def __init__(self, file_path=config_file_path):
        '''
        定义一个配置文件的对象，默认一个文件路径，可自己补充其他路径
        :param file_path: 配置文件的绝对路径
        '''
        # 为了让写入文件的路径是唯一值，所以这样定义下来
        self.config_file_path = file_path
        # 定义配置文件对象
        self.cf = configparser.ConfigParser()
        # 读取配置文件
        self.cf.read(file_path)


    def get_key(self, section, option=None):
        """
        获取配置文件的value值
        :param section: 配置文件中section的值
        :param option: 配置文件中option的值
        :return value:  返回value的值
        """
        # cf对象的get方法获取value值
        value = self.cf.get(section, option)
        return value

    def set_value(self, section, option, value):
        """
        修改value的值
        :param section: 配置文件中section的值
        :param option: 配置文件中option的值
        :param value: 修改value的值
        :return: 无
        """
        # python内存先修改值
        self.cf.set(section, option, value)
        # 需要通过文件的方式写入才行，不然实体文件的值不会改变
        with open(self.config_file_path, "w+") as f:
            self.cf.write(f)

cf = ConFigIni()

if __name__ == '__main__':
    print(cf.get_key('test_env', 'formal_ip'))
    print(cf.get_key('test_env', 'username'))
    print(cf.get_key('test_env', 'password'))



