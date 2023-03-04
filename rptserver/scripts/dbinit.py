# -*- coding:utf-8 -*-
"""
初始化数据库
"""
import logging

from rptserver.database.sqlal import simple_session
from rptserver.scripts.init_user import init_user
def dbinit():
    """ 初始化数据库

    :param bool dev:是否为开发环境
    """
    session = simple_session()
    
    logging.info("生成用户表")
    sql = """
        CREATE TABLE IF NOT EXISTS  `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin` varchar(64) DEFAULT NULL,
  `name` varchar(512) DEFAULT NULL,
  `password` varchar(512) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    # session.execute(sql)
    init_user(session)
    # init_patient(session)

if __name__ == "__main__":
    dbinit()