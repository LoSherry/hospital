# -*- coding:utf-8 -*-
'''
'''
import datetime

from sqlalchemy import BigInteger, String, DateTime, Text, Boolean, Column, Sequence, ForeignKey, UniqueConstraint
from sqlalchemy.orm import backref, relationship

from rptserver.database.sqlal import Base

class User(Base):
    '''用户'''
    __tablename__ = 'user'
    id = Column(BigInteger,  primary_key=True)
    admin = Column(String(64), unique=True, doc='用户号')
    name = Column(String(512), doc='用户姓名')
    password = Column(String(256), doc='密码')
    status = Column(String(32), doc='状态:正常，停用，休假')