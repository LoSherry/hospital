import logging

from flask import g

from rptserver.database.sqlal import func_to_char
from rptserver.model.sample import SampleStore, SampleUse

class SampleService(object):
    
    def qry_sample_store_by_id(self, cfid):
        """通过存放id获取信息

        Args:
            id (_type_): 存放id
        """
        
        query = g.db_session.query(SampleStore).filter(SampleStore.cfid == cfid)
        rst = None
        if query.count() > 0:
            rst = query.first()
        return rst
    
    def qry_sample_use_by_id(self, qyid):
        """通过取用编号获得样本信息

        Args:
            id (_type_): 取用编号
        """
        query = g.db_session.query(SampleUse).filter(SampleUse.qyid == qyid)
        rst = None
        if query.count() > 0:
            rst = query.first()
        return rst