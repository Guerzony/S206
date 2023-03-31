from pymongo import MongoClient
from bson.objectid import ObjectId

class Livro:
    def __init__(self, database):
        self.db = database

    def create_livro(self, titulo:str, ano:int, autor:str, preco:float):
        try:
            res = self.db.collection.insert_one({"titulo": titulo, "ano": ano, "autor":autor, "preco":preco })
            print(f"Livro criado com o ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Erro ao criar o livro: {e}")
            return None

    def read_livro_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Erro ao ler o livro: {e}")
            return None

    def update_livro(self, id:str, titulo:str, ano:int, autor:str, preco:float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "ano": ano, "autor":autor, "preco":preco}})
            print(f"Livro atualizado: {res.modified_count} documento modificado")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar o livro: {e}")
            return None

    def delete_livro(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento deletado")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar o livro: {e}")
            return None