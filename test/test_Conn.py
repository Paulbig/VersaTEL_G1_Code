import pytest
import Conn


class TestFTPConn:

    def setup_class(self):
        engineip = '10.203.1.6'
        ftp_port = 21
        user = 'adminftp'
        password = ''
        timeout = 1.5
        self.ftp = Conn.FTPConn(engineip, ftp_port, user, password, timeout)

    def test_FTPconnect(self):
        assert self.ftp._FTPconnect() == True

    def test_GetFile(self):
        remote = 'ftp_data_20200618_170728.txt'
        local = 'Trace_10.203.1.6_Secondary.log'
        assert self.ftp.GetFile('mbtrace', '.', remote, local) == True

    def test_PutFile(self):
        pass

    def test_close(self):
        assert self.ftp.close() == None
        assert self.ftp._Connection == None


class TestSSHConn:

    def setup_class(self):
        switchip = '10.203.1.9'
        ssh_port = 22
        user = 'admin'
        password = 'Feixi@123'
        timeout = 2
        self.ssh = Conn.SSHConn(switchip, ssh_port, user, password, timeout)

    def test_connect(self):
        assert self.ssh.SSHConnection

    def test_ssh_connect(self):
        assert self.ssh.ssh_connect() == None

    def test_exctCMD(self):
        assert self.ssh.exctCMD('pwd') == '/fabos/users/admin\n'

    def test_close(self):
        pass
        # assert self.ssh.close() == None
        # assert self.ssh.ssh_connect == None


class TestHAAPConn:

    def setup_class(self):
        engineip = '10.203.1.6'
        haap_port = 23
        password = ''
        timeout = 1.5
        self.haap = Conn.HAAPConn(engineip, haap_port, password, timeout)

    def test_connect(self):
        assert self.haap._connect_retry()

    def test_telnet_connect(self):
        assert self.haap.telnet_connect() == None

    def test_get_connection_status(self):
        assert self.haap.get_connection_status()

    def test_is_AH(self):
        assert self.haap.is_AH() == 0

    def test_exctCMD(self):
        data = self.haap.exctCMD('vpd')
        assert 'Engine VPD' in data

    def test_Close(self):
        assert self.haap.Close() == None
