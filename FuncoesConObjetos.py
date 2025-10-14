import math

def calcular_area_do_quadrado(lado):
    return calcular_area_do_retangulo(lado, lado)

def calcular_area_do_retangulo(comprimento, largura):
    return comprimento * largura

def calcular_area_do_circulo(raio):
    return math.pi * raio * raio


# O programa principal começa aqui...
figura = ""

while figura != "sair":
    figura = input("Qual figura você tem? ")

    # Converta-o para letras minúsculas uma única vez, para que não precisemos converter novamente
    figura = figura.lower()

    if figura == "quadrado":
        lado = float(input("Qual é o comprimento do lado? "))
        area = calcular_area_do_quadrado(lado)
        print(f"A área é {area}")
    elif figura == "retangulo":
        comprimento = float(input("Qual é o comprimento? "))
        largura = float(input("Qual é a largura? "))
        area = calcular_area_do_retangulo(comprimento, largura)
        print(f"A área é {area}")
    elif figura == "circulo":
        raio = float(input("Qual é o raio? "))
        area = calcular_area_do_circulo(raio)
        print(f"A área é {area}")