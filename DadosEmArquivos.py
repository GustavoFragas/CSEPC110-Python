pessoas = [
    "Stephanie 36",
    "João 29",
    "Emília 24",
    "Graça 54",
    "Nícolas 12",
    "Penelope 32",
    "Miguel 2",
    "Jacó 10"
]

menor_idade = 100
pessoa_menor_idade = ""

for linha in pessoas:
    
    pessoas_separadas = linha.split()
    conversao_int_idade = float(pessoas_separadas[1])

    if conversao_int_idade < menor_idade:
        menor_idade = conversao_int_idade
        pessoa_menor_idade = pessoas_separadas[0]

print(f"A Idade menor é de {menor_idade} e é {pessoa_menor_idade} que tem essa idade")
