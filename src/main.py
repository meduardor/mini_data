#!/usr/bin/env python3


import writer as WriterCsv
import writer as WriterJson
import read

nameEx = input('Qual extensão? json/csv.\n > ').upper()
dataName = input('Nome do Banco\n > ').upper()
count = int(input('Quantidade de dados.\n > '))

# TODO: Definir funções de saida para cada tarefa


def escrever(name, data):
    # TODO: Refatorar essa função de acordo com as novas funcionalidades do
    # Modulo writer.
    if name == "JSON":
        escrita_json = WriterJson.DocJson(nameEx)
        dados_json = WriterJson.DataJson(dataName)
        escrita_dados_json = WriterJson.ConvertJson(escrita_json, dados_json)
        return escrita_dados_json

    elif name == "CSV":
        escrita_csv = WriterCsv.DocCsv(nameEx)
        dados_csv = WriterCsv.DataCsv(dataName)
        escrita_dados_csv = WriterCsv.WriterDataCsv(escrita_csv, dados_csv)
        return escrita_dados_csv


def ver(data, name):
    if name == "JSON":
        ler = read.ReadDataJson(data)
        return ler


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
            escrever(nameEx, dataName)

        elif stopdata >= count:
            break
