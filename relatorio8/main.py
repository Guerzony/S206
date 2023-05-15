from database import Database
from game import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.236.192.75:7687", "neo4j", "decrements-submarined-servants")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns players
game_db.create_player("Leo")
game_db.create_player("Sidcley")
game_db.create_player("cintia")
game_db.create_player("jacob")

# Criando alguns match e suas relações com os alunos
game_db.create_match("Jogo1", "Leo")
game_db.create_match("Jogo2", "Sidcley")
game_db.create_match("Jogo3", "cintia")
game_db.create_match("Jogo1", "jacob")

# Inserindo player no jogo
game_db.insert_player_match("Leo", "Jogo1")
game_db.insert_player_match("Sidcley", "Jogo2")
game_db.insert_player_match("cintia", "Jogo3")
game_db.insert_player_match("jacob", "Jogo1")
# Print de todas as informações do banco de dados
print("Players:")
print(game_db.get_players())
print("Matchs:")
print(game_db.get_matchs())
print()
# Fechando a conexão
db.close()