from Corrida import Corrida
from typing import Dict, Any

from Motorista import Motorista
from Passageiro import Passageiro
from database import Database
from bson.objectid import ObjectId


class MotoristaDAO:

    def __init__(self):
        self.db = Database("ExercicioAvaliativo1", "Motoristas")

    def create(self, motorista: Motorista):
        try:
            data = {
                "nota": motorista.nota,
                "corridas": [
                    {
                        "nota": corrida.nota,
                        "distancia": corrida.distancia,
                        "valor": corrida.valor,
                        "passageiro": {
                            "nome": corrida.passageiro.nome,
                            "documento": corrida.passageiro.documento
                        }
                    } for corrida in motorista.corridas
                ]
            }
            motoristaCriado = self.db.collection.insert_one(data)
            print("Motorista criado com sucesso!")
            return motoristaCriado.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro durante a criacao: {e}")
            return None

    def read(self, id: str) -> Motorista:
        try:
            data = self.db.collection.find_one({"_id": ObjectId(id)})
            if data is None:
                return None
            corridas = [
                Corrida(
                    cdata["nota"],
                    cdata["distancia"],
                    cdata["valor"],
                    Passageiro(
                        cdata["passageiro"]["nome"],
                        cdata["passageiro"]["documento"]
                    )
                ) for cdata in data["corridas"]
            ]
            return Motorista(data["nota"], corridas)
        except Exception as e:
            print(f"Ocorreu um erro durante a leitura: {e}")
            return None

    def update(self, id: str, fields: Dict[str, Any]):
        try:
            motoristaAtualizado = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": fields})
            print("Motorista atualizado com sucesso!")
            return motoristaAtualizado
        except Exception as e:
            print(f"Ocorreu um erro durante a atualizacao: {e}")
            return None

    def delete(self, id: str):
        try:
            self.db.collection.delete_one({"_id": ObjectId(id)})
            print("Motorista deletado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro durante a delecao: {e}")