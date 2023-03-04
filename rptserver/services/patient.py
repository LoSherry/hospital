import logging

from flask import g

from rptserver.database.sqlal import func_to_char
from rptserver.model.patient import Patient,PreviousHistory,recurrentDistantMetastasis,samplingRecurrenceMetastasisSpecimens,recorderInformation,peripheralBloodSampleSampling, gene21Detection,gene70Detection,genebrcaDetection, relapseInformation, postoperativeTreatment, patientMarryHistory,patientFollow, patientMenstruationHistory, surgicalPathologicalInfo,familyHistory, patientHistory, clinicalFeature
from rptserver.tools.utils import is_id_number
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

    
    def getDetail(self, id):
        query = g.db_session.query(Patient).filter(Patient.id == id)
        rst = {}
        if(query.count() > 0):
            rst = query.first()
        
        return rst
    
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
                'qs' : qst.qs,
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
                
                "xfzzlkssj" : qst.xfzzlkssj.strftime('%Y-%m-%d'),
                "xfzzlfa" : qst.xfzzlfa,
                "xfzzlpg" : qst.xfzzlpg,
                "xfzzlpj" : qst.xfzzlpg,
                
                "sqzlkssj" : qst.sqzlkssj.strftime('%Y-%m-%d'),
                "sqzlfa" : qst.sqzlfa,
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