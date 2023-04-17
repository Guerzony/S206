from MotoristaDAO import MotoristaDAO
from Corrida import Corrida
from Passageiro import Passageiro
from Motorista import Motorista


class SimpleCLI:

    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com os comandos: ")
            if command == "quit":
                print("GoodBye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido, tente novamente")


class MotoristaCLI(SimpleCLI):

    def __init__(self, motorista_dao: MotoristaDAO):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nomePassageiro = input("Entre com o nome do passageiro: ")
        documentoPassageiro = input("Entre com o documento do passageiro: ")
        passageiro = Passageiro(nomePassageiro, documentoPassageiro)
        distancia = int(input("Entre com a distancia da corrida: "))
        valor = int(input("Entre com o valor da corrida: "))
        nota = int(input("Entre com a nota da corrida: "))
        corrida = Corrida(nota, distancia, valor, passageiro)
        corridas = [corrida]
        nota = int(input("Entre com a nota do motorista: "))
        motorista = Motorista(nota, corridas)
        self.motorista_dao.create(motorista)

    def read_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_dao.read(str(id))
        if motorista:
            print(f"nota: {motorista.nota}")
            print(f"corridas: {motorista.corridas}")

    def update_motorista(self):
        id = input("Digite o ID do motorista: ")
        nomePassageiro = input("Digite o novo nome do passageiro: ")
        documentoPassageiro = input("Digite o novo documento do passageiro: ")
        passageiro = Passageiro(nomePassageiro, documentoPassageiro)
        distancia = int(input("Digite a nova distância: "))
        valor = int(input("Digite o novo valor: "))
        nota_corrida = int(input("Digite a nova nota da corrida: "))
        corrida = Corrida(nota_corrida, distancia, valor, passageiro)
        fields = {
            "nota": nota_corrida,
            "corridas": [
                {
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                }
            ]
        }
        self.motorista_dao.update(id, fields)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_dao.delete(id)

    def run(self):
        print("Bem vindo !")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()