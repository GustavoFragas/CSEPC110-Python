with open("TrabalhandocomArquivosTxt.txt", encoding="utf-8") as exemplo:
    for linha in exemplo:
        linha_limpa = linha.strip()
        print(linha_limpa)