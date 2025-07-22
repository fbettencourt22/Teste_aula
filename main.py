import datetime

nome: str = input("Qual é o seu nome? ")
i: int = input("Qual é a tua data de nascimento (no formato DD/MM/AAAA) ?  ")
data_nascimento = datetime.datetime.strptime(i, "%d/%m/%Y")
data_hoje = datetime.datetime.now()
idade = data_hoje.year - data_nascimento.year

def welcome():           
    if idade > 130:
        print("Erro: idade demasiado alta. Verifique a data de nascimento.")
    else:    
        print(f"Olá, {nome}, a tua idade é {idade}!")

welcome()
    