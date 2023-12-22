import re

import requests


class ReceitaFederalService:
    """
    Classe para interagir com a API da Receita Federal para consulta de CNPJs.

    Atributos:
        base_url (str): URL base da API da Receita Federal.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def consulta_cnpj(self, cnpj):
        """
        Consulta um CNPJ na API da Receita Federal e retorna os dados.

        :param:
            cnpj (str): CNPJ a ser consultado.

        :return:
            dict: Dados retornados pela API para o CNPJ especificado.
        """
        cnpj = re.sub('[^0-9]+', '', cnpj)
        url = f'{self.base_url}/{cnpj}'
        response = requests.get(url)
        return response.json()

    def validar_cnpj(self, cnpj):
        """
        Verifica se um CNPJ é válido e está ativo.

        :param:
            cnpj (str): CNPJ a ser validado.

        :return:
            bool: True se o CNPJ é válido e está ativo, False caso contrário.
        """
        data = self.consulta_cnpj(cnpj)
        return data['status'] == 'OK' and data['situacao'] == 'ATIVA'

    def get_situacao_cnpj(self, cnpj):
        """
        Obtém a situação de um CNPJ.

        :param:
            cnpj (str): CNPJ cuja situação será obtida.

        :return:
            str: Situação do CNPJ.
        """
        data = self.consulta_cnpj(cnpj)
        return data.get('situacao')
