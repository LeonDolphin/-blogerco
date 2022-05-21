from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient(host=host,
                      port=int(port),
                      username=Loen,
                      password=admin1234
                     )
 db_handle = client['db_name']
 return db_handle, client