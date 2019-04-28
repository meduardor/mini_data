#!/usr/bin/env python3


import os


def documentJson(filename):
    caminho = '~/.dataset/'
    # TODO: concatenar e criar o arquivo junto com a ext ".json"
    arquivo = caminho + filename
    if not os.path.exists(caminho):
        os.mkdir(caminho)
    if not os.path.exists(arquivo):
        open(arquivo)


def writerData(nameKeys, nameValues):
    dictData = {}
    arquivo = documentJson(filename)
    keysValues = open(arquivo, "w+")
    for keysValues in dictData:
        dictData["nameKeys"] = nameValues
        keysValues.write(dictData)
        keysValues.close()


# TODO: Escrever um looping para determinar a quantidade valores de  entra.


def readData(dictData, nameKeys, nameValues):
    if dictData == {nameKeys}:
        readDataKeys = writerData(nameKeys)
        readDataKeys.readlines()
        return readDataKeys
    elif dictData == {nameValues}:
        readDataValues = writerData(nameValues)
        readDataValues.readlines()
        return readDataValues
    else:
        print("ERROR")
        
        # TODO: Escrever o modulo read || de forma imperativa escrever todas
        # as funções no module writer.
