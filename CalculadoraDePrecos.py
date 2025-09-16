"""
Gustavo Fragas Cunha
20 anos
06/09/2025

-Calculadora de Preço de Refeições

Criatividade:

-uso de métodos para separar os itens e o que cada um vai fazer (em um projeto eu colocaria esses metodos em outros arquivos)

-Uso de estrutura de controle de fluxo (If e else) para adicionar Drinks

"""

def  precos():

    preco_crianca = round(float(input("Qual é o preço da refeição de uma criança? ")), 2)
    preco_adulto = round(float(input("Qual é o preço da refeição de uma adulto? ")), 2)
    qtd_crianca = int(input("Há quantas crianças? "))
    qtd_adulto = int(input("Há quantos adultos? "))

    total_consumo = (preco_crianca * qtd_crianca) + (preco_adulto * qtd_adulto)
    
    print()
    
    print(f"Subtotal: R$ {total_consumo}")

    return total_consumo

def impostos (total_consumo):

    taxa_impostos = round(float(input("Qual é a taxa de imposto sobre vendas? ")), 2)
    
    imposto_sobre_vendas = total_consumo * taxa_impostos / 100

    print(f"Imposto sobre vendas: R$ {imposto_sobre_vendas}")

    total_consumo_com_imposto = total_consumo + imposto_sobre_vendas
    
    print(f"Total: R$ {total_consumo_com_imposto}")
    
    return total_consumo_com_imposto

def validando_drink(total_consumo_com_imposto):

    sim_ou_nao = input("Você consumiu alguma bebida? ").lower()
    if sim_ou_nao in ["sim", "s"]:
        total_consumo_com_imposto += 5
        print(f"Conforme informado antes no atendimento, o valor da bebida é R$5 reais, então o valor a pagar é {total_consumo_com_imposto}")
    else:
        print(f"O restaurante não te cobrará pela bebida")

    return total_consumo_com_imposto

def metodo_pagamento(total_consumo_com_imposto):
    valor_pagamento = round(float(input("Qual é o valor do pagamento? ")), 2)
    
    troco = valor_pagamento - total_consumo_com_imposto
    
    print(f"Troco: R$ {troco:.3}")

    return valor_pagamento, troco


subtotal = precos()
print()
valorzinho = impostos(subtotal)
print()
alimento_bebida = validando_drink(valorzinho)
print()
metodo_pagamento(alimento_bebida)