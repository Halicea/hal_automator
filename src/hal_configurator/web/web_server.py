from cherrypy import wsgiserver
from app import app

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = None 
def run_server(port):
  server  = wsgiserver.CherryPyWSGIServer(('0.0.0.0', port), d)
  server.start()

if __name__ == '__main__':
  try:
    run_server(5001)
  except KeyboardInterrupt:
    server.stop()