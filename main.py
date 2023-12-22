from services.analysers import CNPJAnalyzer
from services.apis import ReceitaFederalService
from services.files import FileManager

receita_service = ReceitaFederalService('https://www.receitaws.com.br/v1/cnpj')
file_manager = FileManager('./.res/contratantes.xlsx')
file_manager.gera_csv_from_excel()

cnpj_analyzer = CNPJAnalyzer(receita_service, file_manager)
cnpj_list = file_manager.read_csv()
cnpj_analyzer.analyze_cnpj(cnpj_list)
