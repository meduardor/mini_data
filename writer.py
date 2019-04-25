#!/usr/bin/env python3


import os


def documentJson(filename):
    caminho = '~/.dataset'
    # TODO: concatenar e criar o arquivo junto com a ext ".json"
    arquivo = caminho + filename
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo)


def writerData(arquivo, *filename, nameKeys):
    keys = open(arquivo, "w+")
    keys.write(nameKeys)
    keys.close()