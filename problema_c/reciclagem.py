"""Problema C"""

NOME_ARQUIVO_ENTRADA = "reciclagem.in"
NOME_ARQUIVO_SAIDA = "reciclagem.out"

RESULTADO = dict()
ORDEM = []
CARGAS = 0

with open(NOME_ARQUIVO_ENTRADA, 'r') as entrada:
    with open(NOME_ARQUIVO_SAIDA, 'w') as saida:
        for linha in entrada:
            linha = linha.rstrip()
            if linha == "0":
                if CARGAS > 0:
                    saida.write(str(CARGAS) + " " +
                        str(RESULTADO['ME']) + " " +
                        str(RESULTADO['PA']) + " " +
                        str(RESULTADO['PL']) + " " +
                        str(RESULTADO['VI']) + "\n")
                break
            temp = linha.split(" ")
            if 'ME' in temp or 'PA' in temp or 'PL' in temp or 'VI' in temp:
                if CARGAS > 0:
                    saida.write(str(CARGAS) + " " +
                        str(RESULTADO['ME']) + " " +
                        str(RESULTADO['PA']) + " " +
                        str(RESULTADO['PL']) + " " +
                        str(RESULTADO['VI']) + "\n")
                RESULTADO['ME'] = 0
                RESULTADO['PA'] = 0
                RESULTADO['PL'] = 0
                RESULTADO['VI'] = 0
                CARGAS = int(temp[0])
                ORDEM = temp[1:]
            else:
                for i in range(0, len(ORDEM), 1):
                    RESULTADO[ORDEM[i]] = RESULTADO[ORDEM[i]] + int(temp[i])

