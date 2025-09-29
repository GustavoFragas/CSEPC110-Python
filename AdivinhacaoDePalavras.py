"""
Gustavo Fragas Cunha
20 anos
06/09/2025

-Calculadora de Preço de Refeições

Criatividade:

-Uso do import os, para limpar a tela

-Ao invés de criar outro loop dentro de um loop para verificar as letras se existem, descobri que o "IN" já fazia esse trabalho de maneira mais simples. O rascunho está logo abaixo como comentários.

"""

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

contador = 0

if escolha == 1:
    print("Você escolheu o nível fácil")
    palavra_facil = nome.lower()
    numero_de_letras_facil = len(palavra_facil)
    
    print("Sua dica é: ", end="")
    for i in range(numero_de_letras_facil):
        print("_", end="")
        
    print()
    dica = 0
    chute_facil = ""
    while chute_facil.lower() != palavra_facil.lower():
        contador += 1
        dica += 1

        if dica == 1:
            print()
            print("Sua primeira dica é:\n A resposta é uma pessoa muito especial para você!")
        elif dica == 2:
            print()
            print("Sua segunda dica é:\n Seus responsáveis que tiveram a ideia dessa palavra")
        elif dica == 3:
            print()
            print("Sua terceira dica é:\n Você mesmo já escrevou a resposta!")
        elif dica > 3:
            print()
            print("Suas dicas são:\n A resposta é uma pessoa muito especial para você!")
            print("Sua segunda dica é:\n Seus responsáveis que tiveram a ideia dessa palavra")
            print("Sua terceira dica é:\n Você mesmo já escrevou a resposta!")
        print()
        chute_facil = input("Dê o seu palpite: \n> ")
        os.system('cls' if os.name == 'nt' else 'clear')

        while len(chute_facil) != len(palavra_facil):
            os.system('cls' if os.name == 'nt' else 'clear')
            chute_facil = (input("Por favor digite uma palavra com a mesma quantidade de letras que a dica:\n> "))
        
        print()

        for i in range(numero_de_letras_facil):
            
            if i < len(chute_facil):
                letra_palpite = chute_facil[i]
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
    print(f"Você precisou de {contador} palpites !")

elif escolha == 2:
    print("Você escolheu o nível médio")
    palavra_media = "Morango"    
    numero_de_letras_media = len(palavra_media)

    print("Sua dica é: ", end="")
    for i in range(numero_de_letras_media):
        print("_", end="")

    print()
    chute_medio = ""
    while palavra_media.lower() != chute_medio.lower():
        contador += 1
        dica += 1

        if dica == 1:
            print()
            print("Sua primeira dica é:\n Vermelho")
        elif dica == 2:
            print()
            print("Sua segunda dica é:\n Fruta")
        elif dica == 3:
            print()
            print("Sua terceira dica é:\n '_______ do amor'!")
        elif dica > 3:
            print()
            print("Sua primeira dica é:\n Vermelho")
            print("Sua segunda dica é:\n Fruta")
            print("Sua terceira dica é:\n '_______ do amor'!")
        print()
        chute_medio = input("Dê o seu palpite: \n> ")
        os.system('cls' if os.name == 'nt' else 'clear')    

        while len(chute_medio) != len(palavra_media):
            os.system('cls' if os.name == 'nt' else 'clear')
            chute_medio = (input("Por favor digite uma palavra com a mesma quantidade de letras que a dica:\n> "))

        print()
        for i in range(numero_de_letras_media):
            if i < len(chute_medio):
                letra_palpite = chute_medio[i]
                letra_palavra = palavra_media[i]
                if letra_palpite.lower() == letra_palavra.lower():
                    print(letra_palpite.upper(), end="")
                elif letra_palpite.lower() in letra_palavra.lower():
                    print(letra_palpite.lower(), end="")
                else:
                    print("_", end="")
                
            else:    
                print ("_", end="")
    print()
    print("Você acertou a palavra!")    
    print(f"Você precisou de {contador} palpites !")

elif escolha == 3:
    print("Você escolheu o nível médio")
    palavra_dificil = "Pindamonhangaba"    
    numero_de_letras_dificil = len(palavra_dificil)

    print("Sua dica é: ", end="")
    for i in range(numero_de_letras_dificil):
        print("_", end="")

    print()
    dica = 0 
    chute_dificil = ""
    while palavra_dificil.lower() != chute_dificil.lower():
        contador += 1
        dica += 1

        if dica == 1:
            print()
            print("Sua primeira dica é:\n Município de São Paulo")
        elif dica == 2:
            print()
            print("Sua segunda dica é:\n Perto de Campos do Jordão")
        elif dica == 3:
            print()
            print("Sua terceira dica é:\n  Região Metropolitana do Vale do Paraíba e Litoral Norte no interior do estado de São Paulo.")
        elif dica > 3:
            print()
            print("Suas dicas são:\n Município de São Paulo")
            print("Sua segunda dica é:\n Perto de Campos do Jordão")
            print("Sua terceira dica é:\n  Região Metropolitana do Vale do Paraíba e Litoral Norte no interior do estado de São Paulo.")

        print()
        chute_dificil = input("Dê o seu palpite: \n> ")
        os.system('cls' if os.name == 'nt' else 'clear')

        while len(chute_dificil) != len(palavra_dificil):
            os.system('cls' if os.name == 'nt' else 'clear')
            chute_dificil = (input("Por favor digite uma palavra com a mesma quantidade de letras que a dica:\n> "))    

        print()
        for i in range(numero_de_letras_dificil):
            if i < len(chute_dificil):
                letra_palpite = chute_dificil[i]
                letra_palavra = palavra_dificil[i]
                if letra_palpite.lower() == letra_palavra.lower():
                    print(letra_palpite.upper(), end="")
                elif letra_palpite.lower() in letra_palavra.lower():
                    print(letra_palpite.lower(), end="")
                else:
                    print("_", end="")
                
            else:    
                print ("_", end="")
    print()
    print("Você acertou a palavra!")    
    print(f"Você precisou de {contador} palpites !")






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

