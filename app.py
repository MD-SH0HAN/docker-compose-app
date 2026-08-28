from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello from the SHOHAN backend container!"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Backend listening on port 8000")
server.serve_forever()
