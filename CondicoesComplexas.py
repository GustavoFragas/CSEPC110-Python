print("Escreva um valor de 0 a 10 para os seguintes valores")
print("-" * 40)
print()
valor_emprestimo = int(input("Qual é o valor do empréstimo? "))
credito = int(input("Quão bom é o seu histórico de crédito? "))
renda = int(input("Qual é a sua renda? "))
entrada = int(input("Qual é o valor da sua entrada? "))

"""
5 2 7 5
"""

emprestimo_liberado = False

if valor_emprestimo >= 5:
    if credito >= 7 and renda >= 7:
        emprestimo_liberado = True
    elif credito >= 7 or renda >= 7:
        if entrada >= 5:
            emprestimo_liberado = True
        else:
            emprestimo_liberado = False
    else:
        emprestimo_liberado = False
else:
    if credito < 4:
        emprestimo_liberado = False
    else:
        if renda >= 7 or entrada >= 7:
            emprestimo_liberado = True
        elif renda >= 4 and entrada >= 4:
            emprestimo_liberado = True
        else:
            emprestimo_liberado = False

if emprestimo_liberado:
    print("O empréstimo será realizado tranquilamente!")
else:
    print("O empréstimo não será feito")

    