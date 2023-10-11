from pymongo import MongoClient

# Conectar ao servidor MongoDB
client = MongoClient('mongodb://localhost:27017/')
# Acessar um banco de dados (ou criar se não existir)
db = client['ipper']
# Acessar uma coleção dentro do banco de dados (ou criar se não existir)
colecao = db['alertas']

def registerAlert(nome):
    novo_documento = {
        "numero": id,
        "nome": nome
    }
    colecao.insert_one(novo_documento)