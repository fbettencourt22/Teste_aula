import datetime

nome: str = input("Qual é o seu nome? ")
i: str = input("Qual é a tua data de nascimento (no formato DD/MM/AAAA)? ")

def calcular_idade():
    data_nascimento = datetime.datetime.strptime(i, "%d/%m/%Y")

    data_hoje = datetime.datetime.now()

    idade = data_hoje.year - data_nascimento.year

    if (data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
        
    return idade

def welcome(nome, idade):  
            
    if idade > 130:
        print("Erro: idade demasiado alta. Verifique a data de nascimento.")
    else:    
        print(f"Olá, {nome}, a tua idade é {idade}!")



def entrar(idade):
    if not welcome(nome, idade):
        return

    if idade >= 18:
        print(f"Como tens {idade}, podes entrar na discoteca. ")
    else:
        print(f"Como tens {idade}, não podes entrar na discoteca. ")

idade = calcular_idade()
entrar(idade)