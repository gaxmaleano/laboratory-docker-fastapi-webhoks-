from pymongo import MongoClient
from pymongo.errors import PyMongoError

def connect_to_mongo(ip_address, port):
    try:
        # Crear el cliente de MongoDB
        client = MongoClient(f"mongodb://{ip_address}:{port}")
        
        print(dir(client))

    except PyMongoError as e:
        print(f"Error al conectar con MongoDB: {e}")

if __name__ == "__main__":
    # IP del contenedor de MongoDB y el puerto
    ip_address = "172.28.0.3"
    port = 27017
    
    # Llamar a la función para conectar
    connect_to_mongo(ip_address, port)