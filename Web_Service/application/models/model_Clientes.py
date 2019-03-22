import web
import config

db = config.db


def get_all_Clientes():
    try:
        return db.select('Clientes')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_Clientes(id_cliente):
    try:
        return db.select('Clientes', where='id_cliente=$id_cliente', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_Clientes(id_cliente):
    try:
        return db.delete('Clientes', where='id_cliente=$id_cliente', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_Clientes(Nombre,Ape_Pat,Ape_Mat,Telefono,email):
    try:
        return db.insert('Clientes',Nombre=Nombre,
Ape_Pat=Ape_Pat,
Ape_Mat=Ape_Mat,
Telefono=Telefono,
email=email)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_Clientes(id_cliente,Nombre,Ape_Pat,Ape_Mat,Telefono,email):
    try:
        return db.update('Clientes',id_cliente=id_cliente,
Nombre=Nombre,
Ape_Pat=Ape_Pat,
Ape_Mat=Ape_Mat,
Telefono=Telefono,
email=email,
                  where='id_cliente=$id_cliente',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
