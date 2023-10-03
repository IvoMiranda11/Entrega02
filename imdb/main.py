import pymongo
import json


uri = "mongodb://localhost:27017"
db_name = "IMDB"


with open("dados.json", "r") as json_file:
    dados = json.load(json_file)


def inserir_dados():

    client = pymongo.MongoClient(uri)

    try:

        db = client[db_name]

        colecao_pessoa = db["Pessoa"]

        resultado = colecao_pessoa.insert_many(dados)

        print(f"Foram inseridos {len(resultado.inserted_ids)} documentos.")
    finally:

        client.close()


inserir_dados()
