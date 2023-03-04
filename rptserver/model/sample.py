'''
sample
'''
import datetime

from sqlalchemy import Integer,Float, BigInteger, String, DateTime, Text, Boolean, Column, Sequence, ForeignKey, UniqueConstraint,Enum
from sqlalchemy.orm import backref, relationship

from rptserver.database.sqlal import Base

class SampleStore(Base):
    '''病人'''
    __tablename__ = 'sample_store_info'
    
    cfid = Column(BigInteger,  primary_key=True, name = '存放编号')
    ybid = Column(BigInteger,  name = '标本编码')
    ybnum = Column(Integer,  name = '样本量')
    ybhbh = Column(String(50), doc='样本盒编号',name = '样本盒编号')
    ybcfwz = Column(String(20), doc='样本存放位置',name = '样本存放位置')


class SampleUse(Base):
    '''病人'''
    __tablename__ = 'sample_use_info'
    
    qyid = Column(BigInteger,  primary_key=True, name = '取用编号')
    ybid = Column(BigInteger,  name = '标本编码')
    qyrq = Column(DateTime, doc="取用日期", name = '取用日期')

    qyr = Column(String(20), doc='取用人',name = '取用人')
    yt = Column(String(50), doc='用途',name = '用途')
    bz = Column(String(20), doc='备注',name = '备注')