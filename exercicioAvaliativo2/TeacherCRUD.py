import numpy as np
class BancoDeDados:
    def __init__(self, database):
        self.db = database

### BUSCA DE INFORMAÇÕES
    def read_Teacher(self, name):
            query = "MATCH (t:Teacher {name: $name}) RETURN t"
            parameters = {"name": name}
            results = self.db.execute_query(query, parameters)
            return [(result["t"]) for result in results]

### CRIAÇÃO DE TEACHER
    def criar_Teacher(self, name, ano_nasc, cpf):
        query = "CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print('Criado com sucesso!')
### DELETE DE TEACHER
    def delete_Teacher(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print('Deletado com sucesso!')

### UPDATE DE TEACHER
    def update_Teacher(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = " + newCpf
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print('Atualizado com sucesso!')
