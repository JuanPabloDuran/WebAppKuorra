import web

db_host = 'localhost'
db_name = 'Ferreteria_Dur'
db_user = 'Pablo'
db_pw = 'Duran'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )