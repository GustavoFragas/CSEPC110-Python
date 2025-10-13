"""
Gustavo Fragas Cunha
20 anos
06/09/2025

Carrinho de Compras

- Uso do import os para deixar mais limpo a visão do cliente (saida de dados)

- Uso do try para verificar se o primeiro valor dado esta entre 1 e 5

"""
import os

#Metodos
def portal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione uma das seguintes ações:")

    try:

        escolha = int(input("1. Adicionar item\n2. Ver carrinho\n3. Remover item\n4. Calcular total\n5. Sair\nPor favor, insira uma ação\n> "))
        if 1 <= escolha <= 5:
            return escolha
        else:
            print("Ação inválida, por favor insira um número entre 1 e 5.")
            return portal()
    except ValueError:
        print("Entrada inválida ou não identificada. Por favor insira um número. ")
        return portal()
    
print("Bem-vindos ao Programa de Carrinho de Compras!")
print("-" * 40)
itens = list()
valores_itens = list()

escolha = 0

while escolha != 5:

    escolha = portal()
    if escolha ==  1:
        os.system('cls' if os.name == 'nt' else 'clear')
        produto = input("Qual item você gostaria de adicionar?\n> ")
        itens.append(produto)

        valor = float(input(f"Qual é o preço de {produto}?\n> "))
        valores_itens.append(valor)

        print (f"O item '{produto}' foi adicionado ao carrinho. ")


    elif escolha == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("O conteúdo do carrinho de compras é:")
        contador = 1

        for i in range(len(valores_itens)):
            nome_produto = itens[i]
            valor_produto = valores_itens[i]
            print(f"{contador}. {nome_produto.capitalize()} - R$ {valor_produto:.2f}")
            contador += 1

        input("\nPressione ENTER para voltar ao menu")

    elif escolha == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        contador = 1

        for i in range(len(valores_itens)):
            nome_produto = itens[i]
            valor_produto = valores_itens[i]
            print(f"{contador}. {nome_produto.capitalize()} - R$ {valor_produto:.2f}")
            contador += 1

        decisao = int(input("Qual item você gostaria de remover?\n> "))
        decisao -= 1  
        itens.pop(decisao)
        valores_itens.pop(decisao)      
        print("Item removido.")    
        print()
        input("\nPressione ENTER para voltar ao menu")


    elif escolha == 4:
        total_valor = 0
        for i in valores_itens:
            total_valor += i
        if total_valor == 0:
             print("O carrinho está vazio. Total: R$0.00")
        else:
            print(f"O preço total dos itens no carrinho de compras é de {total_valor:.2f}")
        
        input("\nPressione ENTER para voltar ao menu")
        
             

print("\nObrigado por usar o Carrinho de Compras. Até logo!")

