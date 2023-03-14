from database import Database
from writeAJson import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()

def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})
types = ["Fighting"]
pokemons = getPokemonsByType(types)
writeAJson(pokemons, "pokemons_by_type")

def getPokemonByName(name: str):
    return db.collection.find({"name": name})
pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")

def getPokemonsBySpawn(types: list):
    return db.collection.find({"type": {"$in": types}})

pokemons1 = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
writeAJson(pokemons1, "pokemons_by_spawn")

def getNameByWeight(weight: str):
    return db.collection.find({"weight": weight})
namePokemon = getNameByWeight ("39.5 kg")
writeAJson(namePokemon, "PesoPokemon")

def getNameByHeight(height: str):
    return db.collection.find({"height": height})
namePokemon = getNameByHeight ("1.50 m")
writeAJson(namePokemon, "AlturaPokemon")
