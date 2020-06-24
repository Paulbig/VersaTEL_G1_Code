import Sundry as sun
import HAAP as haap
import pytest
import datetime
import time
import os
import xlwt


def test_time_now_folder():
    assert sun.time_now_folder()


def test_time_now_to_show():
    assert sun.time_now_to_show()


def test_is_Warning():
    assert sun.is_Warning(500, 200) == True
    assert sun.is_Warning(500, 2000) == None
    assert sun.is_Warning(100, [200, 2000]) == 0
    assert sun.is_Warning(600, [200, 2000]) == 1
    assert sun.is_Warning(3000, [200, 2000]) == 2


def test_is_trace_level():
    assert sun.is_trace_level(0) == None
    assert sun.is_trace_level(1) == True


def test_is_IP():
    assert sun.is_IP('10.203.1.1') == True
    assert sun.is_IP('6.6.6.256') == False


def test_is_file():
    assert sun.is_file('Sundry.py') == True
    assert sun.is_file('test_Sundry.py') == False


def test_is_folder():
    assert sun.is_folder('test') == True
    assert sun.is_folder('pytest') == False


def test_is_port():
    assert sun.is_port('789') == True
    assert sun.is_port(789) == True
    assert sun.is_port('a789') == False


def test_ShowErr():
    pass
    # assert sun.ShowErr('a','b','c','d') == None


def test_GotoFolder():
    fold = sun.GotoFolder('testa')
    assert fold == True
    if fold:
        try:
            os.chdir('../')
            os.removedirs('testa')
        except:
            pass


class TestTiming:

    def setup_class(self):
        self.timing = sun.Timing()

    def a(self):
        print('aaaaaa')

    def test_add_interval(self):
        assert self.timing.add_interval(self.a, 3) == None

    def test_stt(self):
        assert self.timing.stt() == None

    def test_stp(self):
        assert self.timing.stp() == None


class TestTimeNow:

    def setup_class(self):
        self.time = sun.TimeNow()
        self.timenow = time.localtime()

    def test_y(self):
        assert self.time.y() == self.timenow[0]

    def test_mo(self):
        assert self.time.mo() == self.timenow[1]

    def test_d(self):
        assert self.time.d() == self.timenow[2]

    def test_h(self):
        assert self.time.h() == self.timenow[3]

    def test_mi(self):
        assert self.time.mi() == self.timenow[4]

    def test_s(self):
        assert self.time.s() == self.timenow[5]

    def test_wd(self):
        assert self.time.wd() == self.timenow[6]


class TestTraceAnalyse:

    def setup_class(self):
        haap.get_trace_all(3)
        os.chdir('Trace')
        pwd = os.getcwd()
        ls = os.listdir(pwd)
        self.trace = ls[-1]
        self.analyse = sun.TraceAnalyse(self.trace)

    def test_run(self):
        assert self.analyse.run() == None

    def test_get_trace_file_list(self):
        os.chdir(self.trace)
        file = self.analyse._get_trace_file_list()
        assert file[0] == 'Trace_10.203.1.6_Secondary.log'
        assert file[1] == 'Trace_10.203.1.6_Primary.log'
        assert file[2] == 'Trace_10.203.1.6_Trace.log'
        os.chdir('../')

    def test_analyse_file(self):
        assert self.analyse._analyse_file() == None

    def test_find_error(self):
        assert self.analyse._find_error(
            '%s/Trace_10.203.1.6_Secondary.log' % self.trace) == None

    def test_generate_excel_file_name(self):
        assert self.analyse._generate_excel_file_name(
            'Trace_10.203.1.6_Secondary.log') == 'TraceAnalyze_Trace_10.203.1.6_Secondary.xls'

    def test_write_to_excel(self):
        pass
        # objExcel = xlwt.Workbook()
        # assert self.analyse._write_to_excel(objExcel, 'abts_received', '')

    def test_read_file(self):
        assert self.analyse._read_file(
            'Trace_10.203.1.6_Secondary.log') == None
