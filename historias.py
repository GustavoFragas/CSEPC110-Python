"""
Gustavo Fragas Cunha
20 anos
02/09/2025

(Quero deixar bem claro que é bastante dificil programar e Python por eu estar aprendendo C#, dificil não, engraçado pelo fato que muitos "comandos" são diferentes kkkk)
-Demonstrando Criatividade e Indo Além dos Requisitos

1º - Criação de um método contar_historia_inputs para uma melhor organização caso exista mais código no futuro

2º - Criação de aleatoriedade de palavras caso o usuário deixe a pergunta em branco
"""
import random

def contar_historia_conteudo():

    animal = input("Qual é o animal principal da história? ")
    adjetivo_do_animal = input("Como ele era? ")
    acao = input("O que ele fez? ")
    exclamacao = input("O que você gritou? ")
    reacao = input("O que você fez para reagir?")
    acao_final = input("O que o animal tentou fazer no final?")

    animais_aleatorio = ["Hamster", "Dragão", "Onça", "Gato", "Cachorro" ]
    adjetivos_aleatorio = ["bonito", "feio", "cheiroso", "bravo"]
    acao_aleatorio = ["correndo", "gritando", "saltando"]

    if not animal:
        animal = random.choice(animais_aleatorio)
    if not adjetivo_do_animal:
        adjetivo_do_animal = random.choice(adjetivos_aleatorio)
    if not acao:
        acao = random.choice(acao_aleatorio)
    if not exclamacao:
        exclamacao = "Socorro"
    if not reacao:
        reacao = "correr"
    if not acao_final:
        acao_final = "me atacar"

    historia = f"Outro dia, eu estava em apuros. Tudo começou quando vi um {animal} muito {adjetivo_do_animal} {acao} no corredor. \n{exclamacao.capitalize()}! Eu gritei. \nMas tudo que consegui pensar foi em {reacao} várias vezes. \nPor um milagre, isso fez com que a criatura parasse, mas não antes de tentar {acao_final} bem na frente da minha família."

    print("\n--- A HISTÓRIA ---\n")
    print(historia)

contar_historia_conteudo()