def exibir_regular(texto_prompt):
    print(texto_prompt)

def exibir_maiuscula(texto_prompt):
    novo_texto = texto_prompt.upper()
    print(novo_texto)

def exibir_minuscula(texto_prompt):
    novo_texto = texto_prompt.lower()
    print(novo_texto)

resultado = input("Qual é a sua mensagem?")

exibir_regular(resultado)
exibir_maiuscula(resultado)
exibir_minuscula(resultado)