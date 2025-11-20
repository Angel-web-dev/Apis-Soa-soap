from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class HelloService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hola {name} desde SOAP"

app = Application([HelloService], 'soap.example',
                  in_protocol=Soap11(), out_protocol=Soap11())

wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8001, wsgi_app)
    print("SOAP corriendo en http://localhost:8001")
    server.serve_forever()
