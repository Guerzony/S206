class GameDatabase:
    def _init_(self, database):
        self.db = database
    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    def create_match(self, name, player_name):
        query = "MATCH (p:Player {name: $player_name}) CREATE (:Matchs {name: $name})<-[:JOGA]-(p)"
        parameters = {"name": name, "player_name": player_name}
        self.db.execute_query(query, parameters)
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    def get_matchs(self):
        query = "MATCH (m:Matchs)<-[:JOGA]-(p:Player) RETURN m.name AS name, p.name AS player_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["player_name"]) for result in results]
    def insert_player_match(self, player_name, match_name):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {name: $match_name}) CREATE (a)-[:JOGA]->(m)"
        parameters = {"player_name": player_name, "match_name": match_name}
        self.db.execute_query(query, parameters)
    def delete_aluno(self, name):
        query = "MATCH (a:Aluno {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    def delete_aula(self, name):
        query = "MATCH (a:Aula {name: $name})<-[:MINISTRA]-(p:Professor) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)