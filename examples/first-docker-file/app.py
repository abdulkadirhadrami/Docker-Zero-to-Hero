from http.server import BaseHTTPRequestHandler, HTTPServer

host = "0.0.0.0"
port = 5000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(b"Hello Abdulkadir! Docker container is running")

server = HTTPServer((host, port), MyHandler)

print("Server running on port 5000...")
server.serve_forever()
