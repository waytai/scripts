#!/usr/bin/env python
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from __future__ import print_function

from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver



class EchoClient(LineReceiver):
    end = "\n"

    def connectionMade(self):
        print("-"*30) 
        self.transport.write('\n116\n{"CMD":"JOIN","CmdSeq":1,"AppEUI":"2C26C501E8000001","AppNonce":1234,"Challenge":"ABCDEF1234567890ABCDEF1234567890"}\n')
        #self.sendLine('\n116\n{"CMD":"JOIN","CmdSeq":1,"AppEUI":"2C26C501E8000001","AppNonce":1234,"Challenge":"ABCDEF1234567890ABCDEF1234567890"}\n')
        print("-"*30) 


    def lineReceived(self, line):
        print("*"*30) 
        print("receive:", line)
        if line == self.end:
            self.transport.loseConnection()



class EchoClientFactory(ClientFactory):
    protocol = EchoClient

    def __init__(self):
        self.done = Deferred()


    def clientConnectionFailed(self, connector, reason):
        print('connection failed:', reason.getErrorMessage())
        self.done.errback(reason)


    def clientConnectionLost(self, connector, reason):
        print('connection lost:', reason.getErrorMessage())
        self.done.callback(None)



def main(reactor):
    factory = EchoClientFactory()
    reactor.connectTCP('XXX.com', 10002, factory)
    return factory.done



if __name__ == '__main__':
    task.react(main)
