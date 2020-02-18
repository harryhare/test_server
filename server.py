from http.server import BaseHTTPRequestHandler, HTTPServer


class handler1(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/favicon.ico":
            print("path:", self.path)
            print(self.request)
            print(self.headers)
            self.wfile.write(b"hello")


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    print("listen to 8000...")
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__=="__main__":
    run(handler_class=handler1)