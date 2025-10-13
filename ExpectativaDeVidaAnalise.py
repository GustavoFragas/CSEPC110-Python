"""
Gustavo Fragas Cunha
20 anos
10/10/2025

Expectativa de vida - Analise de Dados

Criatividade

-Uso de float('inf') e float('-inf') para não precisar determinar um valor (Esse eu busquei na internet e gostei)

-Uso de TRY E EXCEPT

-Robustez ao digitar o ano (somente entre 1950 até 2019 será valido)

-Uso do import os para limpar a Saída

"""

"""
---OBJETIVO DO PROJETO
Input com a data que o usuario quer
expectativa de vida MAXIMA GERAL de vida
expectativa de vida MINIMA GERAL de vida

media de TODOS OS PAISES
expectativa de vida MAXIMA em SAIDA DO USUARIO de vida
expectativa de vida MINIMA em SAIDA DO USUARIO de vida

(Criatividade)
"""
import os

with open("expectativa-de-vida.csv", encoding="utf-8") as pagina_web:

    """
    Variaveis Criadas
    """
    primeira_linha = pagina_web.readline()

    #Variaveis necessarias para o primeiro problema
    expectativa_maxima_vida = float('-inf') 
    nome_pais_maior_expectativa_vida = ""
    ano_pais_maior_expectativa_vida = 0

    #Variaveis necessarias para o segundo problema
    expectativa_minima_vida = float('inf')
    nome_pais_menor_expectativa_vida = ""
    ano_pais_menor_expectativa_vida = 0

    #Variaveis necessarias para o terceiro problema
    media_todos_paises = 0
    qtd_de_vezes_por_ano = 0 

    #Variaveis necessarias para o quarto problema
    expectativa_maxima_pais_usuario = float('-inf')
    nome_maxima_pais_usuario = ""

    #Variaveis necessarias para o quinto problema
    expectativa_minima_pais_usuario = float('inf')
    nome_minima_pais_usuario = ""
    """ 
    Fim Variaveis Criadas
    """
    while True:
        try:
            ano_resposta_usuario = int(input("Digite o ano de interesse entre 1950 até 2019:\n> "))
            if 1950 <= ano_resposta_usuario <= 2019:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Erro: O ano {ano_resposta_usuario} está fora do intervalo de dados (1950 a 2019).")
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Erro: Entrada inválida. Por favor, digite um número inteiro entre 1950 e 2019 para o ano.")
                        

    for linha in pagina_web:
        linha_separada = linha.strip().split(",")
        # print(linha_separada)
        """
        Variaveis Criadas
        """
        expectativa_vida_arquivo_int = float(linha_separada[3])
        """
        Fim Variaveis Criadas
        """

        """
        Código
        """
        #Lógica para o primeiro problema
        if expectativa_maxima_vida < expectativa_vida_arquivo_int:
            expectativa_maxima_vida = expectativa_vida_arquivo_int
            nome_pais_maior_expectativa_vida = linha_separada[0]
            ano_pais_maior_expectativa_vida = int(linha_separada[2])

        #Lógica para o segundo problema
        if expectativa_minima_vida > expectativa_vida_arquivo_int:
            expectativa_minima_vida = expectativa_vida_arquivo_int
            nome_pais_menor_expectativa_vida = linha_separada[0]
            ano_pais_menor_expectativa_vida = int(linha_separada[2])

        #Lógica para o terceiro problema
        if int(linha_separada[2]) == ano_resposta_usuario:
            media_todos_paises += expectativa_vida_arquivo_int
            qtd_de_vezes_por_ano += 1
            media_geral = media_todos_paises / qtd_de_vezes_por_ano

        #Lógica para o quarto problema
        if int(linha_separada[2]) == ano_resposta_usuario:
            if expectativa_maxima_pais_usuario < expectativa_vida_arquivo_int:
                expectativa_maxima_pais_usuario = expectativa_vida_arquivo_int
                nome_maxima_pais_usuario = linha_separada[0]

        #Lógica para o quinto problema
        if int(linha_separada[2]) == ano_resposta_usuario:
            if expectativa_minima_pais_usuario > expectativa_vida_arquivo_int:
                expectativa_minima_pais_usuario = expectativa_vida_arquivo_int
                nome_minima_pais_usuario = linha_separada[0]
    #Saida de Dados        
    print(f"A expectativa de vida máxima geral é: {expectativa_maxima_vida} de {nome_pais_maior_expectativa_vida} em {ano_pais_maior_expectativa_vida}.")

    print(f"A expectativa de vida máxima geral é: {expectativa_minima_vida} de {nome_pais_menor_expectativa_vida} em {ano_pais_menor_expectativa_vida}.")

    print()

    print(f"Para o ano de {ano_resposta_usuario}:")
    print(f"A média da expectativa de vida em todos os países era de {media_geral:.2f}")

    print(f"A expectativa de vida máxima estava na {nome_maxima_pais_usuario}, com {expectativa_maxima_pais_usuario}.")

    print(f"A expectativa de vida mínima estava no {nome_minima_pais_usuario}, com {expectativa_minima_pais_usuario}.")