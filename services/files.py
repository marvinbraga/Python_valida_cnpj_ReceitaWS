import csv

import pandas as pd


class FileManager:
    """
    Classe para gerenciar operações de arquivo, como leitura e conversão de formatos.

    Atributos:
        file_path (str): Caminho do arquivo a ser manipulado.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def gera_csv_from_excel(self):
        """
        Gera arquivos CSV a partir de um arquivo Excel com múltiplas abas.
        Cada aba é salva como um arquivo CSV separado.
        """
        df = pd.read_excel(self.file_path, sheet_name=None)
        for key, value in df.items():
            value.to_csv(f'{key}.csv')

    def read_csv(self):
        """
        Lê um arquivo CSV e retorna seu conteúdo como uma lista.

        :return:
            list: Conteúdo do arquivo CSV como uma lista de linhas.
        """
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
