nomes = list()

novo_nome = ""

while novo_nome != "fim":
    novo_nome = input("Digite o nome de um amigo: ")

    if novo_nome != "fim":
        nomes.append(novo_nome)
print()
print("Seus amigos são: ")

for i in nomes:
    print(i)
    

   
# amigos = []

# nome = None

# while nome != "fim":
#     nome = input("Digite o nome de um amigo: ")

#     if nome != "fim":
#         amigos.append(nome)

# print()
# print("Seus amigos são: ")

# for amigo in amigos:
#     print(amigo)