from http.server import BaseHTTPRequestHandler, HTTPServer


class handler1(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(404)
            self.end_headers()
        else:
            print("path:", self.path)
            print(self.request)
            print(self.headers)
            self.send_response(200)
            #self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"hello1\n")


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    print("listen to 8000...")
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__=="__main__":
    run(handler_class=handler1)