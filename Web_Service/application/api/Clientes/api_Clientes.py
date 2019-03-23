import web
import config
import json


class Api_Clientes:
    def get(self, id_cliente):
        try:
            # http://0.0.0.0:8080/api_Clientes?user_hash=12345&action=get
            if id_cliente is None:
                result = config.model.get_all_Clientes()
                Clientes_json = []
                for row in result:
                    tmp = dict(row)
                    Clientes_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(Clientes_json)
            else:
                # http://0.0.0.0:8080/api_Clientes?user_hash=12345&action=get&id_cliente=1
                result = config.model.get_Clientes(int(id_cliente))
                Clientes_json = []
                Clientes_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(Clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            Clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(Clientes_json)

# http://0.0.0.0:8080/api_Clientes?user_hash=12345&action=put&id_cliente=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, Nombre,Ape_Pat,Ape_Mat,Telefono,email):
        try:
            config.model.insert_Clientes(Nombre,Ape_Pat,Ape_Mat,Telefono,email)
            Clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(Clientes_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_Clientes?user_hash=12345&action=delete&id_cliente=1
    def delete(self, id_cliente):
        try:
            config.model.delete_Clientes(id_cliente)
            Clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(Clientes_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_Clientes?user_hash=12345&action=update&id_cliente=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_cliente, Nombre,Ape_Pat,Ape_Mat,Telefono,email):
        try:
            config.model.edit_Clientes(id_cliente,Nombre,Ape_Pat,Ape_Mat,Telefono,email)
            Clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(Clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            Clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(Clientes_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_cliente=None,
            Nombre=None,
            Ape_Pat=None,
            Ape_Mat=None,
            Telefono=None,
            email=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_cliente=user_data.id_cliente
            Nombre=user_data.Nombre
            Ape_Pat=user_data.Ape_Pat
            Ape_Mat=user_data.Ape_Mat
            Telefono=user_data.Telefono
            email=user_data.email
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_cliente)
                elif action == 'put':
                    return self.put(Nombre,Ape_Pat,Ape_Mat,Telefono,email)
                elif action == 'delete':
                    return self.delete(id_cliente)
                elif action == 'update':
                    return self.update(id_cliente, Nombre,Ape_Pat,Ape_Mat,Telefono,email)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')