import os
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 5000

name = os.getenv("NAME", "Abdulkadir Osman")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = f"Hello {name}! Docker container is running."
        self.wfile.write(message.encode())

if __name__ == "__main__":
    print("Server started on port", PORT)
    server = HTTPServer((HOST, PORT), Handler)
    server.serve_forever()
