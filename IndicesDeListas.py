compras = list()

produto = ""
print("Por favor, insira os itens da lista de compras (digite 'sair' para finalizar): ")

while produto != "sair":
    produto = input("item: ")
    if produto != "sair":
        compras.append(produto)
    

print()

print("A lista de compras com índices é:")
for i in range(len(compras)):
    comprinhas = compras[i]
    contador_humano = i + 1
    print(f"{contador_humano}. {comprinhas}")

print()

item_retirado = int(input("Qual item você gostaria de alterar? "))
item_retirado_real = item_retirado - 1
compras.pop(item_retirado_real)

item_agregado = input("Qual é o novo item? ")
compras.insert(item_retirado_real, item_agregado)

print()

print("A lista de compras com índices é:")
for i in range(len(compras)):
    comprinhas = compras[i]
    contador_humano = i + 1
    print(f"{contador_humano}. {comprinhas}")