# !/usr/bin/env python
# -*- coding: utf-8 -*-
import socketserver
import struct
from Web.WebClassCongregation import DomainNameSystemLog
from ClassCongregation import ErrorLog
# DNS Query
class DNSQuery:
    def __init__(self, data):
        i = 1
        self.name = ''
        while True:
            d = int(data[i])
            if d == 0:
                break
            if d < 32:
                self.name = self.name + '.'
            else:
                self.name = self.name + chr(d)
            i = i + 1
        self.querybytes = data[0:i + 1]
        (self.type, self.classify) = struct.unpack('>HH', data[i + 1:i + 5])
        self.len = i + 5

    def getbytes(self):
        return self.querybytes + struct.pack('>HH', self.type, self.classify)


# DNS Answer RRS
class DNSAnswer:
    def __init__(self, ip):
        self.name = 49164
        self.type = 1
        self.classify = 1
        self.timetolive = 190
        self.datalength = 4
        self.ip = ip

    def getbytes(self):
        try:
            res = struct.pack('>HHHLH', self.name, self.type, self.classify, self.timetolive, self.datalength)
            s = self.ip.split('.')
            res = res + struct.pack('BBBB', int(s[0]), int(s[1]), int(s[2]), int(s[3]))
            return res
        except Exception as e:
            ErrorLog().Write("DomainNameSystemServer_DNSAnswer(class)_getbytes(def)", e)

# DNS frame
class DNSFrame:
    def __init__(self, data):
        (self.id, self.flags, self.quests, self.answers, self.author, self.addition) = struct.unpack('>HHHHHH',
                                                                                                     data[0:12])
        self.query = DNSQuery(data[12:])

    def getname(self):
        return self.query.name

    def setip(self, ip):
        self.answer = DNSAnswer(ip)
        self.answers = 1
        self.flags = 33152

    def getbytes(self):
        try:
            res = struct.pack('>HHHHHH', self.id, self.flags, self.quests, self.answers, self.author, self.addition)
            res = res + self.query.getbytes()
            if self.answers != 0:
                res = res + self.answer.getbytes()
            return res
        except Exception as e:
            ErrorLog().Write("DomainNameSystemServer_DNSFrame(class)_getbytes(def)", e)

# A UDPHandler to handle DNS query
class DNSUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            data = self.request[0].strip()
            dns = DNSFrame(data)
            socket = self.request[1]
            namemap = DNSServer.namemap
            if (dns.query.type == 1):
                # If this is query a A record, thenresponse it
                name = dns.getname()
                toip = namemap['*']
                dns.setip(toip)
                DomainNameSystemLog().Write(ip=self.client_address[0],domain_name=name)
                #print('%s:%s-->%s' % (self.client_address[0], name, toip))
                socket.sendto(dns.getbytes(), self.client_address)
            else:
                # If this is notquery a A record, ignore it
                socket.sendto(data, self.client_address)

        except Exception as e:
            ErrorLog().Write("DomainNameSystemServer_DNSUDPHandler(class)_getbytes(def)", e)


# DNS Server
class DNSServer:
    def __init__(self, port=53):
        DNSServer.namemap = {}
        self.port = port

    def addname(self, name, ip):
        DNSServer.namemap[name] = ip

    def start(self):
        HOST, PORT = "0.0.0.0", self.port
        server = socketserver.UDPServer((HOST, PORT), DNSUDPHandler)
        server.serve_forever()



if __name__ == '__main__':
    sev = DNSServer()
    sev.addname('*', '127.0.0.1')  # default address
    sev.start()