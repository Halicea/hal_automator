from cherrypy import wsgiserver
from app import app

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 5001), d)
def run_server():
  server.start()

if __name__ == '__main__':
  try:
    server.start()
  except KeyboardInterrupt:
    server.stop()