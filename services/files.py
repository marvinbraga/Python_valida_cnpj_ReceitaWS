import pandas as pd


class FileManager:
    """
    Classe para gerenciar operações de arquivo, como leitura e conversão de formatos.

    Atributos:
        file_path (str): Caminho do arquivo a ser manipulado.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def get_data_from_excel(self):
        """
        Gera uma sequência de CNPJs a partir de um arquivo Excel com múltiplas abas.
        Cada CNPJ é gerado um de cada vez.
        """
        df = pd.read_excel(self.file_path, sheet_name=None)
        for _, value in df.items():
            for cnpj in value["CNPJ"]:
                yield cnpj
