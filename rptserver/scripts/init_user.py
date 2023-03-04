# -*- coding:utf-8 -*-
import logging
from faker import Faker

from ..model.user import User
from ..tools.utils import to_md5


fake = Faker(locale=['zh_CN'])


def init_user(session):
    """ 初始化用户
    :param session:
    """
    logging.info("User Info Init.")
    logging.info("清理用户历史数据...")
    session.query(User).delete()  
    
    user_list = []
    for i in range(10):
        user= User(**{
            'admin' : "admin" + str(i),
            'name': fake.name(),
            'password': to_md5('123456'),
            'status': '正常',
        })
        
        user_list.append(user)
    
    session.add_all(user_list)
    session.commit()