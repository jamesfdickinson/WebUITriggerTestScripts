# Python 3 server example which executes a function based on a POST request
import tool

from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if(self.path == "/"):
            f = open("index.html").read()
            self.wfile.write(bytes(f, 'utf-8'))

    def do_POST(self):
        #set header
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        #echo back
        response = BytesIO()
        response.write(b'This is POST request.  Received: ' + body)
        self.wfile.write(response.getvalue())
        #do something
        value = body.decode()
        if(value == "Test1"):
            tool.testSound1()
        if(value == "Test2"):
            tool.testSound2()




if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")





