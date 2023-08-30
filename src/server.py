from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import hashlib
import os
import subprocess

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query string
        query_string = self.path.split("?", 1)[-1]
        params = parse_qs(query_string)
        # Generate a hash of the parameters as filename
        hash = hashlib.md5(f"{params['text'][0]}{params['model'][0]}".encode()).hexdigest()
        wav_file = f"/app/generated/{hash}.wav"
        # Check if a file already exists before generating one with piper
        if not os.path.exists(wav_file):
            print(f"Generating file... {hash}.wav")
            command = f"echo \"{params['text'][0]}\" | piper -f /app/generated/{hash}.wav -m {params['model'][0]}"
            subprocess.run(command, shell=True)
        # Return the filename after generation by piper
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"{hash}.wav".encode())
        
# Start the serverdc
print("Starting server...")
server = HTTPServer(("", 8000), MyHandler)
server.serve_forever()
print("Server started!")