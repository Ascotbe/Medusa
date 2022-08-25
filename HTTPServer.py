# !/usr/bin/env python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
from Web.DatabaseHub import DomainNameSystemLog
import base64
from ClassCongregation import ErrorLog
class Server(BaseHTTPRequestHandler):
    def Response(self):
        try:
            self.response_headers=""
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            for i in self._headers_buffer:
                self.response_headers+=str(i.decode("utf-8"))
            self.end_headers()
        except Exception as e:
            ErrorLog().Write(e)

    def do_GET(self):
        try:
            Request=str(self.requestline)+"\n"+str(self.headers)
            self.Response()
            DomainNameSystemLog().Write(ip="", domain_name="", type="http", response=base64.b64encode(self.response_headers.encode('utf-8')), request=base64.b64encode(Request.encode('utf-8')))
            #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        except Exception as e:
            ErrorLog().Write(e)
    def do_POST(self):
        try:
            ContentLength = int(self.headers['Content-Length'])  # <--- Gets the size of data
            PostData = self.rfile.read(ContentLength)  # <--- Gets the data itself
            Request=str(self.requestline)+"\n"+str(self.headers)+"\n"+PostData.decode("utf-8")
            self.Response()
            DomainNameSystemLog().Write(ip="", domain_name="", type="http", response=base64.b64encode(self.response_headers.encode('utf-8')), request=base64.b64encode(Request.encode('utf-8')))
            #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        except Exception as e:
            ErrorLog().Write(e)


if __name__ == '__main__':
    try:
        ServerAddress = ('0.0.0.0', 8888)
        Httpd = HTTPServer(ServerAddress, Server)
        Httpd.serve_forever()
    except Exception as e:
        ErrorLog().Write(e)