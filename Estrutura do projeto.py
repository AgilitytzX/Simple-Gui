import json


alunos=[]

#Funcao para ler os arquivos do Json

try:
    with open('data.json', 'r') as openfile:
        alunos = json.load(openfile)
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado!")
except:
    print("Erro ao carregar os alunos.")


#Funcao para escrever os arquivos do Json        
def salvar_alunos(alunos):
     with open("data.json", "w") as outfile: 
                json.dump(alunos, outfile,indent=2)


# Função para calcular a média de notas de um aluno
def calcular_media_notas(aluno):
    notas = aluno['notas']
    media = sum(notas) / len(notas)
    return media


# Função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    sobrenome = input("Digite o sobrenome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = input("Digite o CPF do aluno (11 digitos): ")
    while len(cpf) != 11:
        cpf = input("CPF invalido. Digite o CPF do aluno (11 digitos): ")
    curso = input("Digite o curso do aluno (Programacao, Excel, Web Design ou Robotica): ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno: "))
        nota = round(max(min(nota, 10), 0), 2)
        notas.append(nota)
    alunos.append({"nome": nome, "sobrenome": sobrenome, "idade": idade, "cpf": cpf, "curso": curso, "notas": notas})
    salvar_alunos(alunos)
    print("Aluno cadastrado com sucesso!")


#Funcao para atualizar dados do aluno
def atualizar_aluno():
    nome_completo = input("Digite o nome completo do aluno a ser atualizado: ")
    nome, sobrenome = nome_completo.split(' ', 1)
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower() and aluno['sobrenome'].lower() == sobrenome.lower():
            print(f"Atualizando informacoes do aluno {nome} {sobrenome}:")
            aluno['idade'] = int(input("Digite a nova idade do aluno: "))
            aluno['cpf'] = input("Digite o novo CPF do aluno (11 digitos): ")
            while len(aluno['cpf']) != 11:
                aluno['cpf'] = input("CPF invalido. Digite o novo CPF do aluno (11 digitos): ")
            aluno['curso'] = input("Digite o novo curso do aluno (Programacao, Excel, Web Design ou Robotica): ")
            for i in range(4):
                nota = float(input(f"Digite a nova nota {i+1} do aluno: "))
                nota = round(max(min(nota, 10), 0), 2)
                aluno['notas'][i] = nota
            salvar_alunos(alunos)
            print(f"Informacoes do aluno {nome} {sobrenome} atualizadas com sucesso!")
            return
    print(f"Não foi encontrado nenhum aluno com o nome {nome} {sobrenome}.")


#Funcao para excluir aluno
def excluir_aluno():
    nome_completo = input("Digite o nome completo do aluno a ser excluido: ")
    nome, sobrenome = nome_completo.split(' ', 1)
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower() and aluno['sobrenome'].lower() == sobrenome.lower():
            alunos.remove(aluno)
            salvar_alunos(alunos)
            print(f"Aluno {nome_completo} excluído com sucesso!")
            return
    print(f"Não foi encontrado nenhum aluno com o nome {nome_completo}.")


#Função para listar todos os alunos
def listar_alunos():
    for aluno in alunos:
        notas = aluno['notas']
        media = calcular_media_notas(aluno)
        print(f"Nome: {aluno['nome']} {aluno['sobrenome']}, Idade: {aluno['idade']}, Cpf: {aluno['cpf']}, Curso: {aluno['curso']}, Notas: {notas}, Media: {media:.2f}, Professor: {professor_do_curso(aluno['curso'])}")


#Função para filtrar alunos por curso
def filtrar_alunos_por_curso():
    curso = input("Digite o curso a ser filtrado (Programacao, Excel, Web Design ou Robotica): ")
    alunos_filtrados = [aluno for aluno in alunos if aluno['curso'].lower() == curso.lower()]
    if len(alunos_filtrados) == 0:
        print("Nao ha alunos cadastrados neste curso.")
    else:
        print(f"Alunos do curso de {curso}:")
        for aluno in alunos_filtrados:
            notas = aluno['notas']
            media = calcular_media_notas(aluno)
            print(f"Nome: {aluno['nome']} {aluno['sobrenome']}, Idade: {aluno['idade']}, Cpf: {aluno['cpf']}, Notas: {notas}, Media: {media:.2f}, Professor: {professor_do_curso(aluno['curso'])}")


def atualizar_nota():
    nome = input("Digite o nome do aluno que deseja atualizar as notas: ")
    sobrenome = input("Digite o sobrenome do aluno que deseja atualizar as notas: ")
    for aluno in alunos:
        if aluno['nome'] == nome and aluno['sobrenome'] == sobrenome:
            notas = []
            for i, nota_atual in enumerate(aluno['notas']):
                nota = input(f"Digite a nota {i+1} atual do aluno (ou deixe em branco para manter a nota atual): ")
                if nota == "":
                    notas.append(nota_atual)
                else:
                    notas.append(float(nota))
            aluno['notas'] = notas
            aluno['media'] = calcular_media_notas(aluno)
            salvar_alunos(alunos)
            print("Notas atualizadas com sucesso!")
            return
    print("Aluno não encontrado.")



#Funcao para definir qual professor pertence a cada curso
def professor_do_curso(curso):
    if curso.lower() == "programacao":
        return "Joao"
    elif curso.lower() == "excel":
        return "Maria"
    elif curso.lower() == "web design":
        return "Sergio"
    elif curso.lower() == "robotica":
        return "Lucas"
    else:
        return "Professor desconhecido"


#Menu 
while True:
    print("Selecione uma opcao:")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar informacoes de um aluno")
    print("3 - Atualizar nota do aluno")
    print("4 - Excluir aluno")
    print("5 - Listar todos os alunos")
    print("6 - Filtrar alunos por curso")
    print("7 - Sair")
    opcao = int(input())

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        atualizar_aluno()
    elif opcao == 3:
        atualizar_nota()
    elif opcao == 4:
        excluir_aluno()
    elif opcao == 5:
        listar_alunos()
    elif opcao == 6:
        filtrar_alunos_por_curso()
    elif opcao == 7:
        break
    else:
        print("Opcao invalida. Tente novamente.")
