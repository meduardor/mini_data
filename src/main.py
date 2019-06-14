#!/usr/bin/env python3


import writer as WriterCsv
import writer as WriterJson
import read as ReadJson

nameEx = input('Qual extensão? json/csv.\n > ').upper()
dataName = input('Nome do Banco\n > ').upper()
count = int(input('Quantidade de dados.\n > '))

# TODO: Definir funções de saida para cada tarefa
# TODO: Criar uma Chave primaria para identificar os dados.


def escrever_json(name, data):
    # TODO: Refatorar essa função de acordo com as novas funcionalidades do
    # NOTE: Exemplo de dados de entrada.(Não permanentes)

    # Criação da base de dados in JSON
    escrita_json = WriterJson.DocJson(name)

    # Número definido para entrada de e dados
    count = int(input('Quantos dados vai escrever: '))

    # Chamada do Modulo writer e das funções de escritas Json
    dados_json_key = WriterJson()
    dados_json_value = WriterJson()

    # TODO: Fazer testes sobre a entrada de dados das lista.
    # Listas de dados
    data_json_value = []
    data_json_key = []

    # Condicional de entrada de dados
    if not data_json_key == 0:
        for i in range(count):
            data_json_key.append(input('Digite nome dos Campos: '))
            dados_json_key.DataJson(data_json_key, data)
        else:
            pass
    elif not data_json_value == 0:
        for x in range(count):
            data_json_value.append(input('Digite os valores: '))
            dados_json_value.DataJson(data_json_value, data)
        else:
            pass

    # Converte os dos da lista em Dict e grava no arquivo JSON
    escrita_dados_json = WriterJson.ConvertJson(escrita_json,
                                                dados_json_key,
                                                dados_json_value)
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
