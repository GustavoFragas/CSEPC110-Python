import os

print()
print("Bem-vindo ao jogo de adivinhação de palavras!")
nome = input("Qual o seu primeiro nome?\n> ")

print(f"Antes de começar a jogar {nome.capitalize()}")
print()

escolha = int(input(("Selecione o nível de dificuldade: \n1 - Fácil\n2 - Médio\n3 - Difícil\n> ")))

while escolha < 1 or escolha > 3:
    escolha = int(input("Por favor digite um valor válido:\n> "))

os.system('cls' if os.name == 'nt' else 'clear')

if escolha == 1:
    print("Você escolheu o nível fácil")
    palavra_facil = nome.lower()
    numero_de_letras_facil = len(palavra_facil)
    
    print("Sua dica é: ", end="")
    for i in range(numero_de_letras_facil):
        print("_", end="")
        
    print()
    chute = ""
    while chute.lower() != palavra_facil.lower():
        
        print()
        chute = input("Dê o seu palpite: \n> ")
        os.system('cls' if os.name == 'nt' else 'clear')

        print()
        for i in range(numero_de_letras_facil):
            if i < len(chute):
                letra_palpite = chute[i]
                letra_palavra = palavra_facil[i]

                if letra_palpite.lower() == letra_palavra.lower():
                    print(letra_palpite.upper(), end="")
                elif letra_palpite.lower() in palavra_facil.lower():
                    print(letra_palpite.lower(), end="")
                else:
                    print("_", end="")
                
            else:    
                print ("_", end="")
    print()
    print("Você acertou a palavra!")

    





        # letra = chute[i]
        # letra_palavra_original = palavra_facil[i]

        # if letra_palavra_original == letra:
        #     print(letra_palavra_original.upper(), end="")
        
        # elif letra_palavra_original != letra:
        #     for j in range(numero_de_letras_facil):
        #         letrita = palavra_facil[j]
        #         if letra == letrita:
        #             print(letrita, end="")
        #         else:
        #             print("",  end="")
        #     else:
        #         print("_", end="")
        
# elif escolha == 2:
#     print("Você escolheu o nível médio")
#     palavra_media = "Morango"

# elif escolha == 3:Gusg
#     print("Você escolheu o nível difícil")
#     palavra_dificil = "Pindamonhangaba"

