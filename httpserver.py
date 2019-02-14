#!/usr/bin/env python3

import http.server
import socketserver
import os

PORT = int(os.environ.get('EVAL_PORT', '9000'))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
