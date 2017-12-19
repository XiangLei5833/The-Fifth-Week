from rmon.models import Server

class TestServer:
    ''' 测试 Server 相关功能 '''

    def test_save(self, db):
        assert Server.query.count() == 0
        server = Server(name='test', host='127.0.0.1')
        server.save()  
        assert Server.query.count() == 1  
        assert Server.query.first() == server

    def test_delete(self, db, server):
        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0


    def test_ping_success(self, db, server):
        ''' 测试 Server.ping 方法执行成功 '''
        assert server.ping() is True

    def test_ping_failed(self, db):
        ''' 测试 Server.ping 方法执行失败 '''
        server = Server(name='test', host='127.0.0.1', port=6399)
        try:
            server.ping()
        except ResException as e:
            assert e.code == 400
            assert e.message == 'redis server %s can not connected' % server.host

