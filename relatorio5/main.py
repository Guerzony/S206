from database import Database
from writeAJson import writeAJson
from Livro import Livro
from cli import BookCLI

db = Database(database="atividade5", collection="Livros")
personModel = Livro(database=db)


bookCLI = BookCLI(personModel)
bookCLI.run()