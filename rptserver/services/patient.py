import logging

from flask import g
import pandas as pd
import numpy as np

from rptserver.database.sqlal import func_to_char
from rptserver.model.patient import Patient,PreviousHistory,recurrentDistantMetastasis,samplingRecurrenceMetastasisSpecimens,recorderInformation,peripheralBloodSampleSampling, gene21Detection,gene70Detection,genebrcaDetection, relapseInformation, postoperativeTreatment, patientMarryHistory,patientFollow, patientMenstruationHistory, surgicalPathologicalInfo,familyHistory, patientHistory, clinicalFeature
from rptserver.tools.utils import is_id_number, upload_excel
from pymysql.err import DataError

class PatientService(object):
    
    def query(self,pageNum=None, pageSize=10, **query_conds):
        
        query = g.db_session.query(Patient)
        
        for key, value in query_conds.items():
            model_column = getattr(Patient, key, None)
            if model_column and bool(value):
                if "CHAR" in str(model_column.type) or "TEXT" in str(model_column.type):
                    query = query.filter(getattr(Patient, key).contains(value))
                elif "DATE" in str(model_column.type):
                    query = query.filter(func_to_char(getattr(Patient, key), "yyyy-mm-dd") == value)
                else:
                    query = query.filter(getattr(Patient, key) == value)
            else:
                logging.warning("Unknow Query Condtions [%s] For %s", key, Patient)
        total = query.count()

        if bool(pageNum) or bool(pageSize):
            query = query.limit(pageSize).offset(pageSize * (int(pageNum) - 1))
        
        rst = []
        for pat in query.all():
            rst.append(pat)
        return {"data": rst, "total" : total}

    
    def getDetail1(self, bhzyid):
        query = g.db_session.query(Patient).filter(Patient.bhzyid == bhzyid)
        rst = None
        if(query.count() > 0):
            patient = query.first()
            rst = {"patient_info" : {
                                    "id" : patient.id,
                                    "bhzyid" : patient.bhzyid,
                                    "hxzyid" : patient.hxzyid,
                                    "name" : patient.name,
                                    "phone1" : patient.phone1,
                                    "phone2" : patient.phone2,
                                    "sex" : patient.sex,
                                    "marital_status" : patient.marital_status,
                                    "age" : patient.age,
                                    "mz" : patient.mz,
                                    "job" : patient.job,
                                    "jg" : patient.jg,
                                    "addr" : patient.addr,
                                    "fbDate" : patient.fbDate.strftime('%Y-%m-%d'),
                                    "ryDate" : patient.ryDate.strftime('%Y-%m-%d'),
                                    "cert_id" : patient.cert_id,
                                    "birthday" : patient.birthday.strftime('%Y-%m-%d'),
                                    "tall" : patient.tall,
                                    "weight" : patient.weight,
                                    "bmi" : patient.bmi
        }}
            return {"message" : "查询成功","data": rst}
        
    def getDetail2(self, hxzyid):
        query = g.db_session.query(Patient).filter(Patient.hxzyid == hxzyid)
        rst = None
        if(query.count() > 0):
            patient = query.first()
            rst = {"patient_info" : {
                                    "id" : patient.id,
                                    "bhzyid" : patient.bhzyid,
                                    "hxzyid" : patient.hxzyid,
                                    "name" : patient.name,
                                    "phone1" : patient.phone1,
                                    "phone2" : patient.phone2,
                                    "sex" : patient.sex,
                                    "marital_status" : patient.marital_status,
                                    "age" : patient.age,
                                    "mz" : patient.mz,
                                    "job" : patient.job,
                                    "jg" : patient.jg,
                                    "addr" : patient.addr,
                                    "fbDate" : patient.fbDate.strftime('%Y-%m-%d'),
                                    "ryDate" : patient.ryDate.strftime('%Y-%m-%d'),
                                    "cert_id" : patient.cert_id,
                                    "birthday" : patient.birthday.strftime('%Y-%m-%d'),
                                    "tall" : patient.tall,
                                    "weight" : patient.weight,
                                    "bmi" : patient.bmi
        }}
            return {"message" : "查询成功","data": rst}
            
    
    def search(self, key, pageSize=10, pageNum=1):
        query = g.db_session.query(Patient).filter(Patient.name.like("%{}%".format(key)))
        
        total = query.count()
        if bool(pageNum) or bool(pageSize):
            query = query.limit(pageSize).offset(pageSize * (int(pageNum) - 1))
        
        rst = []
        for pat in query.all():
            rst.append(pat)
        return {"data": rst, "total" : total}
    
    
    def get_previous_history(self,id, typeInput="id"):
        """获得既往病史"""
        if typeInput == "hxzyid":
            query = g.db_session.query(PreviousHistory).filter(PreviousHistory.hxzyid == id)
        elif typeInput == "hbzyid":
            query = g.db_session.query(PreviousHistory).filter(PreviousHistory.bhzyid == id)
        else:
            query = g.db_session.query(PreviousHistory).filter(PreviousHistory.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'rxlxjbs': qst.rxlxjbs,
                'rxlxjbsjtqk': qst.rxlxjbsjtqk,
                'grxjb':qst.grxjb,
                'grxjbjtqk':qst.grxjbjtqk,
                'xgyxrq':qst.xgyxrq.strftime('%Y-%m-%d'),
                'xgzyrq':qst.xgzyrq.strftime('%Y-%m-%d'),
                'xgzyqzfs':qst.xgzyqzfs,
                'xtxjb':qst.xtxjb,
                'xtjbjtqk':qst.xtjbjtqk,
                'sss':qst.sss,
                'sssjtqk':qst.sssjtqk,
                'exzl':qst.exzl,
                'exzljtqk':qst.exzljtqk
            }
        
        return rst
    

    def get_surgical_pathological_info(self, id, typeInput="id"):
        """获得 手术及病理信息

        Args:
            id (_type_): 病人编号
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(surgicalPathologicalInfo).filter(surgicalPathologicalInfo.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(surgicalPathologicalInfo).filter(surgicalPathologicalInfo.bhzyid == id)
        else:
            query = g.db_session.query(surgicalPathologicalInfo).filter(surgicalPathologicalInfo.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'ssrq' : qst.ssrq.strftime('%Y-%m-%d'),
                'ssfs' : qst.ssfs,
                'sfbr' : qst.sfbr,
                'sfzz' : qst.sfzz,
                'ywlbqsfs' : qst.ywlbqsfs,
                'shdblh' : qst.shdblh,
                'bzsl' : qst.bzsl,
                'ryzwdx' : qst.ryzwdx,
                'blxfq' : qst.blxfq,
                'bllx' : qst.bllx,
                'blxjtms' : qst.blxjtms,
                'zzxfj' : qst.zzxfj,
                'zzxfjjtqk':qst.zzxfjjtqk,
                'lbxgqf' : qst.lbxgqf,
                'lbgbs' : qst.lbgbs,
                "jzznqrlbxb" : qst.jzznqrlbxb,
                'hlfy' : qst.hlfy,
                "brsskjazz" : qst.brsskjazz,
                'brssbbzdd' : qst.brssbbzdd,
                'brssbbbqzdd' : qst.brssbbbqzdd,
                'lbjqk' : qst.lbjqk,
                'ywlbzs' : qst.ywlbzs,
                'yxywlbzs' : qst.yxywlbzs,
                'er' : qst.er,
                'pr' : qst.pr,
                'her2' : qst.her2,
                'her2jtqk':qst.her2jtqk,
                'ki67' : qst.ki67,
                'p53' : qst.p53,
                'fish':qst.fish,
                'fishjtqk':qst.fishjtqk,
                'hfc' : qst.hfc,
                'hfr' : qst.hfr
            }

        return rst

    def get_family_history(self, id, typeInput ="id"):
        """获得家族史

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(familyHistory).filter(familyHistory.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(familyHistory).filter(familyHistory.bhzyid == id)
        else:
            query = g.db_session.query(familyHistory).filter(familyHistory.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'wxzl' : qst.wxzl,
                'rxa' : qst.rxa,
                'lca' : qst.lca,
                'qtwxzl' : qst.qtwxzl,
                'xqs' : qst.xqs,
            }
        
        return rst
    
    def get_patient_history(self,id, typeInput="id"):
        """获得个人病史

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(patientHistory).filter(patientHistory.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(patientHistory).filter(patientHistory.bhzyid == id)
        else:
            query = g.db_session.query(patientHistory).filter(patientHistory.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'sfxy' : qst.sfxy,
                'jtxyl':qst.jtxyl,
                'sfyj' : qst.sfyj,
                'jtyjl':qst.jtyjl
            }
        
        return rst
    
    def get_clinical_feature(self, id, typeInput="id"):
        """获得临床特征

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(clinicalFeature).filter(clinicalFeature.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(clinicalFeature).filter(clinicalFeature.bhzyid == id)
        else:
            query = g.db_session.query(clinicalFeature).filter(clinicalFeature.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'fxwz' : qst.fxwz,
                'zkwz' : qst.zkwz,
                "lcsfzz" : qst.lcsfzz,
                'sfzzjtms':qst.sfzzjtms,
                "hcrt" : qst.hcrt,
                'hcrtjtms':qst.hcrtjtms,
                "hcpf" : qst.hcpf,
                'hcpfjtms':qst.hcpfjtms,
                "rtyy" : qst.rtyy,
                "yydg" : qst.yydg,
                "yyxz" : qst.yyxz,
                'yyxzjtms':qst.yyxzjtms,
                "yxjclx" : qst.yxjclx,
                "yxjch" : qst.yxjch,
                "sqzldx" : qst.sqzldx,
                "sqtfq" : qst.sqtfq,
                "sqyxlbjwz" : qst.sqyxlbjwz,
                "sqyxlbjdx" : qst.sqyxlbjdx,
                "sqnfq" : qst.sqnfq,
                "yczy" : qst.yczy,
                "zybw" : qst.zybw,
                'jtzybw':qst.jtzybw,
                "tnm" : qst.tnm,
                "zlbzqzfs" : qst.zlbzqzfs,
                'lbjqzfs':qst.lbjqzfs,
                "qzblh" : qst.qzblh,
                "sfxmyzh":qst.sfxmyzh,
                "er" : qst.er,
                "pr" : qst.pr,
                "her2" : qst.her2,
                'her2jtqk':qst.her2jtqk,
                "ki67" : qst.ki67,
                "p53" : qst.p53,
                'fish':qst.fish,
                'fishjtqk':qst.fishjtqk,
                "fcopy" : qst.fcopy,
                "fratio" : qst.fratio,
                
                "ywlbjer" : qst.ywlbjer,
                "ywlbjpr" : qst.ywlbjpr,
                "ywlbjher2" : qst.ywlbjher2,
                "ywlbjher2jtqk" : qst.ywlbjher2jtqk,
                "ywlbjki67" : qst.ywlbjki67,
                "ywlbjp53" : qst.ywlbjp53,
                'ywlbjfish':qst.ywlbjfish,
                'ywlbjfishjtqk':qst.ywlbjfishjtqk,
                "ywlbjfcopy" : qst.ywlbjfcopy,
                "ywlbjfratio" : qst.ywlbjfratio,

                "jblbjer" : qst.jblbjer,
                "jblbjpr" : qst.jblbjpr,
                "jblbjher2" : qst.jblbjher2,
                "jblbjher2jtqk" : qst.jblbjher2jtqk,
                "jblbjki67" : qst.jblbjki67,
                "jblbjp53" : qst.jblbjp53,
                'jblbjfish':qst.jblbjfish,
                'jblbjfishjtqk':qst.jblbjfishjtqk,
                "jblbjfcopy" : qst.jblbjfcopy,
                "jblbjfratio" : qst.jblbjfratio,
                
                "yczyqzbw" : qst.yczyqzbw,
                "yczyer" : qst.yczyer,
                "yczypr" : qst.yczypr,
                "yczyher2" : qst.yczyher2,
                'yczyher2jtqk':qst.yczyher2jtqk,
                "yczyki67" : qst.yczyki67,
                "yczyp53" : qst.yczyp53,
                'yczyfish':qst.yczyfish,
                'yczyfishjtqk':qst.yczyfishjtqk,
                "yczyfcopy" : qst.yczyfcopy,
                "yczyfratio" : qst.yczyfratio,
                
                "xfzzl" : qst.xfzzl,
                "xfzzlkssj" : qst.xfzzlkssj.strftime('%Y-%m-%d'),
                "xfzzlfa" : qst.xfzzlfa,
                "xfzlc" : qst.xfzlc,
                "xfzlcyw" : qst.xfzlcyw,
                "xfzzlpg" : qst.xfzzlpg,
                "xfzzlpj" : qst.xfzzlpg,
                
                "jjlz" : qst.jjzl,
                "sqzlkssj" : qst.sqzlkssj.strftime('%Y-%m-%d'),
                "sqzlfa" : qst.sqzlfa,
                "jjlc" : qst.jjlc,
                "jjlcyw" : qst.jjlcyw,
                "sqzlpg" : qst.sqzlpg,
                "sqzlpj" : qst.sqzlpj,
            }
        
        return rst
    
    def get_patient_menstruation_history(self, id, typeInput="id"):
        """获得月经史

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(patientMenstruationHistory).filter(patientMenstruationHistory.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(patientMenstruationHistory).filter(patientMenstruationHistory.bhzyid == id)
        else:
            query = g.db_session.query(patientMenstruationHistory).filter(patientMenstruationHistory.id == id)

        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'ccage' : qst.ccage,
                'yjzq' : qst.yjzq,
                'jq' : qst.jq,
                'sfjj' : qst.sfjj,
                'jjfs' : qst.jjfs,
                'jtjjfs':qst.jtjjfs,
                'mqyj' : qst.mqyj.strftime('%Y-%m-%d'),
                'jjage' : qst.jjage
            }
        
        return rst

    def get_patient_marry_history(self, id, typeInput="id"):
        """获得婚育史

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(patientMarryHistory).filter(patientMarryHistory.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(patientMarryHistory).filter(patientMarryHistory.bhzyid == id)
        else:
            query = g.db_session.query(patientMarryHistory).filter(patientMarryHistory.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'sy' : qst.sy,
                'qzssyzt' : qst.qzssyzt,
                'ccage' : qst.ccage,
                'mtage' : qst.mtage,
                'hycs' : qst.hycs,
                'zyc' : qst.zyc,
                'lczcs' : qst.lczcs,
                'fzsy' : qst.fzsy,
                'fzsyfs' : qst.fzsyfs,
                'sfmrwy' : qst.sfmrwy,
                'mrcb' : qst.mrcb,
                'mrsc' : qst.mrsc
            }
        
        return rst

    def get_patient_follow(self, id, typeInput="id"):
        """获得病人跟踪记录

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(patientFollow).filter(patientFollow.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(patientFollow).filter(patientFollow.bhzyid == id)
        else:
            query = g.db_session.query(patientFollow).filter(patientFollow.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'dfs' : qst.dfs,
                'os' : qst.os,
                'mcfcsj' : qst.mcfcsj.strftime('%Y-%m-%d'),
                'syqk' : qst.syqk,
                'syfaz' : qst.syfaz,
                'syfazjtxq':qst.syfazjtxq,
                'zhsfsj' : qst.zhsfsj.strftime('%Y-%m-%d'),
                'sfbz' : qst.sfbz,
                'swyf' : qst.swyf,
                'swsj' : qst.swsj.strftime('%Y-%m-%d'),
                'sy' : qst.sy,
                'jtsy':qst.jtsy
            }
        
        return rst
    
    def get_postoperative_treatment(self, id, typeInput="id"):
        """获得术后治疗

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(postoperativeTreatment).filter(postoperativeTreatment.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(postoperativeTreatment).filter(postoperativeTreatment.bhzyid == id)
        else:
            query = g.db_session.query(postoperativeTreatment).filter(postoperativeTreatment.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'shhl' : qst.shhl,
                'hlkssj' : qst.hlkssj.strftime('%Y-%m-%d'),
                'shhlfam' : qst.shhlfam,
                'hllc' : qst.hllc,
                'hllcyw' : qst.hllcyw,
                'shhlxq' : qst.shhlxq,
                'shnfmzl' : qst.shnfmzl,
                'nfmzlkssj' : qst.nfmzlkssj.strftime('%Y-%m-%d'),
                'nfmzlym' : qst.nfmzlym,
                'nfmzlfzy' : qst.nfmzlfzy,
                'shbxzl' : qst.shbxzl,
                'bxzlkssj' : qst.bxzlkssj.strftime('%Y-%m-%d'),
                'bxzlym' : qst.bxzlym,
                'shfl' : qst.shfl,
                'flkssj' : qst.flkssj.strftime('%Y-%m-%d'),
                'flbz' : qst.flbz,
                'shmyzl' : qst.shmyzl,
                'myzlsj':qst.myzlsj.strftime('%Y-%m-%d'),
                'myzlbz':qst.myzlbz

            }
        
        return rst
        
        
    def get_relapse_information(self, id, typeInput="id"):
        """获得复发信息

        Args:
            id (_type_): _description_
        """
        if typeInput == "hxzyid":
            query = g.db_session.query(relapseInformation).filter(relapseInformation.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(relapseInformation).filter(relapseInformation.bhzyid == id)
        else:
            query = g.db_session.query(relapseInformation).filter(relapseInformation.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'djcff': qst.djcff,
                'ffbw' : qst.ffbw,
                'jtffbw':qst.jtffbw,
                'ffrq' : qst.ffrq.strftime('%Y-%m-%d'),
                'ffqzsd' : qst.ffqzsd,
                'ffbzblxx' : qst.ffbzblxx,
                "ffbzymzh" : qst.ffbzymzh,               
                'ffhzl' : qst.ffhzl,
                'ffxgpj' : qst.ffxgpj
            }
            
        return rst
    
    def get_peripheral_blood_sample_sampling(self, id,typeInput="id"):
        if typeInput == "hxzyid":
            query = g.db_session.query(peripheralBloodSampleSampling).filter(peripheralBloodSampleSampling.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(peripheralBloodSampleSampling).filter(peripheralBloodSampleSampling.bhzyid == id)
        else:
            query = g.db_session.query(peripheralBloodSampleSampling).filter(peripheralBloodSampleSampling.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                'id' : qst.id,
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                'bblx' : qst.bblx,
                'cxsjd' : qst.cxsjd.strftime('%Y-%m-%d'),
                'cjr' : qst.cjr,
                'cjbz' : qst.cjbz,
                "cjyt" : qst.cjyt,
                'ybid':qst.ybid,
                'ybnum':qst.ybnum,
                'ybhbh':qst.ybhbh,
                'ybcfwz':qst.ybcfwz,
                'sfqy':qst.sfqy,
                'qyrq':qst.qyrq.strftime('%Y-%m-%d'),
                'qyr':qst.qyr,
                'qyyt':qst.qyyt,
                'qybz':qst.qybz



            }
            
        return rst
    
    def get_gene21_detection(self, id, typeInput="id"):
        if typeInput == "hxzyid":
            query = g.db_session.query(gene21Detection).filter(gene21Detection.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(gene21Detection).filter(gene21Detection.bhzyid == id)
        else:
            query = g.db_session.query(gene21Detection).filter(gene21Detection.id == id)
        rst = []
        if query.count() > 0:
            for qst in query.all():
                rst.append({
                "id" : qst.id, 
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                "sfjx21jyjc" : qst.sfjx21jyjc, 
                "jcsj" : qst.jcsj.strftime('%Y-%m-%d'), 
                "yjbh" : qst.yjbh,
                "jcry" : qst.jcry, 
                "bbwz" : qst.bbwz, 
                "bz" : qst.bz,
                'jtxq' : qst.jtxq
            })
            
        return rst
    
    def get_gene70_detection(self, id, typeInput="id"):
        if typeInput == "hxzyid":
            query = g.db_session.query(gene70Detection).filter(gene70Detection.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(gene70Detection).filter(gene70Detection.bhzyid == id)
        else:
            query = g.db_session.query(gene70Detection).filter(gene70Detection.id == id)
        rst = []
        if query.count() > 0:
            for qst in query.all():
                rst.append({
                "id" : qst.id, 
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                "sfjx70jyjc" : qst.sfjx70jyjc, 
                "jcsj" : qst.jcsj.strftime('%Y-%m-%d'), 
                "yjbh" : qst.yjbh,
                "jcry" : qst.jcry, 
                "bbwz" : qst.bbwz, 
                "bz" : qst.bz,
                'jtxq' : qst.jtxq
            })
            
        return rst
    
    def get_genebrca_detection(self, id, typeInput="id"):
        if typeInput == "hxzyid":
            query = g.db_session.query(genebrcaDetection).filter(genebrcaDetection.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(genebrcaDetection).filter(genebrcaDetection.bhzyid == id)
        else:
            query = g.db_session.query(genebrcaDetection).filter(genebrcaDetection.id == id)
        rst = []
        if query.count() > 0:
            for qst in query.all():
                rst.append({
                "id" : qst.id, 
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                "sfjxbrcajyjc" : qst.sfjxbrcajyjc, 
                "jcsj" : qst.jcsj.strftime('%Y-%m-%d'), 
                "yjbh" : qst.yjbh,
                "jcry" : qst.jcry, 
                "bbwz" : qst.bbwz, 
                "bz" : qst.bz,
                'jtxq' : qst.jtxq
            })
            
        return rst
    
    
    
    def get_recorder_information(self, id, typeInput="id"):
        
        if typeInput == "hxzyid":
            query = g.db_session.query(recorderInformation).filter(recorderInformation.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(recorderInformation).filter(recorderInformation.bhzyid == id)
        else:
            query = g.db_session.query(recorderInformation).filter(recorderInformation.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                "id" : qst.id, 
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                "sclrr" : qst.sclrr,  
                "sclrsj" : qst.sclrsj.strftime('%Y-%m-%d'), 
                "mcsfr" : qst.mcsfr, 
                "mcsfsj" : qst.mcsfsj.strftime('%Y-%m-%d')
            }
            
        return rst
    
    def get_recurrent_distant_metastasis(self, id, typeInput="id"):
        """recurrent_distant_metastasis"""
        
        if typeInput == "hxzyid":
            query = g.db_session.query(recurrentDistantMetastasis).filter(recurrentDistantMetastasis.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(recurrentDistantMetastasis).filter(recurrentDistantMetastasis.bhzyid == id)
        else:
            query = g.db_session.query(recurrentDistantMetastasis).filter(recurrentDistantMetastasis.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                "id" : qst.id, 
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                "djczy" : qst.djczy,  
                "yzzybw" : qst.yzzybw, 
                "yczyrq" : qst.yczyrq.strftime('%Y-%m-%d'), 
                'yczyqzsd':qst.yczyqzsd,
                'yzzyblxx':qst.yzzyblxx,
                'yzzymyzh':qst.yzzymyzh,
                "yczyzl" : qst.yczyzl,
                "yczyzlxgpj" : qst.yczyzlxgpj
            }
            
        return rst
        
    def get_sampling_recurrence_metastasis_specimens(self, id, typeInput="id"):
        """sampling_recurrence_metastasis_specimens"""
        
        if typeInput == "hxzyid":
            query = g.db_session.query(samplingRecurrenceMetastasisSpecimens).filter(samplingRecurrenceMetastasisSpecimens.hxzyid == id)
        elif typeInput == "bhzyid":
            query = g.db_session.query(samplingRecurrenceMetastasisSpecimens).filter(samplingRecurrenceMetastasisSpecimens.bhzyid == id)
        else:
            query = g.db_session.query(samplingRecurrenceMetastasisSpecimens).filter(samplingRecurrenceMetastasisSpecimens.id == id)
        rst = None
        if query.count() > 0:
            qst = query.first()
            rst = {
                "id" : qst.id, 
                'bhzyid' : qst.bhzyid,
                'hxzyid' : qst.hxzyid,
                "glbz" : qst.glbz, 
                "cyrq" : qst.cyrq.strftime('%Y-%m-%d'),  
                "ytbz" : qst.ytbz, 
                "qtyt" : qst.qtyt, 
                "cjr" : qst.cjr,
                "bblx" : qst.bblx,
                "bbxz" : qst.bbxz,
                'ybid':qst.ybid,
                'ybnum':qst.ybnum,
                'ybhbh':qst.ybhbh,
                'ybcfwz':qst.ybcfwz,
                'sfqy':qst.sfqy,
                'qyrq':qst.qyrq.strftime('%Y-%m-%d'),
                'qyr':qst.qyr,
                'qyyt':qst.qyyt,
                'qybz':qst.qybz
            }
            
        return rst
    
    
    def get_all_patient_info_by_id(self, id):
        query = g.db_session.query(Patient).filter(Patient.id == id)
        rst = None
        if(query.count() > 0):
            patient = query.first()
            rst = {"patient_info" : {
                                    "id" : patient.id,
                                    "bhzyid" : patient.bhzyid,
                                    "hxzyid" : patient.hxzyid,
                                    "name" : patient.name,
                                    "phone1" : patient.phone1,
                                    "phone2" : patient.phone2,
                                    "sex" : patient.sex,
                                    "marital_status" : patient.marital_status,
                                    "age" : patient.age,
                                    "mz" : patient.mz,
                                    "job" : patient.job,
                                    "jg" : patient.jg,
                                    "addr" : patient.addr,
                                    "fbDate" : patient.fbDate.strftime('%Y-%m-%d'),
                                    "ryDate" : patient.ryDate.strftime('%Y-%m-%d'),
                                    "cert_id" : patient.cert_id,
                                    "birthday" : patient.birthday.strftime('%Y-%m-%d'),
                                    "tall" : patient.tall,
                                    "weight" : patient.weight,
                                    "bmi" : patient.bmi
        }}
        
            rst["previous_history"] = self.get_previous_history(id)
            rst["surgical_pathological_info"] = self.get_surgical_pathological_info(id)
            rst["family_history"] = self.get_family_history(id)
            rst["patient_history"] = self.get_patient_history(id)
            rst["clinical_feature"] = self.get_clinical_feature(id)
            rst['patient_menstruation_history'] = self.get_patient_menstruation_history(id)
            rst['patient_marry_history'] = self.get_patient_marry_history(id)
            rst['patient_follow'] = self.get_patient_follow(id)
            rst["postoperative_treatment"] = self.get_postoperative_treatment(id)
            rst["relapse_information"] = self.get_relapse_information(id)
            rst["gene21_detection"] = self.get_gene21_detection(id)
            rst["gene70_detection"] = self.get_gene70_detection(id)
            rst["genebrca_detection"] = self.get_genebrca_detection(id)
            rst['recorder_information'] = self.get_recorder_information(id)
            rst['recurrent_distant_metastasis'] = self.get_recurrent_distant_metastasis(id)
            rst['sampling_recurrence_metastasis_specimens'] = self.get_sampling_recurrence_metastasis_specimens(id)
            rst["peripheral_blood_sample_sampling"] = self.get_peripheral_blood_sample_sampling(id)
            
        return {"message" : "查询成功","data": rst}        
    
    def get_all_patient_info_by_bhzyid(self,bhzyid):
        
        query = g.db_session.query(Patient).filter(Patient.bhzyid == bhzyid)
        rst = {}
        if(query.count() > 0):
            patient = query.first()
            rst = {"patient_info" : {
                                    "id" : patient.id,
                                    "bhzyid" : patient.bhzyid,
                                    "hxzyid" : patient.hxzyid,
                                    "name" : patient.name,
                                    "phone1" : patient.phone1,
                                    "phone2" : patient.phone2,
                                    "sex" : patient.sex,
                                    "marital_status" : patient.marital_status,
                                    "age" : patient.age,
                                    "mz" : patient.mz,
                                    "job" : patient.job,
                                    "jg" : patient.jg,
                                    "addr" : patient.addr,
                                    "fbDate" : patient.fbDate.strftime('%Y-%m-%d'),
                                    "ryDate" : patient.ryDate.strftime('%Y-%m-%d'),
                                    "cert_id" : patient.cert_id,
                                    "birthday" : patient.birthday.strftime('%Y-%m-%d'),
                                    "tall" : patient.tall,
                                    "weight" : patient.weight,
                                    "bmi" : patient.bmi
        }}
        
        
        rst["previous_history"] = self.get_previous_history(bhzyid, "bhzyid")
        rst["surgical_pathological_info"] = self.get_surgical_pathological_info(bhzyid, "bhzyid")
        rst["family_history"] = self.get_family_history(bhzyid, "bhzyid")
        rst["patient_history"] = self.get_patient_history(bhzyid, "bhzyid")
        rst["clinical_feature"] = self.get_clinical_feature(bhzyid, "bhzyid")
        rst['patient_menstruation_history'] = self.get_patient_menstruation_history(bhzyid, "bhzyid")
        rst['patient_marry_history'] = self.get_patient_marry_history(bhzyid, "bhzyid")
        rst['patient_follow'] = self.get_patient_follow(bhzyid, "bhzyid")
        rst["postoperative_treatment"] = self.get_postoperative_treatment(bhzyid, "bhzyid")
        rst["relapse_information"] = self.get_relapse_information(bhzyid, "bhzyid")
        rst["gene21_detection"] = self.get_gene21_detection(bhzyid, "bhzyid")
        rst["gene70_detection"] = self.get_gene70_detection(bhzyid, "bhzyid")
        rst["genebrca_detection"] = self.get_genebrca_detection(bhzyid, "bhzyid")
        rst['recorder_information'] = self.get_recorder_information(bhzyid, "bhzyid")
        rst['recurrent_distant_metastasis'] = self.get_recurrent_distant_metastasis(bhzyid, "bhzyid")
        rst['sampling_recurrence_metastasis_specimens'] = self.get_sampling_recurrence_metastasis_specimens(bhzyid, "bhzyid")
        rst["peripheral_blood_sample_sampling"] = self.get_peripheral_blood_sample_sampling(bhzyid, "bhzyid")
        
        return {"message" : "查询成功","data": rst}


    def get_all_patient_info_by_hxzyid(self, hxzyid):
        query = g.db_session.query(Patient).filter(Patient.hxzyid == hxzyid)
        rst = None
        if(query.count() > 0):
            patient = query.first()
            rst = {"patient_info" : {
                                    "id" : patient.id,
                                    "bhzyid" : patient.bhzyid,
                                    "hxzyid" : patient.hxzyid,
                                    "name" : patient.name,
                                    "phone1" : patient.phone1,
                                    "phone2" : patient.phone2,
                                    "sex" : patient.sex,
                                    "marital_status" : patient.marital_status,
                                    "age" : patient.age,
                                    "mz" : patient.mz,
                                    "job" : patient.job,
                                    "jg" : patient.jg,
                                    "addr" : patient.addr,
                                    "fbDate" : patient.fbDate.strftime('%Y-%m-%d'),
                                    "ryDate" : patient.ryDate.strftime('%Y-%m-%d'),
                                    "cert_id" : patient.cert_id,
                                    "birthday" : patient.birthday.strftime('%Y-%m-%d'),
                                    "tall" : patient.tall,
                                    "weight" : patient.weight,
                                    "bmi" : patient.bmi
        }}
        
            rst["previous_history"] = self.get_previous_history(hxzyid, "hxzyid")
            rst["surgical_pathological_info"] = self.get_surgical_pathological_info(hxzyid, "hxzyid")
            rst["family_history"] = self.get_family_history(hxzyid, "hxzyid")
            rst["patient_history"] = self.get_patient_history(hxzyid, "hxzyid")
            rst["clinical_feature"] = self.get_clinical_feature(hxzyid, "hxzyid")
            rst['patient_menstruation_history'] = self.get_patient_menstruation_history(hxzyid, "hxzyid")
            rst['patient_marry_history'] = self.get_patient_marry_history(hxzyid, "hxzyid")
            rst['patient_follow'] = self.get_patient_follow(hxzyid, "hxzyid")
            rst["postoperative_treatment"] = self.get_postoperative_treatment(hxzyid, "hxzyid")
            rst["relapse_information"] = self.get_relapse_information(hxzyid, "hxzyid")
            rst["gene21_detection"] = self.get_gene21_detection(hxzyid, "hxzyid")
            rst["gene70_detection"] = self.get_gene70_detection(hxzyid, "hxzyid")
            rst["genebrca_detection"] = self.get_genebrca_detection(hxzyid, "hxzyid")
            rst['recorder_information'] = self.get_recorder_information(hxzyid, "hxzyid")
            rst['recurrent_distant_metastasis'] = self.get_recurrent_distant_metastasis(hxzyid, "hxzyid")
            rst['sampling_recurrence_metastasis_specimens'] = self.get_sampling_recurrence_metastasis_specimens(hxzyid, "hxzyid")
            rst["peripheral_blood_sample_sampling"] = self.get_peripheral_blood_sample_sampling(hxzyid, "hxzyid")
            
            return {"message" : "查询成功","data": rst}
        
        
    def add_patient(self, **kwargs):
        """Add a new patient"""
        cert_id = kwargs.get("cert_id")
        if not is_id_number(cert_id):
            return {"message":"添加失败，身份证号校验失败", "status":403} 

        try:
            patient = Patient(**kwargs)
            g.db_session.add(patient)
            g.db_session.flush()
            id = patient.id
            g.db_session.commit()
            msg = "添加成功，patient编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}


    def add_previous_history(self, **kwargs):
        """Add a new history"""

        grxjb = kwargs.get("grxjb").split(",")
        grxjb_set = set(['无','肝炎','梅毒','艾滋','新冠'])

        for x in grxjb:
            if x not in grxjb_set:
                return {"message":"添加失败,非法输入[感染性疾病]，只支持 【'无','肝炎','梅毒','艾滋','新冠'】", "status":403}
        
        xtxjb = kwargs.get("xtxjb").split(",")
        xtxjb_set = set(['无','高血压','心脏病','糖尿病','青光眼','哮喘','甲状腺疾病','脑血管疾病','精神疾病'])
        for x in xtxjb:
            if x not in xtxjb_set:
                return {"message":"添加失败,非法输入[是否有系统疾病]，只支持 【'无','高血压','心脏病','糖尿病','青光眼','哮喘','甲状腺疾病','脑血管疾病','精神疾病'】", "status":403}
        try:
            histroy = PreviousHistory(**kwargs)
            g.db_session.add(histroy)
            g.db_session.flush()
            id = histroy.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_surgical_pathological_info(self, **kwargs):
        """add 手术及病理信息"""
        try:
            surgical = surgicalPathologicalInfo(**kwargs)
            g.db_session.add(surgical)
            g.db_session.flush()
            id = surgical.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}

    def add_family_history(self, **kwargs):
        """add 家族史表"""
        try:
            fhistory = familyHistory(**kwargs)
            g.db_session.add(fhistory)
            g.db_session.flush()
            id = fhistory.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_patient_history(self, **kwargs):
        """add 个人史表"""

        try:
            ph = patientHistory(**kwargs)
            g.db_session.add(ph)
            g.db_session.flush()
            id = ph.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_clinical_feature(self, **kwargs):
        """add 临床特征表"""

        zybw = kwargs.get("zybw").split(",")
        zybw_set = set(['肝','肺','骨','脑','其他',''])

        for x in zybw:
            if x not in zybw_set:
                return {"message":"添加失败,非法输入[转移部位]，只支持 【'肝','肺','骨','脑','其他',''】", "status":403}
        try:
            feature = clinicalFeature(**kwargs)
            g.db_session.add(feature)
            g.db_session.flush()
            id = feature.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_patient_menstruation_history(self, **kwargs):
        """add 月经史表"""

        try:
            history = patientMenstruationHistory(**kwargs)
            g.db_session.add(history)
            g.db_session.flush()
            id = history.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_patient_marry_history(self, **kwargs):
        """add 婚育史表"""
        try:
            history = patientMarryHistory(**kwargs)
            g.db_session.add(history)
            g.db_session.flush()
            id = history.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_patient_follow(self, **kwargs):
        """add 病人跟踪记录表"""
        try:
            follow = patientFollow(**kwargs)
            g.db_session.add(follow)
            g.db_session.flush()
            id = follow.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_postoperative_treatment(self, **kwargs):
        """add术后治疗表 """

        try:
            treatment = postoperativeTreatment(**kwargs)
            g.db_session.add(treatment)
            g.db_session.flush()
            id = treatment.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_relapse_information(self, **kwargs):
        """add 复发信息表"""

        try:
            relapse = relapseInformation(**kwargs)
            g.db_session.add(relapse)
            g.db_session.flush()
            id = relapse.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_gene21_detection(self, **kwargs):
        """add 21基因信息表"""

        try:
            gene21 = gene21Detection(**kwargs)
            g.db_session.add(gene21)
            g.db_session.flush()
            id = gene21.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}

    def add_gene70_detection(self, **kwargs):
        """add 70基因信息表"""

        try:
            gene70 = gene70Detection(**kwargs)
            g.db_session.add(gene70)
            g.db_session.flush()
            id = gene70.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
        
    def add_genebrca_detection(self, **kwargs):
        """add brca基因信息表"""

        try:
            genebrca = genebrcaDetection(**kwargs)
            g.db_session.add(genebrca)
            g.db_session.flush()
            id = genebrca.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_peripheral_blood_sample_sampling(self, **kwargs):
        """add 外周血标本采样表"""

        try:
            blood = peripheralBloodSampleSampling(**kwargs)
            g.db_session.add(blood)
            g.db_session.flush()
            id = blood.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_recorder_information(self, **kwargs):
        """add 记录人员信息表"""


        try:
            recorder = recorderInformation(**kwargs)
            g.db_session.add(recorder)
            g.db_session.flush()
            id = recorder.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    

    def add_recurrent_distant_metastasis(self, **kwargs):
        """add 远处转移信息表"""

        yzzybw = kwargs.get('yzzybw')
        yzzybw_set = set(['对侧乳腺','非同侧胸壁','区域淋巴结','骨','肺','肝','脑','其他'])

        for x in yzzybw:
            if x not in yzzybw_set:
                return {"message":"添加失败,非法输入[远处转移部位]，只支持 【'对侧乳腺','非同侧胸壁','区域淋巴结','骨','肺','肝','脑','其他'】", "status":403}

        try:
            recurrent = recurrentDistantMetastasis(**kwargs)
            g.db_session.add(recurrent)
            g.db_session.flush()
            id = recurrent.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
    
    def add_sampling_recurrence_metastasis_specimens(self, **kwargs):
        """add 复发转移灶标本采样表"""


        try:
            specimens = samplingRecurrenceMetastasisSpecimens(**kwargs)
            g.db_session.add(specimens)
            g.db_session.flush()
            id = specimens.id
            g.db_session.commit()
            msg = "添加成功，编号为：{}".format(id)
            status = 200
        except Exception as e:
            status = 400
            msg = "添加失败，失败原因[{}]".format(e.orig)
            print(e)
        finally:
            return {"message":msg,"status":status}
        
    
    def batch_add_patient(self, filename):
        """批量添加患者信息
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "姓名" : "name",
                "初诊年龄":"age",
                "婚姻状况":"marital_status",
                "民族":"mz",
                "性别":"sex",
                "职业":"job",
                "籍贯":"jg",
                "现地址":"addr", 
                "入院日期":"ryDate",
                "发现日期":"fbDate",
                "联系电话1":"phone1",
                "联系电话2":"phone2",
                "身份证号":"cert_id",
                "出生日期":"birthday",
                "体重":"tall",
                "身高":"weight",
                "BMI":"bmi"
            }
            
            df = upload_excel(filename, name_dict)
            # df['fbDate']=pd.to_datetime(df['fbDate'],format='%m-%d-%Y %H:%M:%S')
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['age'] = df['age'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['birthday'] = df['birthday'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['ryDate'] = df['ryDate'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['fbDate'] = df['fbDate'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['tall'] = df['tall'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['weight'] = df['weight'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['bmi'] = df['bmi'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            rst_data = df.to_dict(orient='records')
            """校验：
                手机号码校验：phone1,phone2 不能相同
                
            """
            valid_num = 0
            for row in rst_data:
                if row['phone1'] == row['phone2']:
                    continue
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = Patient(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
            status = 200
            msg = "批量导入成功"    
            
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    
    def batch_add_patient_history(self, filename):
        """批量添加个人史信息

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                # "编号" : "id",
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "是否吸烟" : "sfxy",
                "具体吸烟量" : "jtxyl",
                "是否饮酒" : "sfyj",
                "具体饮酒量" : "jtyjl"
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            
            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = patientHistory(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}


    def batch_add_family_history(self, filename):
        """批量添加家族史信息

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "是否有恶性肿瘤家族史" : "wxzl",
                "乳腺癌家族史" : "rxa",
                "卵巢癌家族史" : "lca",
                "其他恶性肿瘤家族史" : "qtwxzl",
                "x级亲属" : "xqs"
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = familyHistory(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
        
    
    def batch_add_postoperative_treatment(self, filename):
        """批量添加术后治疗表信息

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "术后化疗" : "shhl",
                "术后化疗开始时间" : "hlkssj",
                "术后化疗方案": "shhlfam",
                "术后化疗详情": "shhlxq",
                "术后化疗期间是否使用卵巢功能抑制剂": "hllc",
                "术后化疗卵巢功能抑制剂具体药物名称": "hllcyw",
                "术后内分泌治疗": "shnfmzl",
                "术后内分泌治疗开始时间": "nfmzlkssj",
                "术后内分泌药物": "nfmzlym",
                "内分泌治疗副作用": "nfmzlfzy",
                "是否术后靶向治疗": "shbxzl",
                "术后靶向治疗开始时间": "bxzlkssj",
                "术后靶向治疗具体药物": "bxzlym",
                "术后放疗": "shfl",
                "术后放疗开始时间": "flkssj",
                "术后放疗备注": "flbz",
                "术后免疫治疗": "shmyzl",
                "术后免疫治疗开始时间": "myzlsj",
                "术后免疫治疗备注": "myzlbz",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hlkssj'] = df['hlkssj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['nfmzlkssj'] = df['nfmzlkssj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['bxzlkssj'] = df['bxzlkssj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['flkssj'] = df['flkssj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['myzlsj'] = df['myzlsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = postoperativeTreatment(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    
    def batch_add_patient_marry_history(self, filename):
        """批量添加婚育史信息

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "生育" : "sy",
                "确诊时生育状态" : "qzssyzt",
                "初产年龄" : "ccage",
                "末胎年龄" : "mtage",
                "怀孕次数" : "hycs",
                "足月产" : "zyc",
                "流产或早产史" : "lczcs",
                "是否辅助生育" : "fzsy",
                "辅助生育方式" : "fzsyfs",
                "是否母乳喂养" : "sfmrwy",
                "哺乳侧别" : "mrcb",
                "哺乳时长" : "mrsc",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = patientMarryHistory(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    

    def batch_add_menstruation_history(self, filename):
        """批量添加月经史信息

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid" ,
                "河西住院号" : "hxzyid" ,
                "初潮年龄" : "ccage" ,
                "月经周期" : "yjzq" ,
                "经期" : "jq" ,
                "是否绝经" : "sfjj" ,
                "绝经方式" : "jjfs" ,
                "具体绝经方式" : "jtjjfs" ,
                "末次月经" : "mqyj" ,
                "绝经年龄" : "jjage" ,
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['mqyj'] = df['mqyj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = patientMenstruationHistory(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
        
    def batch_add_clinical_feature(self, filename):
        """批量添加临床特征表信息

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid" ,
                "河西住院号" : "hxzyid" ,
                "发现方式" : "fxwz" ,
                "肿瘤位置" : "zkwz" ,
                "有无临床首发症状" : "lcsfzz" ,
                "首发症状具体描述" : "sfzzjtms",
                "患侧乳头" : "hcrt",
                "患侧乳头症状具体描述" : "hcrtjtms",
                "患侧皮肤" : "hcpf",
                "患侧皮肤症状具体描述" : "hcpfjtms",
                "乳头溢液" : "rtyy",
                "溢液导管" : "yydg",
                "溢液性质" : "yyxz",
                "溢液性质具体描述" : "yyxzjtms",
                "影像检查类型" : "yxjclx",
                "影像检查号" : "yxjch",
                "术前影像肿瘤大小" : "sqzldx",
                "术前T分期" : "sqtfq",
                "术前影像腋下淋巴结位置" : "sqyxlbjwz",
                "术前影像腋下淋巴结大小" : "sqyxlbjdx",
                "术前N分期" : "sqnfq",
                "远处转移与否" : "yczy",
                "转移部位" : "zybw",
                "具体转移部位" : "jtzybw",
                "临床TNM分期" : "tnm",
                "肿瘤病灶确诊方式" : "zlbzqzfs",
                "淋巴结确诊方式" : "lbjqzfs",
                "确诊病理信息" : "qzblh",
                "是否行免疫组化" : "sfxmyzh",

                "肿瘤病灶穿刺ER" : "er",
                "肿瘤病灶穿刺PR" : "pr",
                "肿瘤病灶穿刺Her2" : "her2",
                "肿瘤病灶穿刺Her2具体情况" : "her2jtqk",
                "肿瘤病灶穿刺Ki67" : "ki67",
                "肿瘤病灶穿刺P53" : "p53",
                "肿瘤病灶FISH" : "fish",
                "肿瘤病灶FISH具体情况" : "fishjtqk",
                "肿瘤病灶FISH copy数" : "fcopy",
                "肿瘤病灶FISH ratio" : "fratio",

                "腋窝淋巴结穿刺ER" : "ywlbjer",
                "腋窝淋巴结穿刺PR" : "ywlbjpr",
                "腋窝淋巴结穿刺Her2" : "ywlbjher2",
                "腋窝淋巴结穿刺Her2具体情况" : "ywlbjher2jtqk",
                "腋窝淋巴结穿刺Ki67" : "ywlbjki67",
                "腋窝淋巴结穿刺P53" : "ywlbjp53",
                "腋窝淋巴结FISH" : "ywlbjfish",
                "腋窝淋巴结FISH具体情况" : "ywlbjfishjtqk",
                "腋窝淋巴结FISH copy数" : "ywlbjfcopy",
                "腋窝淋巴结FISH ratio" : "ywlbjfratio",

                "颈部淋巴结穿刺ER" : "jblbjer",
                "颈部淋巴结穿刺PR" : "jblbjpr",
                "颈部淋巴结穿刺Her2" : "jblbjher2",
                "颈部淋巴结穿刺Her2具体情况" : "jblbjher2jtqk",
                "颈部淋巴结穿刺Ki67" : "jblbjki67",
                "颈部淋巴结穿刺P53" : "jblbjp53",
                "颈部淋巴结FISH" : "jblbjfish",
                "颈部淋巴结FISH具体情况" : "jblbjfishjtqk",
                "颈部淋巴结FISHcopy数" : "jblbjfcopy",
                "颈部淋巴结FISHratio" : "jblbjfratio",

                "远处转移确诊部位" : "yczyqzbw",
                "远处转移灶ER" : "yczyer",
                "远处转移灶PR" : "yczypr",
                "远处转移灶Her2" : "yczyher2",
                "远处转移灶Her2具体情况" : "yczyher2jtqk",
                "远处转移灶Ki67" : "yczyki67",
                "远处转移灶P53" : "yczyp53",
                "远处转移灶FISH" : "yczyfish",
                "远处转移灶FISH具体情况" : "yczyfishjtqk",
                "远处转移灶FISH copy数" : "yczyfcopy",
                "远处转移灶FISH ratio" : "yczyfratio",

                "术前是否行新辅助治疗" : "xfzzl" ,
                "新辅助治疗开始时间" : "xfzzlkssj" ,
                "新辅助治疗方案及周期" : "xfzzlfa" ,
                "新辅助治疗期间是否使用卵巢功能抑制剂" : "xfzlc" ,
                "新辅助治疗卵巢功能抑制剂具体药物名称" : "xfzlcyw" ,
                "新辅助治疗过程评估" : "xfzzlpg" ,
                "新辅助治疗疗效评价" : "xfzzlpj" ,

                "术前是否行解救治疗" : "jjzl" ,
                "术前解救治疗开始时间" : "sqzlkssj" ,
                "术前解救治疗方案及周期" : "sqzlfa" ,
                "术前解救治疗期间是否使用卵巢功能抑制剂" : "jjlc" ,
                "术前解救治疗卵巢功能抑制剂具体药物名称" : "jjlcyw" ,
                "术前解救治疗过程评估" : "sqzlpg" ,
                "术前解救治疗疗效评价" : "sqzlpj" ,


            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['xfzzlkssj'] = df['xfzzlkssj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['sqzlkssj'] = df['sqzlkssj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = clinicalFeature(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    def batch_add_recorder_info(self, filename):
        """记录人员信息表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "首次录入人" : "sclrr",
                "首次录入时间" : "sclrsj",
                "末次随访人" : "mcsfr",
                "末次随访时间" : "mcsfsj",

            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['sclrsj'] = df['sclrsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['mcsfsj'] = df['mcsfsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = recorderInformation(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
        
    def batch_add_gene21(self, filename):
        """21基因信息表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "是否进行21基因检测" : "sfjx21jyjc",
                "检测时间" : "jcsj",
                "研究编号" : "yjbh",
                "检测人员" : "jcry",
                "标本位置" : "bbwz",
                "备注" : "bz",
                "具体详情" : "jtxq",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['jcsj'] = df['jcsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = gene21Detection(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    def batch_add_gene70(self, filename):
        """70基因信息表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "是否进行70基因检测" : "sfjx70jyjc",
                "检测时间" : "jcsj",
                "研究编号" : "yjbh",
                "检测人员" : "jcry",
                "标本位置" : "bbwz",
                "备注" : "bz",
                "具体详情" : "jtxq",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['jcsj'] = df['jcsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = gene70Detection(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
        
    
    def batch_add_genebrca(self, filename):
        """BRCA基因信息表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "是否进行BRCA基因检测" : "sfjxbrcajyjc",
                "检测时间" : "jcsj",
                "研究编号" : "yjbh",
                "检测人员" : "jcry",
                "标本位置" : "bbwz",
                "备注" : "bz",
                "具体详情" : "jtxq",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['jcsj'] = df['jcsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = genebrcaDetection(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    def batch_add_patient_follow(self, filename):
        """病人跟踪记录表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "DFS" : "dfs",
                "OS" : "os",
                "末次复查时间（截止查病历时/电话随诊）" : "mcfcsj",
                "治疗后生育情况" : "syqk",
                "双原发癌症" : "syfaz",
                "双原发癌症具体详情" : "syfazjtxq",
                # "双原发癌症首次发生时间" : "zhsfsj",
                "随访备注" : "sfbz",
                "死亡与否" : "swyf",
                "死亡时间" : "swsj",
                "死因" : "sy",
                "具体死因" : "jtsy",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['swsj'] = df['swsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['mcfcsj'] = df['mcfcsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            # df['zhsfsj'] = df['zhsfsj'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = patientFollow(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    def batch_add_peripheral_blood(self, filename):
        """外周血标本

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "标本类型" : "bblx" ,
                "采血时间点" : "cxsjd" ,
                "采集人" : "cjr" ,
                "采集备注" : "cjbz" ,
                "采集用途" : "cjyt" ,
                "标本编码" : "ybid" ,
                "标本量" : "ybnum" ,
                "标本盒编码" : "ybhbh" ,
                "标本存放位置" : "ybcfwz" ,
                "是否取用" : "sfqy" ,
                "取用日期" : "qyrq" ,
                "取用人" : "qyr" ,
                "取用用途" : "qyyt" ,
                "取用备注" : "qybz" ,
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['cxsjd'] = df['cxsjd'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['qyrq'] = df['qyrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = peripheralBloodSampleSampling(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    

    def batch_add_recurrent(self, filename):
        """远处转移信息表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "第几次转移" : "djczy",
                "远处转移部位" : "yzzybw",
                "远处转移日期" : "yczyrq",
                "远处转移确诊手段" : "yczyqzsd",
                "远处转移病理信息" : "yzzyblxx",
                "远处转移免疫组化" : "yzzymyzh",
                "远处转移治疗" : "yczyzl",
                "远处转移治疗效果评价" : "yczyzlxgpj",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['djczy'] = df['djczy'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['yczyrq'] = df['yczyrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = recurrentDistantMetastasis(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
        
    
    def batch_add_previous_history(self, filename):
        """既往史表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "乳腺良性疾病史" : "rxlxjbs" ,
                "乳腺良性疾病史具体情况" : "rxlxjbsjtqk" ,
                "感染性疾病" : "grxjb" ,
                "感染性疾病具体情况" : "grxjbjtqk" ,
                "新冠阳性日期" : "xgyxrq" ,
                "新冠转阴日期" : "xgzyrq" ,
                "新冠转阴确诊方式" : "xgzyqzfs" ,
                "是否有系统疾病" : "xtxjb" ,
                "系统疾病具体情况" : "xtjbjtqk" ,
                "是否有手术史" : "sss" ,
                "手术史具体情况" : "sssjtqk" ,
                "是否有恶性肿瘤既往史" : "exzl" ,
                "恶性肿瘤既往史具体情况" : "exzljtqk"

            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['xgyxrq'] = df['xgyxrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['xgzyrq'] = df['xgzyrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = PreviousHistory(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    def batch_add_relapse_info(self, filename):
        """复发信息表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "第几次复发" : "djcff",
                "复发部位" : "ffbw",
                "具体复发部位" : "jtffbw",
                "复发日期" : "ffrq",
                "复发确诊手段" : "ffqzsd",
                "复发病灶病理信息" : "ffbzblxx",
                "复发病灶免疫组化" : "ffbzymzh",
                "复发后治疗" : "ffhzl",
                "复发后治疗效果评价" : "ffxgpj",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['djcff'] = df['djcff'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['ffrq'] = df['ffrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = relapseInformation(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
        
    def batch_add_specimens(self, filename):
        """复发转移灶标本采样表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "关联病灶" : "glbz",
                "采样日期" : "cyrq",
                "用途标识" : "ytbz",
                "其他用途" : "qtyt",
                "采集人" : "cjr",
                "标本类型" : "bblx",
                "标本性质" : "bbxz",
                "标本编码" : "ybid",
                "标本量" : "ybnum",
                "标本盒编码" : "ybhbh",
                "标本存放位置" : "ybcfwz",
                "是否取用" : "sfqy",
                "取用日期" : "qyrq",
                "取用人" : "qyr",
                "取用用途" : "qyyt",
                "取用备注" : "qybz",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['cyrq'] = df['cyrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['qyrq'] = df['qyrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = samplingRecurrenceMetastasisSpecimens(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}
    
    def batch_add_pathological(self, filename):
        """手术病理信息表

        Args:
            filenames (str): 文件
        """
        try:
            name_dict = {
                "滨海住院号" : "bhzyid",
                "河西住院号" : "hxzyid",
                "手术日期" : "ssrq",
                "手术方式" : "ssfs",
                "是否保乳" : "sfbr",
                "是否再造" : "sfzz",
                "腋窝淋巴结清扫方式" : "ywlbqsfs",
                "术后大病理号" : "shdblh",
                "病灶数量" : "bzsl",
                "肉眼肿物大小" : "ryzwdx",
                "病理学分期" : "blxfq",
                "病理类型" : "bllx",
                "病理具体描述" : "blxjtms",

                "组织学分级" : "zzxfj",
                "组织学分级具体情况" : "zzxfjjtqk",
                "淋巴血管侵犯与否" : "lbxgqf",
                "淋巴管癌栓" : "lbgbs",
                "间质内浸润淋巴细胞" : "jzznqrlbxb",
                "化疗反应" : "hlfy",
                "保乳手术标本周断端是否可见癌组织" : "brsskjazz",
                "保乳手术标本周断端" : "brssbbzdd",
                "保乳手术标本补切周断端" : "brssbbbqzdd",

                "淋巴结情况" : "lbjqk",
                "腋窝淋巴结总数" : "ywlbzs",
                "阳性腋窝淋巴结数" : "yxywlbzs",
                "ER" : "er",
                "PR" : "pr",
                "HER2" : "her2",
                "her2具体情况" : "her2jtqk",
                "Ki67" : "ki67",
                "P53" : "p53",
                "FISH" : "fish",
                "FISH具体情况" : "fishjtqk",
                "HER2-FISH COPY数" : "hfc",
                "HER2-FISH RATIO" : "hfr",
            }
            df = upload_excel(filename, name_dict)
            df.fillna("", inplace=True)
            # 替换非varchar类型空串""为None
            df['bhzyid'] = df['bhzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['hxzyid'] = df['hxzyid'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['ssrq'] = df['ssrq'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['bzsl'] = df['bzsl'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['ywlbzs'] = df['ywlbzs'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)
            df['yxywlbzs'] = df['yxywlbzs'].replace({pd.NaT: None, np.NaN: None, '': None}, method=None)

            status = 200
            msg = "批量导入成功" 
            valid_num = 0
            rst_data = df.to_dict(orient='records')
            for row in rst_data:
                if row["hxzyid"] is None and row["bhzyid"] is None:
                    continue
                p = surgicalPathologicalInfo(**row)
                g.db_session.add(p)
                valid_num += 1
            g.db_session.commit()
        except Exception as e:
            status = 400
            msg = "批量导入失败，失败原因[{}]".format(e)
            valid_num = 0
            print(e)
        finally:
            return {"status" : status, "message" : msg, "valid_num" : valid_num}