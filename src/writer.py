#!/usr/bin/env python3


import os
import json
import csv


def documentCsv(filename):
    caminho = '.dataset/'
    arquivo = caminho + (filename + ".csv")
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo)


def writerDatajson(filename):
    lista_key = []
    lista_value = []
    count = int(input('Digite o numero de Dados: '))
    # Dados que serão trasmitidos para o arquivo
    # Incluindo dados na lista.
    for i in range(count):
        lista_key.append(input("Digite uma Chave: "))

    for x in range(count):
        lista_value.append(input("Digite um Valor: "))

    # Criação do Arquivo que vai receber os dados

    caminho = '.dataset/'
    arquivo = caminho + (filename + ".json")
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo, 'w')

    # Conversão das listas em dict, para a escrita no documento ".json"

    lista_salvar = [dict(zip(lista_key, lista_value))]
    dictData = {"Dados": lista_salvar}
    dictData = json.dumps(dictData, indent=4, sort_keys=False)
    try:
        abrir = open(arquivo, 'r+')
        conteudo = abrir.readlines()
        conteudo.append(dictData)
        abrir = open(arquivo, 'w')
        abrir.writelines(conteudo)
        abrir.close()
    except Exception as Error:
        print("Não foi possivel iterar os dados {}, {}".format(dictData,
                                                               Error))


def writerDataCsv(filename):
    count = int(input('Digite numero de campos: '))
    fieldnames = []
    fieldcampos = []

    for i in range(count):
        fieldnames.append(input('Digite o Nome do campos: '))
    for x in range(count):
        fieldcampos.append(input('Digite os Campos: '))

    lista_salvar = dict(zip(fieldnames, ' '))
    # TODO: Mudar a forma de atrelar os valores no dict
    # para enviar para o documento
    lista_salvar1 = dict(zip(' ', fieldcampos))
# Criação dos arquivos csv
    caminho = '.dataset/csv/'
    arquivo = caminho + (filename + ".csv")
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(arquivo):
        open(arquivo, 'w')
# TODO: Escrever a primeira fileira de descrição das informações
# TODO: Depois append dos dados nas informações

    with open(arquivo, 'w+', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(lista_salvar)
        with open(arquivo, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file,
                                    fieldnames=fieldnames,
                                    delimiter='\t')
            writer.writerow(lista_salvar1)
