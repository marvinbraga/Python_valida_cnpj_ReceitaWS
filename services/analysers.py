import re
import time

from services.apis import ReceitaFederalService
from services.files import FileManager


class CNPJAnalyzer:
    """
    Classe principal para analisar CNPJs utilizando o serviço da Receita Federal.

    :argument:
        receita_service (ReceitaFederalService): Instância do serviço de consulta à Receita Federal.
        file_manager (FileManager): Instância do gerenciador de arquivos.
    """

    def __init__(self, receita_service: ReceitaFederalService, file_manager: FileManager):
        self.receita_service = receita_service
        self.file_manager = file_manager

    def analyze_cnpj(self, cnpj_list):
        """
        Analisa uma lista de CNPJs, consultando a situação de cada um na Receita Federal.

        Parâmetros:
            cnpj_list (list): Lista de CNPJs a serem analisados.
        """
        for cnpj in cnpj_list:
            cnpj = re.sub('[^0-9]+', '', cnpj)
            if len(cnpj) > 5:
                time.sleep(21)  # Mantendo a regra do plano gratuito
                situacao = self.receita_service.get_situacao_cnpj(cnpj)
