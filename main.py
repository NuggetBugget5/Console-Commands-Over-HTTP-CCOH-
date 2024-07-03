import hashlib, os, json, re
from http.server import BaseHTTPRequestHandler, HTTPServer

os.chmod("./Webview/index.html", 0o700)  # Set the appropriate file permissions


class RequestHandler(BaseHTTPRequestHandler):

  def _set_headers(self, content_type='text/html'):
    self.send_response(200)
    self.send_header('Content-type', content_type)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods',
                     'GET, POST, PUT, DELETE, OPTIONS')
    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    self.end_headers()

  def do_OPTIONS(self):
    self._set_headers()
    self.send_response(200, "ok")

  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    parsed_data = json.loads(post_data.decode())
    try:
      command = parsed_data.get('command', '')
      hash = hashlib.sha256(command[-64].encode())
      print(hash.hexdigest())
      with open("./Hash/hash.key", "r") as file:
        if command and re.search(file.read(), hash.hexdigest()):
          file.close()
          result = os.popen(command[:-64]).read()  # Run command and read output
          self._set_headers(content_type='application/json')
          response = {'output': result}
          self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
          file.close()
          self.send_error(400, 'Invalid command or incorrect password')
    except Exception as e:
      self.send_error(500, str(e))

  def do_GET(self):
    try:
      with open("./Webview/index.html", "r") as file:
        html = file.read()
        self._set_headers()
        self.wfile.write(html.encode('utf-8'))
        file.close()
    except:
      self.send_error(404)
      self.end_headers()


def run(server_class=HTTPServer, handler_class=RequestHandler, port=443):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Starting httpd on port {port}...')
  httpd.serve_forever()


if __name__ == '__main__':
  run()