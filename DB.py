# coding:utf-8

import datetime

from mongoengine import Document, connect
from mongoengine.fields import *

import GetConfig as gc
import HAAP as haap
import SANSW as sw
import Sundry as s

# <<<read config >>>
cfgDB = gc.DBConfig()
strDBName = cfgDB.name()
strDBHost = cfgDB.host()
intDBPort = cfgDB.port()
# <<<read config >>>

# connet to the datebase
connect(strDBName, host=strDBHost, port=intDBPort)


def haap_insert(time, origin, info):
    """
    @note: monitoHAAP数据插入
    """
    HAAP().insert(time, origin, info)


def haap_last_record():
    """
    @note: HAAP最后一次所有的数据
    """
    return HAAP().query_last_records()


# SANSW
def switch_insert(time, origin, sum_total, dicPEFormated):
    """
    @note: SANSW数据插入
    """
    SANSW().insert(time, origin, sum_total, dicPEFormated)


def switch_last_info():
    """
    @note: SANSW最后一次所有的数据
    """
    return SANSW().query_last_records()


# Warning
def insert_warning(time, ip, device, level, warn_message, confirm):
    """
    @note: warning数据插入
    """
    Warning().insert(time, ip, device, level,
                     warn_message, confirm)


def update_warning():
    """
    @note: 更新warning数据库
    """
    Warning().update_Warning()


def get_unconfirm_warning():
    """
    @note: warning网页部分展示
    """
    lstAllUCW = []
    for warning in Warning().get_all_unconfirm_warning():
        lstAllUCW.append([warning.time, warning.ip, warning.device,
                          warning.level, warning.warn_message])
    if lstAllUCW:
        return lstAllUCW


class collHAAP(Document):
    time = DateTimeField(default=datetime.datetime.now())
    origin = DictField()
    info = DictField()


class collSANSW(Document):
    # ptes = port error show info formatted
    time = DateTimeField(default=datetime.datetime.now())
    origin = DictField()
    ptes = DictField()
    sum_total = DictField()


class collWarning(Document):
    time = StringField()
    level = IntField()
    device = StringField()
    ip = StringField()
    warn_message = StringField()
    confirm = IntField()


class HAAP(object):

    def insert(self, time, origin, info):
        t = collHAAP(time=time, origin=origin, info=info)
        t.save()

#     获取引擎一段时间数据，暂未使用，后续可能使用
#     def query_range(self, time_start, time_end):
#         return collHAAP.objects(date__gte=time_start,
#                          date__lt=time_end).order_by('-date')

    def query_last_records(self):
        return collHAAP.objects().order_by('-time').first()


class SANSW(object):

    def insert(self, time, origin, sum_total, ptes):
        t = collSANSW(time=time, origin=origin,
                      sum_total=sum_total, ptes=ptes,)
        t.save()

#     获取SAN交换机一段时间数据，暂未使用，后续可能使用
#     def query_range(self, time_start, time_end):
#         return collSANSW.objects(date__gte=time_start,
#                           date__lt=time_end).order_by('-date')

    def query_last_records(self):
        return collSANSW.objects().order_by('-time').first()


class Warning(object):

    def insert(self, time_now, lstip, device, lstdj, lstSTS, confirm):
        t = collWarning(time=time_now, ip=lstip, device=device, level=lstdj,
                        warn_message=lstSTS, confirm=confirm)
        t.save()

#     获取Warning一段时间数据，暂未使用，后续可能使用
#     def query_range(self, time_start, time_end):
#         return collWarning.objects(date__gte=time_start,
#                             date__lt=time_end).order_by('-date')

    def query_last_records(self):
        return collWarning.objects().order_by('-time').first()

    def get_all_unconfirm_warning(self):
        warning_status = collWarning.objects(confirm=0)
        return warning_status

    def update_Warning(self):
        return collWarning.objects(confirm=0).update(confirm=1)


if __name__ == '__main__':
    pass
