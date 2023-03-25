import result as result

from database import Database
from writeAJson import writeAJson
db = Database(database="mercado", collection="compras")
db.resetDatabase()


class ProductAnalyser():
    # 1.Total de vendas por dia:
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"},
                    "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},

    ])

    writeAJson(result, "Total de vendas por dia")

    # # Cliente que mais comprou em cada dia:
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"},
                    "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])

    writeAJson(result, "Cliente que mais gastou em uma única compra")

    # # Produto mais vendido:
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])

    writeAJson(result, "Produto mais vendido em todas as compras")

    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 1}}},
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    ])

    writeAJson(result, "todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.")
