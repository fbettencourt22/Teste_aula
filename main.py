import datetime

nome: str = input("Qual é o seu nome? ")
i: str = input("Qual é a tua data de nascimento (no formato DD/MM/AAAA)? ")

data_nascimento = datetime.datetime.strptime(i, "%d/%m/%Y")

data_hoje = datetime.datetime.now()

idade = data_hoje.year - data_nascimento.year

if (data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

def welcome():           
    if idade > 130:
        print("Erro: idade demasiado alta. Verifique a data de nascimento.")
    else:    
        print(f"Olá, {nome}, a tua idade é {idade}!")



def entrar():
    welcome()
    if idade >= 18:
        print(f"Como tens {idade}, podes entrar na discoteca. ")
    else:
        print(f"Como tens {idade}, não podes entrar na discoteca. ")

entrar()