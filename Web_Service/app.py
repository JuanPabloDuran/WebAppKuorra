#Author : Salvador Hernandez Mendoza
#Email  : salvadorhm@gmail.com
#Twitter: @salvadorhm
import web
import application

ssl = False #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    '''
    Use OpenSSL to generate  keys

    user@host$ openssl genrsa -out server.key 1024
    user@host$ openssl req -new -key server.key -out server.csr
    user@host$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

    '''
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

urls = (
    '/', 'application.controllers.main.index.Index','/Clientes', 'application.controllers.Clientes.index.Index',
    '/Clientes/view/(.+)', 'application.controllers.Clientes.view.View',
    '/Clientes/edit/(.+)', 'application.controllers.Clientes.edit.Edit',
    '/Clientes/delete/(.+)', 'application.controllers.Clientes.delete.Delete',
    '/Clientes/insert', 'application.controllers.Clientes.insert.Insert',
    '/api_Clientes/?', 'application.api.Clientes.api_Clientes.Api_Clientes',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()
