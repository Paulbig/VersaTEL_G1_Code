import pytest
import SendEmail

E = SendEmail.Email()

class TestEmail():

    def test_get_msg(self):
        assert E.get_msg('pytest', 'test')

    def test_prepare(self):
        assert E.prepare()

    def test_anonymous_prepare(self):
        assert E.anonymous_prepare()

    def test_send_email(self):
    	assert E.send_email('pytest', 'test') == None


def testfunc():
	return

def test_switch():
	switch = SendEmail.email_switch(testfunc())
	assert switch


def test_send_warnmail():
	info = [['2020-06-01 11:36:42', '10.203.1.4', 'engine1', 2, 'Engine reboot 6674 secends ago']]
	assert SendEmail.send_warnmail(info) == None

def test_send_test():
	assert SendEmail.send_test() == None

def test_send_live():
	assert SendEmail.send_live() == None
