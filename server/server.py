__author__='rresol'
__email__ = 'shashank.kumar.apc13@itbhu.ac.in'


from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import searcher
import time

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

class GetHandler(BaseHTTPRequestHandler):
    
    #Server can handle the HTTP Request on its own . We need to define methods ...Do_Get Serve for GET method.

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        try:
            message = searcher.search(parsed_path.query)    #query passed into the searcher . make sure to prefix your queries by '?' i browser.
            self.send_response(200)                         #marking the end of response by blank line                         
            self.end_headers()  
            self.wfile.write(message)                       # Writing the data to a output file
        except:
            raise 404       
        return


if __name__ == '__main__':
    import BaseHTTPServer
    server_class = BaseHTTPServer.HTTPServer            #Server Subclassed with HTTPServer.
    httpd = server_class((HOST_NAME,PORT_NUMBER),GetHandler)
    print time.asctime(), "Server Starts - localhost:8000 "
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime() ,"Server stops - localhost:8000"
