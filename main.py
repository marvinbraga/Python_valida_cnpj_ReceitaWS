from services.analysers import CNPJAnalyzer
from services.apis import ReceitaFederalService
from services.files import FileManager

CNPJAnalyzer(
    ReceitaFederalService('https://www.receitaws.com.br/v1/cnpj')
).analyze_cnpj(
    FileManager('./.res/contratantes.xlsx').get_data_from_excel()
)
