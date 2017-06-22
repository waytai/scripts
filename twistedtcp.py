import os
import pdb
if os.name!='nt':
    from twisted.internet import epollreactor
    epollreactor.install()    
else:
    from twisted.internet import iocpreactor
    iocpreactor.install()
from twisted.internet.protocol import Factory,Protocol
from twisted.internet import reactor
client_socks = []

class gameSocket(Protocol):
    def __init__(self):
        print "777"

    def connectionMade(self):
        print 'New Client'
        #pdb.set_trace()
        client_socks.append(self.transport.socket)

    def connectionLost(self,reason):
        print 'Lost Client'

    def dataReceived(self, data):
        print 'Get data:' + str(data)


        server_ip_port = self.transport.server.getHost()
        server_ip = server_ip_port.host
        server_port = server_ip_port.port
        print "="*20, server_ip, server_port

        client_ip_port = self.transport.client
        client_ip = client_ip_port[0]
        client_port = str(client_ip_port[1])

        print "%"*10, client_socks 

        print "="*20, client_ip, client_port
        self.transport.write('bingo!i got your msg:'+ str(data))
if __name__=='__main__':
    f = Factory()
    f.protocol = gameSocket
    reactor.listenTCP(8001,f)
    print 'server started...'
    reactor.run()
