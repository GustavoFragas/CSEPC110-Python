with open ("sistema_rh.txt", encoding="utf-8") as lista:
    
    linha_cabecalho = lista.readline()

    for linha in lista:
        linha_separada = linha.strip().split()
        nome = linha_separada[0]
        numero_de_id = linha_separada[1]
        cargo = linha_separada[2]
        salario = int(linha_separada[3])
        salario_quinzenal = (salario / 12) / 2
        if cargo == "Engenheiro(a)":
            salario_quinzenal += 1000

        salario_formatado = f"{salario_quinzenal:.2f}".replace('.', ',')
        
        print(f"{nome} (ID: {numero_de_id}), {cargo} - R$ {salario_formatado}")