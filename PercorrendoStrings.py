palavra = "Compromisso"
letra_favorita = input("Qual é a sua letra favorita? \n> ")

print(f"Sua letra favorita é {letra_favorita.upper()}")

for letra in palavra:
    if letra.lower() != letra_favorita.lower():
        print(letra.lower(), end="")
    else:
        print("_", end="")

        # v_STA_O