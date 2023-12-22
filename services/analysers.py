import re
import time

from services.apis import ReceitaFederalService


class CNPJAnalyzer:
    """
    Classe principal para analisar CNPJs utilizando o serviço da Receita Federal.

    Atributos:
        receita_service (ReceitaFederalService): Instância do serviço de consulta à Receita Federal.
    """

    def __init__(self, receita_service: ReceitaFederalService):
        self.receita_service = receita_service

    def save_data(self, cnpj, situacao):
        """
        Salva a situação do CNPJ em um arquivo.

        Parâmetros:
            cnpj (str): CNPJ analisado.
            situacao (str): Situação do CNPJ obtida da Receita Federal.
        """
        with open("RelCNPJ.txt", "a", encoding='utf-8') as file:
            file.write(f'A situação do CNPJ {cnpj} é {situacao}.\n')

        print(f'A situação do CNPJ {cnpj} é {situacao}')
        return self

    def analyze_cnpj(self, cnpj_list):
        """
        Analisa uma sequência de CNPJs, consultando a situação de cada um na Receita Federal.

        :param:
            cnpj_list (generator): Gerador que produz CNPJs.
        """
        for cnpj in cnpj_list:
            cnpj = re.sub('[^0-9]+', '', str(cnpj))
            if len(cnpj) > 5:
                time.sleep(21)  # Mantendo a regra do plano gratuito
                situacao = self.receita_service.get_situacao_cnpj(cnpj)
                self.save_data(cnpj, situacao)
