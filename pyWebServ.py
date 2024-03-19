#!python



import http.server
import socketserver
import requests

PORT = 8000
handler = http.server.CGIHTTPRequestHandler

with http.server.HTTPServer(("", PORT), handler) as httpd:
    print(f"Server starting on port {PORT}")
    httpd.serve_forever()