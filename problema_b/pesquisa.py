"""Problema B"""

NOME_ARQUIVO_ENTRADA = "pesquisa.in"
NOME_ARQUIVO_SAIDA = "pesquisa.out"

with open(NOME_ARQUIVO_ENTRADA, 'r') as entrada:
    with open(NOME_ARQUIVO_SAIDA, 'w') as saida:
        CIDADE = ""
        ELEITORES = ""
        DATA = ""
        VOTOS = list()
        CANDIDATOS = list()
        AMOSTRAGEM = 0

        for linha in entrada:
            linha = linha.rstrip()
            if CIDADE == "" and len(VOTOS) == 0:
                TEMP = linha.split(';')
                CIDADE = TEMP[0]
                ELEITORES = TEMP[1]
                DATA = TEMP[2]
            elif len(VOTOS) == 0:
                TEMP = linha.split(';')
                for candidato in TEMP:
                    CANDIDATOS.append(candidato)
                    VOTOS.append(0)
                CANDIDATOS.append('Nulos')
                VOTOS.append(0)
                CANDIDATOS.append('Brancos')
                VOTOS.append(0)
                CANDIDATOS.append('Indecisos')
                VOTOS.append(0)
                AMOSTRAGEM = 0
            else:
                if linha == "Z":
                    saida.write(CIDADE + " " + ELEITORES + " " + DATA + " " + str(AMOSTRAGEM) + " " + str(len(CANDIDATOS) - 3) + "\n")
                    for i in range(0, len(VOTOS), 1):
                        CALC = VOTOS[i] * 100 / AMOSTRAGEM
                        saida.write(str(CANDIDATOS[i]) + " " + ("%.1f" % CALC).replace('.', ',') + "\n")
                    CIDADE = ""
                    VOTOS = list()
                    CANDIDATOS = list()
                elif linha == "N":
                    VOTOS[len(CANDIDATOS) - 3] += 1
                    AMOSTRAGEM += 1
                elif linha == "B":
                    VOTOS[len(CANDIDATOS) - 2] += 1
                    AMOSTRAGEM += 1
                elif linha == "I":
                    VOTOS[len(CANDIDATOS) - 1] += 1
                    AMOSTRAGEM += 1
                else:
                    VOTOS[int(linha) - 1] += 1
                    AMOSTRAGEM += 1
