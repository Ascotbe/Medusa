# !/usr/bin/env python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
from Web.DatabaseHub import DomainNameSystemLog
import base64
class Server(BaseHTTPRequestHandler):
    def Response(self):
        self.response_headers=""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        for i in self._headers_buffer:
            self.response_headers+=str(i.decode("utf-8"))
        self.end_headers()

    def do_GET(self):
        Request=str(self.requestline)+"\n"+str(self.headers)
        self.Response()
        DomainNameSystemLog().Write(ip="", domain_name="", type="http", response=base64.b64encode(self.response_headers.encode('utf-8')), request=base64.b64encode(Request.encode('utf-8')))
        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
    def do_POST(self):
        ContentLength = int(self.headers['Content-Length'])  # <--- Gets the size of data
        PostData = self.rfile.read(ContentLength)  # <--- Gets the data itself
        Request=str(self.requestline)+"\n"+str(self.headers)+"\n"+PostData.decode("utf-8")
        self.Response()
        DomainNameSystemLog().Write(ip="", domain_name="", type="http", response=base64.b64encode(self.response_headers.encode('utf-8')), request=base64.b64encode(Request.encode('utf-8')))
        #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


if __name__ == '__main__':
    ServerAddress = ('0.0.0.0', 8888)
    Httpd = HTTPServer(ServerAddress, Server)
    Httpd.serve_forever()