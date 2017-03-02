"""Problema A"""

NOME_ARQUIVO_ENTRADA = "excel.in"
NOME_ARQUIVO_SAIDA = "excel.out"

with open(NOME_ARQUIVO_ENTRADA, 'r') as entrada:
    with open(NOME_ARQUIVO_SAIDA, 'w') as saida:
        for linha in entrada:
            if linha == "0":
                break
            temp = linha.rstrip()
            valor = 0
            for i in range(0, len(temp), 1):
                valor += (ord(temp[i]) - 64) * pow(26, len(temp) - 1 - i)
            saida.write(str(valor) + '\n')
