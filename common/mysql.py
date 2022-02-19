#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/02/16 11:22
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : mysql.py
# @Software: PyCharm
import pymysql

from common.config import cf
from common.get_log import log


class Mysql():

    """
    操作mysql的类
    """

    def __init__(self):
        """
        初始化mysql的conn对家，连接数据库
        """
        # 通过配置文件获取数据库的host，port，username，password，charset，database
        host = cf.get_key("mysql", "host")
        # 从配置文件获取的值是str，需要转化成int
        port = int(cf.get_key("mysql", "port"))
        user = cf.get_key("mysql", "user")
        password = cf.get_key("mysql", "password")
        charset = cf.get_key("mysql", "charset")
        database = cf.get_key("mysql", "database")
        # 当无法连接数据库，走异常处理处理
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user,
                                        password=password, charset=charset, database=database)
        except Exception as e:
            log.error(f"无法登陆数据库，错误原因：{e}")


    def select(self, query):
        """
        运行mysql的select语句
        :param query: select语句
        :return: select_data：返回全部的select语句的数据
        """
        log.info(f"select语句为：{query}")
        try:
            # 定义游标，并通过execute执行sql语句
            cur = self.conn.cursor()
            cur.execute(query)
            # fetchall读取游标中的所有select数据
            select_data = cur.fetchall()
            log.info("数据查询成功")
            # 返回select数据
            print(select_data)
            return select_data
        except Exception as e:
            log.error(f"select语句错误，错误原因是：{e}")

    def insert(self, query):
        """
        运行mysql的select语句
        :param query: insert语句
        """
        log.info(f"insert语句为：{query}")
        try:
            # 定义游标，并通过execute执行insert语句
            cur = self.conn.cursor()
            cur.execute(query)
            # insert执行成功后commit提交数据
            cur.execute("commit")
            log.info(f"数据插入成功")
        except Exception as e:
            log.error(f"insert 语句错误，原因是{e}")
            # insert失败后rollback回滚数据
            cur.execute("rollback")

    def update(self, query):
        """
        运行mysql的update语句
        :param query: update语句
        """
        log.info(f"update语句为：{query}")
        try:
            # 定义游标，并通过execute执行update语句
            cur = self.conn.cursor()
            cur.execute(query)
            # update执行成功后commit提交数据
            cur.execute("commit")
            log.info(f"数据更新成功")
        except Exception as e:
            log.error(f"update 语句错误，原因是{e}")
            # update失败后执行rollback回滚数据
            cur.execute("rollback")

    def delete(self, query):
        """
        运行mysql的delete语句
        :param query: delete语句
        """
        log.info(f"delete语句为：{query}")
        try:
            # 定义游标，并通过execute执行delete语句
            cur = self.conn.cursor()
            cur.execute(query)
            # delete执行成功后commit提交数据
            cur.execute("commit")
            log.info("数据删除成功")
        except Exception as e:
            log.error(f"delete语句失败，原因：{e}")
            # delete失败后rollback回滚数据
            cur.execute("rollback")

# 定义对象为单例模式，其他模块可方便使用
sql = Mysql()

if __name__ == '__main__':
    select = "select * from ad_agent where name = '海南光一'"
    insert = "INSERT INTO `python14`.`ad_agent`(`name`, `full_name`, `contact_person`, `contact_number`, `company_pay_id`, `type`, `custody_rate`) VALUES ('海南星嘉', '海南星嘉网络科技有限公司', NULL, NULL, 1, 1, NULL);"
    delete = "delete from ad_agent where id = 26"
    update = "UPDATE `python14`.`ad_agent` SET `name` = '测试', `full_name` = '白云深处有人家', `contact_person` = NULL, `contact_number` = NULL, `company_pay_id` = 1, `type` = 1, `custody_rate` = NULL WHERE `id` = 24;"
    sql.select(select)
    # sql.insert(insert)
    # sql.update(update)
    sql.delete(delete)