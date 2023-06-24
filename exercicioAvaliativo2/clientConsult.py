import numpy as np
class BancoDeDados:
    def __init__(self, database):
        self.db = database


    def get_emprego(self, emprego):
        query = "MATCH(e:" + emprego + ") RETURN e.nome"
        results = self.db.execute_query(query)
        return [(result["e.nome"]) for result in results]

    def get_Pai(self,nome):
        query = "MATCH (p1:Pessoa{nome: $nome})-[:PAI_DE]->(p2:Pessoa) RETURN p1.nome,p2.nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [(result["p1.nome"], result["p2.nome"]) for result in results]

    def get_Relacionamento(self, nome):
        query = "MATCH (p1:Pessoa{nome: $nome})-[:ESPOSO_DE]->(p2:Pessoa) RETURN p2.nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [(result["p2.nome"]) for result in results]
    def get_pessoa(self):
        query = "MATCH (p:Pessoa) RETURN p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]
    def get_pet(self):
        query = "MATCH (p:Pet) RETURN p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]



    def criar_pessoa(self, profissao, nome, idade, sexo):
        query = "CREATE (:Pessoa:" + profissao + "{ nome: $nome, idade: $idade, sexo: $sexo})"
        parameters = {"nome": nome, "idade": idade, "sexo": sexo}
        self.db.execute_query(query, parameters)
    def criar_pet(self, nome, idade, sexo, tipo):
        query = "CREATE (:Pet:tipo {nome: $nome, idade: $idade, sexo: $sexo})"
        parameters = {"tipo": tipo, "nome": nome, "idade": idade, "sexo": sexo}
        self.db.execute_query(query, parameters)
    def criar_pessoa_pet(self, nome_pessoa, nome_pet):
        query = "MATCH (p:Pessoa {nome: $nome_pessoa}),(pet:Pet {nome: $nome_pet}) CREATE (p)-[:DONO_DE]->(pet)"
        parameters = {"nome_pet": nome_pet, "nome_pessoa": nome_pessoa}
        self.db.execute_query(query, parameters)
    def criar_pessoa_pessoa(self    , nome_pessoa1, nome_pessoa2, relacionamento):
        query = "MATCH (p1:Pessoa {nome: $nome_pessoa1}),(p2:Pessoa {nome: $nome_pessoa2}) CREATE (p1)-[:" + relacionamento + "]->(p2)"
        parameters = {"nome_pessoa1": nome_pessoa1, "nome_pessoa2": nome_pessoa2,"relacionamento": relacionamento}
        self.db.execute_query(query, parameters)




    def delete_pessoa(self, nome):
        query = "MATCH (p:Pessoa {nome: $nome}) DETACH DELETE p"
        parameters = {"name": nome}
        self.db.execute_query(query, parameters)
    def delete_pet(self, nome):
        query = "MATCH (pet:Pet {nome: $nome}) DETACH DELETE pet"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)