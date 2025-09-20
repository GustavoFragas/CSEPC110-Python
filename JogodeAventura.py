"""
Gustavo Fragas Cunha
20 anos
06/09/2025

RPG

-Criação de Métodos para facilitar e colocar alguns efeitos visuais

Comentário da minha mãe: "Ficou bem divertido, você é tipo um hacker né? Como você fez isso, é literalmente muita linha o que você teve que escrever"

"""
import time

"""
Funções
"""
def pontinhos():
    for i in range(40):
        print("-", end="", flush=True)
        time.sleep(0.1)

def narrador(texto, atraso = 0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(atraso)
    print()       
"""
Fim das funções
"""

print("Seja bem vindo ao RPG FRAGASTORM")
pontinhos()
print()
print ("Antes de começar, vamos escolher a classe do seu personagem! ")
classe_personagem = input("Qual é a classe do seu personagem? \n 1 - Ladino \n 2 - Bardo \n 3 - Mago \n 4 - Guerreiro \n ")
print()
pontinhos()
print()


match classe_personagem:
    case "1":  # Ladino
        narrador("*Está um lindo dia e você decide ir a um bar muito conhecido em uma cidade chamada HOMETOWN")
        narrador("*Você entra nesse bar um pouco desconfiado, muitas pessoas te olham de maneira estranha, tem orks tocando música de fundo, mas você sente a vontade de sentar ao lado do bartender chamado Goblinger")
        narrador("*Ele te oferece uma bebida ALCOÓLICA e te pergunta:")
        narrador("Goblinger: Boa tarde cavalheiro, aceita essa humilde bebida? (SIM ou NAO ou IGNORAR)")

        while True:
            primeira_decisao = input("> ")

            if primeira_decisao.upper() in ["SIM", "S"]:
                narrador("*Você toma da bebida")
                narrador("*Você a saboreou e realmente gostou, mas se sente um pouco estranho fisicamente")
                narrador("*Você se sente um pouco zonzo a cada segundo e do nada")
                narrador("*CRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASH")
                narrador("<ALGUÉM QUEBROU UMA GARRAFA DE VIDRO NA SUA CABEÇA>")

                narrador("Você consegue se levantar? (SIM ou NAO)")
                segunda_decisao = input("> ")

                if segunda_decisao.upper() in ["SIM", "S"]:
                    narrador("*Você se levanta e tenta fugir do bar rapidamente, mas alguém te bloqueia o caminho!")
                    narrador("Você enfrenta a pessoa ou tenta se esconder? (ENFRENTAR ou ESCONDER)")
                    terceira_decisao = input("> ")
                    if terceira_decisao.upper() == "ENFRENTAR":
                        narrador("*Você enfrenta a pessoa e consegue escapar do bar ferido, mas vivo!")
                    elif terceira_decisao.upper() == "ESCONDER":
                        narrador("*Você se esconde e espera alguém vir te salvar do perigo iminente")

                elif segunda_decisao.upper() in ["NAO", "N"]:
                    narrador("*Você cai no chão inconsciente e acorda algumas horas depois com dor de cabeça insuportável")
                    narrador("Você tenta procurar ajuda ou fica esperando alguém encontrar você? (PROCURAR ou ESPERAR)")
                    terceira_decisao = input("> ")
                    if terceira_decisao.upper() == "PROCURAR":
                        narrador("*Você consegue se arrastar até a porta e encontrar um aliado")
                    elif terceira_decisao.upper() == "ESPERAR":
                        narrador("*Alguém te encontra e te salva, mas você perdeu todos os seus pertences")

                break

            elif primeira_decisao.upper() in ["NAO", "N", "NÃO"]:
                narrador("*Você recusa educadamente a bebida de Goblinger")

                narrador("Goblinger te pergunta: deseja sentar e conversar um pouco? (SIM ou NAO)")
                segunda_decisao = input("> ")

                if segunda_decisao.upper() in ["SIM", "S"]:
                    narrador("*Vocês começam a conversar e ele te dá informações valiosas sobre a cidade")
                    narrador("Você aceita a missão que ele propõe ou prefere recusar? (ACEITAR ou RECUSAR)")
                    terceira_decisao = input("> ")
                    if terceira_decisao.upper() == "ACEITAR":
                        narrador("*Você aceita a missão e se prepara para uma aventura emocionante")
                    elif terceira_decisao.upper() == "RECUSAR":
                        narrador("*Você recusa a missão, mas ganha a confiança do bartender")

                elif segunda_decisao.upper() in ["NAO", "N"]:
                    narrador("*Você decide não interagir e continua observando o bar de longe")
                    narrador("Você entra em outro bar ou continua explorando a cidade? (ENTRAR ou EXPLORAR)")
                    terceira_decisao = input("> ")
                    if terceira_decisao.upper() == "ENTRAR":
                        narrador("*Você entra em outro bar e encontra novos personagens interessantes")
                    elif terceira_decisao.upper() == "EXPLORAR":
                        narrador("*Você explora a cidade e descobre segredos escondidos nas ruas")

                break

            elif primeira_decisao.upper() == "IGNORAR":
                narrador("*Você ignora Goblinger e olha ao redor do bar, percebendo coisas estranhas acontecendo")

                narrador("Você decide investigar o bar ou sair rapidamente? (INVESTIGAR ou SAIR)")
                segunda_decisao = input("> ")

                if segunda_decisao.upper() == "INVESTIGAR":
                    narrador("*Você começa a andar pelo bar, tentando descobrir segredos escondidos nas sombras")
                    narrador("Você entra na sala dos fundos ou fica observando de longe? (ENTRAR ou OBSERVAR)")
                    terceira_decisao = input("> ")
                    if terceira_decisao.upper() == "ENTRAR":
                        narrador("*Você entra e encontra um mapa secreto da cidade")
                    elif terceira_decisao.upper() == "OBSERVAR":
                        narrador("*Você percebe um movimento suspeito sem se expor")

                elif segunda_decisao.upper() == "SAIR":
                    narrador("*Você sai rapidamente do bar, evitando problemas, mas sentindo que perdeu algo importante")
                    narrador("Você vai para a taverna da esquina ou volta para sua hospedaria? (TAVERNA ou HOSPEDARIA)")
                    terceira_decisao = input("> ")
                    if terceira_decisao.upper() == "TAVERNA":
                        narrador("*Você encontra viajantes que compartilham histórias fascinantes")
                    elif terceira_decisao.upper() == "HOSPEDARIA":
                        narrador("*Você descansa e planeja seu próximo passo na cidade")

                break

            else:
                narrador("Cavalheiro, não escutei o que você disse, poderia repetir? (SIM, NAO ou IGNORAR)")

    case "2":
        print("Em desenvolvimento")
    
    case "3":
        print("Em desenvolvimento")

    case "4":
        print("Em desenvolvimento")