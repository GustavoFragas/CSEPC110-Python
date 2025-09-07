"""
Gustavo Fragas Cunha
20 anos
06/09/2025

-Gerador de Crachás
"""

def pedir_informacao():
    
    print("Por favor, insira as seguintes informações: ")
    print()
    nome = input ("Qual é seu nome? \n")
    sobrenome = input ("Qual é seu Sobrenome? \n")
    email = input ("Qual é seu e-mail? \n")
    ddd = input ("Qual é seu DDD? \n")
    telefone = input ("Qual é seu número de telefone? ex: 987650192 \n")
    cargo = input ("Qual é seu Cargo atual? \n")
    numeroID = input ("Qual é seu número de identificação? \n")
    cor_cabelo = input ("Qual é a cor do seu cabelo? \n")
    mes = input ("Qual mês você iniciou na operação? \n")
    olhos = input ("Qual é a cor dos seus olhos? \n")
    treinamento = input ("Está em treinamento? \n")

    return nome, sobrenome, email, ddd, telefone, cargo, numeroID, cor_cabelo, mes, olhos, treinamento

def screen(nome, sobrenome, email, ddd, telefone, cargo, numeroID, cor_cabelo, mes, olhos, treinamento):
    print ("O crachá de identificação é: ")
    print("-" * 40 )
    print(f"{sobrenome.capitalize()}, {nome.capitalize()} ")
    print(f"{cargo.title()} ")
    print(f"Identificação: {numeroID} ")
    print()
    print(f"{email.lower()}")
    print(f"({ddd}) {telefone}")
    print()
    print(f"Cabelo: {cor_cabelo:15} Olhos: {olhos}")
    print(f"Mês: {mes:15} Treinamento:{treinamento}")
    print("-" * 40 )

dados = pedir_informacao()
screen (*dados)

