import math
"""
QUADRADO
"""

def area_do_quadrado():
    comprimento_quadrado = round(float(input("Qual é o comprimento de um lado do quadrado? ")),2)
    area_quadrado = comprimento_quadrado ** 2
    print (f"A área do quadrado é: {area_quadrado}")

    return area_quadrado

"""
Retângulo
"""

def area_do_retangulo():
    comprimento_retangulo = round(float(input("Qual é o comprimento do retângulo? ")),2)
    largura_retangulo = round(float(input("Qual é a largura do retângulo? ")),2)
    area_retangulo = comprimento_retangulo * largura_retangulo
    print (f"A área do retângulo é: {area_retangulo}")

    return area_retangulo

"""
Círculo
"""

def area_do_circulo():
    raio_circulo = round(float(input("Qual é o raio do circulo? ")),2)
    area_circulo = (raio_circulo ** 2) * 3.14
    print (f"A área do quadrado é: {area_circulo}")

    return area_circulo


area_do_quadrado()
print()
area_do_retangulo()
print()
area_do_circulo()
print()

"""
Desafios adicionais
"""

"""
Desafio 1
"""
def desafio1():
    raio_circulo = round(float(input("Qual é o raio do circulo? ")),2)
    area_circulodesafio = (raio_circulo ** 2) * math.pi 
    print (f"A área do quadrado é: {area_circulodesafio:.2f}")

    return area_circulodesafio

desafio1()
print()
"""
Desafio 2
"""

def desafio2():
    root_comprimento = round(float(input("Digite um valor do seu agrado: ")), 2)

    print(f"Com esse valor o seu quadrado teria a área de {root_comprimento ** 2}")

    print(f"Com esse valor o seu circulo teria a área de {(root_comprimento ** 2) * math.pi}")

    print(f"Com esse valor o seu cubo teria o volume de {root_comprimento ** 3}")

    print(f"Com esse valor o seu cilindro teria o volume de {(4 / 3) * math.pi * root_comprimento ** 3}")

desafio2()
print()








