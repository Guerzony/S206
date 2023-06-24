class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "4":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class CartaCLI(SimpleCLI):
    def __init__(self, carta_model):
        super().__init__()
        self.carta_model = carta_model
        self.add_command("0", self.create_carta)
        self.add_command("1", self.read_carta)
        self.add_command("2", self.update_carta)
        self.add_command("3", self.delete_carta)

    def create_carta(self):
        nome = input("Entre com o nome: ")
        ataque = int(input("Entre com o valor do ataque: "))
        defesa = int(input("Entre com o valor da defesa: "))
        vida = int(input("Entre com o valor da vida: "))
        self.carta_model.create_carta(nome, ataque, defesa, vida)

    def read_carta(self):
        id = input("Entre com o id: ")
        carta = self.carta_model.read_carta_by_id(id)
        if carta:
            print(f"Name: {carta['nome']}")
            print(f"Ataque: {carta['ataque']}")
            print(f"Defesa: {carta['defesa']}")
            print(f"Vida: {carta['vida']}")

    def update_carta(self):
        id = input("Entre com o id : ")
        nome = input("Entre com o nome : ")
        ataque = int(input("Entre o valor do ataque: "))
        defesa = int(input("Entre o valor do defesa: "))
        vida = int(input("Entre com o valor da vida: "))
        self.carta_model.update_carta(id, nome, ataque, defesa, vida)

    def delete_carta(self):
        id = input("Enter the id: ")
        self.carta_model.delete_carta(id)

    def run(self):
        print("<<<==========MENU==========>>>")
        print("Available commands:")
        print("0 - create ")
        print("1 - read ")
        print("2 - update "),
        print("3 - delete ")
        print("4 - quit ")
        super().run()