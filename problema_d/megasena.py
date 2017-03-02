"""Problema D"""
import operator

NOME_ARQUIVO_ENTRADA = "megasena.in"
NOME_ARQUIVO_SAIDA = "megasena.out"

DEZENAS = dict.fromkeys(range(1, 61), 0)

with open(NOME_ARQUIVO_ENTRADA, 'r') as entrada:
    with open(NOME_ARQUIVO_SAIDA, 'w') as saida:
        for linha in entrada:
            if linha == "0":
                break
            temp = linha.split(';')[2:]
            for num in temp:
                DEZENAS[int(num)] += 1
        SORTED = sorted(DEZENAS.items(), key=operator.itemgetter(1), reverse=True)
        COUNT = 1
        for num, qtd in SORTED:
            saida.write(str(COUNT) + " " + str(num) + " " + str(qtd) + "\n")
            COUNT += 1
