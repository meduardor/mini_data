#!/usr/bin/env python3


import os
import sys
import json


def documentJson(filename):
    caminho = '.dataset/'
    arquivo = caminho + (filename + ".json")
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo, "w+")


def documentCsv(filename):
    caminho = '.dataset/'
    arquivo = caminho + (filename + ".csv")
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo, "w+")


def writerDatajson(nameKeys, nameValues, filename):
    # TODO: Função para criar a Dict que vai ser escrito no arquivo ".Json"
    # dictData = {'nameKeys': 'nameValues'}
    arquivo = documentJson(filename)
    with open(arquivo, "w+") as abrir:
            conteudo = abrir.readlines()
            try:
                for dictData in json.JSONEncoder().iterencode({"nameKeys": "nameValues"}):
                    conteudo.append(str(dictData))
                    abrir = open(arquivo, "w")
                    abrir.writelines(conteudo)
            except ValueError:
               print('ERROR: Objeto não interou no Dict')
            else:
                abrir.close()
                return arquivo


def writerDataCsv():
    # TODO: Escrever função para gravar dados em arquivos csv
    pass
