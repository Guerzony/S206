from database import Database
from clientConsult import BancoDeDados

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.89.138.223:76870","neo4j", "cloth-modifications-educators")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
try:
    banco = BancoDeDados(db)
    print('Conectado!')
except:
    print('Não conectado!')

# Criando algumas pessoas
banco.criar_pessoa("Jogador", "Drake", 31, "M")
banco.criar_pessoa("Empresario", "Suygetsu", 11, "M")
banco.criar_pessoa("Lixeiro", "Viserys", 16, "M")
banco.criar_pessoa("Urologista", "Danny", 63, "M")
banco.criar_pessoa("Medica", "Lissandra", 32, "F")
banco.criar_pessoa("Freira", "Dillion", 42, "F")
banco.criar_pessoa("Psicologa", "Emilia", 56, "F")

# Criando alguns match e suas relações com os alunos
banco.criar_pet("Leon", 5, "M", "cao")
banco.criar_pet("Eugenia", 2, "F", "gato")
banco.criar_pet("Nina", 1, "F", "passaro")

#Criando relacionamento pessoa com pet e pessoa com pessoa
banco.criar_pessoa_pet("Drake", "Leon")
banco.criar_pessoa_pet("Drake", "Eugenia")
banco.criar_pessoa_pet("Drake", "Nina")
banco.criar_pessoa_pessoa("Viserys", "Drake", "IRMAO_DE")
banco.criar_pessoa_pessoa("Lissandra", "Suygetsu", "PAI_DE")
banco.criar_pessoa_pessoa("Lissandra", "Drake", "PAI_DE")
banco.criar_pessoa_pessoa("Lissandra", "Viserys", "PAI_DE")
banco.criar_pessoa_pessoa("Danny", "Lissandra", "ESPOSO_DE")
banco.criar_pessoa_pessoa("Emilia", "Lissandra", "PAI_DE")

while True:
    # Print de todas as informações do banco de dados
    print("Escolha a opcao")
    print("0-Mostrar pessoas")
    print("1-Mostrar pets")
    print("2-Procurar emprego da pessoa")
    print("3-Procurar quem é filha de quem")
    print("4-Procurar quem é casada com outra")
    print("5-Sair")
    escolha = int(input("Escolha: "))

    if escolha == 0:
        print("Pessoas: ", banco.get_pessoa())
    elif escolha == 1:
        print("Pets: ", banco.get_pet())
    elif escolha == 2:
        nome = input("Entre com o nome da profissao: ")
        print("Quem é " + nome + " :", banco.get_emprego(nome))
    elif escolha == 3:
        nome = input("Entre com o nome do pai ou da mae: ")
        print("Quem tem " + nome + "como pai ou mae: ", banco.get_Pai(nome))
    elif escolha == 4:
        nome = input("Entre com o nome da pessoa que voce quer saber do relacionamento: ")
        print("Essa pessoa possui relacionamento com: ", banco.get_Relacionamento(nome))
    elif escolha == 5:
        print("Adeus!")
        break
    else:
        print('Opção invalida!')

# Fechando a conexão
db.close()