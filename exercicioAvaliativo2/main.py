from database import Database
from TeacherCRUD import BancoDeDados

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.236.192.75:7687", "neo4j", "decrements-submarined-servants")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
try:
    banco = BancoDeDados(db)
    print('Conectado!')
except:
    print('Não conectado!')

'''
#ENTRADA DE DADOS POR USUARIO
while True:
    print('Oque voce deseja fazer:')
    print('1- Criar professor')
    print('2- Atualizar Cpf do professor')
    print('3- Deletar professor')
    print('4- Procurar professor')
    print('5- Sair')
    escolha = int(input('Escolha:'))
    if escolha == 1:
        nome = input('Entre com o nome do professor: ')
        ano = int(input('Entre com o ano de nascimento do professor: '))
        cpf = input('Entre com o cpf do professor: ')
        banco.criar_Teacher(nome, ano, cpf)
    elif escolha == 2:
        nome = input('Entre com o nome do professor: ')
        cpfNovo = input('Entre com o novo cpf: ')
        banco.update_Teacher(nome, cpfNovo)
    elif escolha == 3:
        nome = input('Entre com o nome do professor: ')
        banco.delete_Teacher(nome)
    elif escolha == 4:
        nome = input('Entre com o nome do professor: ')
        print(banco.read_Teacher(nome))
    elif escolha == 5:
        print('Adeus!')
        break
    else:
        print('Opção não existe! Tente novamente!')
'''

banco.criar_Teacher('Chris Lima',1956,'189.052.396-66')
print(banco.read_Teacher('Chris Lima'))
banco.update_Teacher('Chris Lima', "162.052.777-77")

# Fechando a conexão com o banco
db.close()