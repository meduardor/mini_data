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
    ''' Escreve arquivo json e add dados no arquivo'''

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
# TODO: Refatorar essa parte do codigo
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
    '''Escrever documentos csv e insere dados no documento'''

    count = int(input('Digite numero de campos: '))
    fieldnames = []
    fieldcampos = []

    for i in range(count):
        fieldnames.append(input('Digite o Nome do campos: '))
        Campos = dict(zip(fieldnames, ' '))

    for x in range(count):
        fieldcampos.append(input('Digite os Campos: '))

    # TODO: Mudar a forma de atrelar os valores no dict
    # para enviar para o documento

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
        if fieldnames in csv_file:
            pass
        else:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                    delimiter='\t')
            writer.writeheader()
            writer.writerow(Campos)
        csv_file.close()
    complete = True
    while True:
        with open(arquivo, 'a+') as csv_file:
            writer = csv.writer(csv_file)
            for x in range(count):
                writer.writerow(fieldcampos)
# TODO: Escrever dois loops para iterar os dados no documento
