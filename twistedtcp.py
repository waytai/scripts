import os
if os.name!='nt':
    from twisted.internet import epollreactor
    epollreactor.install()    
else:
    from twisted.internet import iocpreactor
    iocpreactor.install()
from twisted.internet.protocol import Factory,Protocol
from twisted.internet import reactor
class gameSocket(Protocol):
    def connectionMade(self):
        print 'New Client'
    
    def connectionLost(self,reason):
        print 'Lost Client'
    
    def dataReceived(self, data):
        print 'Get data:' + str(data)
        self.transport.write('bingo!i got your msg:'+ str(data))
if __name__=='__main__':
    f = Factory()
    f.protocol = gameSocket
    reactor.listenTCP(8001,f)
    print 'server started...'
    reactor.run()
