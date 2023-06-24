from pymongo import MongoClient
from bson.objectid import ObjectId

class carta:
    def __init__(self, database):
        self.db = database

    def create_carta(self, nome: str, ataque: int, defesa: int, vida: int):
        try:
            res = self.db.collection.insert_one({"nome": nome, "ataque": ataque, "defesa": defesa, "vida": vida})
            print(f"Carta criado com o ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Erro ao criar a carta: {e}")
            return None

    def read_carta_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Carta encontrado: {res}")
            return res
        except Exception as e:
            print(f"Erro ao ler a carta: {e}")
            return None

    def update_carta(self, id:str, nome: str, ataque: int, defesa: int, vida: int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome, "ataque": ataque, "defesa": defesa, "vida": vida}})
            print(f"Carta atualizado: {res.modified_count} documento modificado")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar o carta: {e}")
            return None

    def delete_carta(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Carta deletada: {res.deleted_count} documento deletado")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar a carta: {e}")
            return None