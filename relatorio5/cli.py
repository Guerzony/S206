class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com o comando: ")
            if command == "quit":
                print("Adeus!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido, tente novamente!")


class BookCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        titulo = input("Entre com o titulo: ")
        ano = int(input("Entre com o ano: "))
        autor = input("Entre com o autor: ")
        preco= input("Entre com o preco: ")
        self.livro_model.create_livro(titulo, ano, autor, preco)

    def read_livro(self):
        id = input("Entre com o id: ")
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"Titulo: {livro['titulo']}")
            print(f"Ano: {livro['ano']}")
            print(f"Autor: {livro['autor']}")
            print(f"Preco: {livro['preco']}")

    def update_livro(self):
        id = input("Entre com o id: ")
        titulo = input("Entre com o novo titulo: ")
        ano = (input("Entre com o novo ano: "))
        autor = input("Entre com o novo autor: ")
        preco = (input("Entre com o novo preco: "))
        self.livro_model.update_livro( id,titulo, ano, autor, preco)

    def delete_livro(self):
        id = input("Entre com o id: ")
        self.livro_model.delete_livro(id)

    def run(self):
        print("Bem vindo!")
        print("CRUD: create, read, update, delete, quit")
        super().run()