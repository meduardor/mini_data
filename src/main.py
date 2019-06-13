#!/usr/bin/env python3


import writer as WriterCsv
import writer as WriterJson
import read as ReadJson

nameEx = input('Qual extensão? json/csv.\n > ').upper()
dataName = input('Nome do Banco\n > ').upper()
count = int(input('Quantidade de dados.\n > '))

# TODO: Definir funções de saida para cada tarefa


def escrever_json(name, data):
    # TODO: Refatorar essa função de acordo com as novas funcionalidades do
    # NOTE: Exemplo de dados de entrada.(Não permanentes)
    # Dados constantes "keys"
    data_json_key = [

        'Nome:',
        'Data:',
        'Senha:',
        'Pergunta:'
    ]
    # Dados variaveis entrada do usuario  
    data_json_value = [data]
    # Chamada do Modulo writer e das funções de escritas Json  
    escrita_json = WriterJson.DocJson(name)
    dados_json = WriterJson.DataJson(data_json_key, data_json_value)
    escrita_dados_json = WriterJson.ConvertJson(escrita_json, dados_json)
    return escrita_dados_json


def escrever_csv():
    escrita_csv = WriterCsv.DocCsv(nameEx)
    dados_csv = WriterCsv.DataCsv(dataName)
    escrita_dados_csv = WriterCsv.WriterDataCsv(escrita_csv, dados_csv)
    return escrita_dados_csv


def ver_json(name):
    '''Ver os dados do Documento json'''
    verDados = ReadJson.verDoc(name)
    return verDados


def ver_csv():
    pass


def backup():
    pass


def connection():
    pass


def users():
    pass


if __name__ == '__main__':
    stopdata = 0
    while True:
        if stopdata <= count:
            stopdata += 1
            escrever_json(nameEx, dataName)

        elif stopdata >= count:
            break
