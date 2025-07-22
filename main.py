import datetime

def calcular_idade(data_nascimento):
    data_hoje = datetime.datetime.now()
    idade = data_hoje.year - data_nascimento.year
    if (data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

def welcome(nome, idade):  
    if idade > 130:
        print("Erro: idade demasiado alta. Verifique a data de nascimento.")
        return False
    else:    
        print(f"Olá, {nome}, a tua idade é {idade}!")
        return True

def entrar(nome, idade):
    if not welcome(nome, idade):
        return

    if idade >= 18:
        print(f"Como tens {idade}, podes entrar na discoteca.")
    else:
        print(f"Como tens {idade}, não podes entrar na discoteca.")

while True:
    print("\n--- Verificação de idade para entrada na discoteca ---")
    nome = input("Qual é o seu nome? ")
    i = input("Qual é a tua data de nascimento (no formato DD/MM/AAAA)? ")

    try:
        data_nascimento = datetime.datetime.strptime(i, "%d/%m/%Y")
        idade = calcular_idade(data_nascimento)
        entrar(nome, idade)
    except ValueError:
        print("Data inválida! Tenta novamente no formato DD/MM/AAAA.")
        continue

    sair = input("Desejas verificar outra pessoa? (s/n): ").strip().lower()
    if sair == 'n':
        print("Programa encerrado.")
        break
