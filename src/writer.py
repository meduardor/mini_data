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
        open(arquivo)


def documentCsv(filename):
    caminho = '.dataset/'
    arquivo = caminho + (filename + ".csv")
    if not os.path.exists(caminho):
       os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo)


def writerDatajson(filename, count):
    lista_dados = []
# Dados que serão trasmitidos para o arquivo
    key = input("Digite uma Chave: ")
    lista_dados.append(key)
    value = input("Digite um Valor: ")
    lista_dados.append(value)
# Criação do Arquivo que vai receber os dados
    caminho = '.dataset/'
    arquivo = caminho + (filename + ".json")
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo, 'w')

    for key, value in range(count):
        lista_dados.append(key)
        lista_dados.append(value)
# TODO: Criar uma lista unica, fazer um split para converter em um dict
    lista_key = [lista_dados[0]]
    lista_value = [lista_dados[1]]
    lista_salvar = [dict(zip(lista_key, lista_value))]
    dictData = {"Dados":lista_salvar}
    dictData = json.dumps(dictData, indent=4, sort_keys=False)
    try:
        abrir = open(arquivo, 'r+')
        conteudo = abrir.readlines()
        conteudo.append(dictData)
        abrir = open(arquivo, 'w')
        abrir.writelines(conteudo)
        abrir.close()
    except Exception as Error:
        print("Não foi possivel iterar os dados {}".format(dictData))


def writerDataCsv():
    # TODO: Escrever função para gravar dados em arquivos csv
    pass
