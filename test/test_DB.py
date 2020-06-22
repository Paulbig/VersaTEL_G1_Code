import pytest
import DB
import datetime
import HAAP as haap
import SANSW as sw

time = datetime.datetime.now()
timeshow = time.strftime('%Y-%m-%d %H:%M:%S')
Origin, Info = haap.data_for_db()
origin, total, dic = sw.get_info_for_DB()
ip = '10.203.1.6'
device = 'engine0'
level = 2
warn = 'Engine AH'
confirm = 0


def test_haap_insert():
    assert DB.haap_insert(time, Origin, Info) == None


def test_haap_last_record():
    assert DB.haap_last_record()


def test_switch_insert():
    assert DB.switch_insert(time, origin, total, dic) == None


def test_switch_last_info():
    assert DB.switch_last_info()


def test_insert_warning():
    assert DB.insert_warning(timeshow, ip, device,
                             level,  warn, confirm) == None


def test_update_warning():
    assert DB.update_warning() == None


def test_get_unconfirm_warning():
    assert DB.get_unconfirm_warning() == None


class TestHAAP:

    def setup_class(self):
        self.haap = DB.HAAP()

    def test_insert(self):
        assert self.haap.insert(time, Origin, Info) == None

    def test_query_last_record(self):
        assert self.haap.query_last_record()


class TestSANSW:

    def setup_class(self):
        self.sw = DB.SANSW()

    def test_insert(self):
        assert self.sw.insert(time, origin, total, dic) == None

    def test_query_last_records(self):
        assert self.sw.query_last_records()


class TestWarning:

    def test_insert(self):
        assert DB.Warning().insert(timeshow, ip, device, level, warn, confirm) == None

    def test_query_last_records(self):
        assert DB.Warning().query_last_records()

    def test_get_all_unconfirm_warning(self):
        assert DB.Warning().get_all_unconfirm_warning()

    def test_update_Warning(self):
        assert DB.Warning().update_Warning()
