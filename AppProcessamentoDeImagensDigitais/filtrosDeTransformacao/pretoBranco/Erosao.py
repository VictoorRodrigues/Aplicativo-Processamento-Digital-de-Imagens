# -*- coding: utf-8 -*-

import sys
import numpy as np


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    linha = entrada.readline()  # P1
    linha = entrada.readline()  # Comentário
    linha = entrada.readline()  # Dimensões da imagem
    dimensoes = linha.split()  # Lista com as dimensões
    largura = int(dimensoes[0])
    altura = int(dimensoes[1])
    dimensoes = np.asarray(dimensoes, dtype=int)

    linhas = entrada.readlines()
    linhas = [x.strip() for x in linhas]

    stringLonga = concatenarLista(linhas)
    imagem = np.array(list(stringLonga))
    imagem = np.reshape(imagem, [dimensoes[1], dimensoes[0]])
    imagem = imagem.astype(int)

    # Elemento Estruturante 3x3
    # elemento = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    # Elemento Estruturante 5x5
    # elemento = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

    # Elemento Estruturante 7x7
    # elemento = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1],
    #            [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]

    # Elemento Estruturante 9x9
    elemento = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

    # Array numpy do elemento estruturante
    elemento = np.asarray(elemento)

    # Pegar pixel posição pixel central
    es = int((len(elemento) - 1) / 2)

    escreverImagemSaida(entrada, largura, altura, imagem, elemento, es)


def concatenarLista(list):
    result = ''
    for element in list:
        result += str(element)
    return result


def escreverImagemSaida(entrada, largura, altura, imagem, elemento, es):
    saida = open(sys.argv[2], "w+")
    saida.write("P1\n")
    saida.write("#Criado por Victor\n")
    saida.write(str(largura))
    saida.write(" ")
    saida.write(str(altura))
    saida.write("\n")

    # Fazer cópia da imagem original
    imagemTransformada = imagem.copy()

    for px in range(es, len(imagem) - es):
        for py in range(es, len(imagem[1]) - es):
            if imagem[px][py] == 0:
                for ex in range(len(elemento)):
                    for ey in range(len(elemento[1])):
                        if elemento[ex][ey] == 1:
                            imagemTransformada[px - es + ex][py - es + ey] = 0

    for linha in range(len(imagemTransformada)):
        for coluna in range(len(imagemTransformada[1])):
            saida.write(str(imagemTransformada[linha][coluna]))
            saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()

