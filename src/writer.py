#!/usr/bin/env python3

# Modulo Writer


import os
import json
import csv


class WriterJson():
    '''Escreve documentos Json'''

    def __init__(self, lista_key, lista_value):
        self.lista_key = list
        self.lista_value = list

    def DocJson(filename):
        '''Cria arquivo Json'''
        caminho = '.dataset/'
        arquivo = caminho + (filename + ".json")
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        if not os.path.exists(arquivo):
            open(arquivo, 'w')

    def DataJson(self, arquivo, *data):
        '''Grava os dados que serão processados obj -> [obj]'''

        # Loop for para armazenar os dados.
        # Armazenamento de dados na lista_key.
        if os.path.exists(arquivo) and self.lista_key == []:
            with open(arquivo, 'r+') as f:
                f.readlines()
                for i in data:
                    self.lista_key.append(input('Digite nome dos Campos: '))
        elif not os.path.exists(arquivo) and data in f.readlines():
            print('Crie o Arquivo para Gravação de dados!!')
            pass
        # Armazenamento dos  dados de valores na lista_value.
        # TODO(merds): Tirar as instancias de class das funções.

        def dataJson_value():
            if os.path.exists(arquivo):
                with open(arquivo, 'r+') as f:
                    f.readlines()
            elif data in f.readlines():
                for item in data:
                    self.lista_value.append(input('Digite os Valores: '))

    def ConvertJson(self, l_value, l_key, filename, *data):
        '''Converte Dict Python em dados Json'''
        l_value = WriterJson.DataJson(self.lista_value, filename)
        l_value.dataJson_value()
        l_key = WriterJson.DataJson(self.lista_key)

        __lista_salvar = [dict(zip(l_key, l_value))]
        __dictData = {"Dados": __lista_salvar}
        __dictData = json.dumps(__dictData,
                                indent=4,
                                sort_keys=False)
        try:
            arquivo = WriterJson.DocJson(filename)
            # TODO: Ver se o uso da função dentro da classe é dessa forma
            abrir = open(arquivo, 'r+')
            conteudo = arquivo.readlines()
            conteudo.append(__dictData)
            abrir = open(arquivo, 'w')
            abrir.writelines(conteudo)
            abrir.close()
        except FileNotFoundError:
            print("Não foi possivel escrever os Dados {}, {}"
                  .format(__dictData))


class WriterCsv():
    '''Escrever documento csv'''

    def __init__(self, fieldcampos, fieldnames):
        self.fieldcampos = fieldcampos
        self.fieldnames = fieldnames

    def DocCsv(filename):
        __caminho = '.dataset/csv/'
        __arquivo = __caminho + (filename + ".csv")
        if not os.path.exists(__caminho):
            os.makedirs(__caminho)
        if not os.path.exists(__arquivo):
            open(__arquivo, 'w')

    def DataCsv(self, **data):
        self.fieldnames = []
        self.fieldcampos = []
        for i in self.fieldnames:
            self.fieldnames.append(data)

        for x in self.fieldcampos:
            self.fieldcampos.append(data)

    def WriterDataCsv(self, **data):
        arquivo = WriterCsv.DocCsv(self.filename)
        try:
            with open(arquivo, 'w+', newlines='') as csvfile:
                datawriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|',
                                        quoting=csv.QUOTE_MINIMAL)
                datawriter.writerow(data)
        except FileNotFoundError:
            print('O arquivo csv não existe')

    # TODO: pensar a forma de passar os **args
    # TODO: E de escrever eles no Documento
