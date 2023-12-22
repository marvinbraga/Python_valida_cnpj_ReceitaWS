# PoC CNPJ Analyzer | ReceitaWS
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Poetry Version](https://img.shields.io/badge/poetry-1.1.4-blue.svg)](https://python-poetry.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Esta Prova de Conceito (PoC) demonstra a funcionalidade de análise de CNPJs utilizando uma API da Receita Federal e
manipulação de arquivos Excel e CSV em Python, gerenciada pelo Poetry.

## Estrutura do Projeto

O projeto é composto por:

- `main.py`: Script principal para análise de CNPJs.
- `/services`: Módulos de serviços para análise de CNPJ, API da Receita Federal e gerenciamento de arquivos.
- `/utils/make_data.py`: Script para geração de dados fictícios de contratantes.
- `/.res`: Diretório para o arquivo Excel com dados fictícios.

## Pré-requisitos

Certifique-se de ter o Python 3.10 ou superior e o Poetry instalados em seu sistema.

## Configuração do Projeto

1. **Instalação das Dependências**: Dentro do diretório do projeto, execute o seguinte comando para instalar todas as
   dependências listadas no `pyproject.toml`:

    ```bash
    poetry install
    ```

2. **Gerar Dados Fictícios**: Execute o script `make_data.py` para criar um arquivo Excel com dados fictícios:

    ```bash
    python /utils/make_data.py
    ```

   Isso irá gerar o arquivo `contratantes.xlsx` no diretório `/.res`.

## Executando o Projeto

Após configurar o ambiente, você pode executar o script principal com o seguinte comando:

```bash
python main.py
```

Isso iniciará a análise dos CNPJs, lendo os dados do arquivo Excel, convertendo-os para CSV e realizando consultas na
API da Receita Federal.

## Saída Esperada

O script exibirá no console a situação dos CNPJs analisados e gravará informações relevantes no arquivo `RelCNPJ.txt`.


Adicionar badges (insígnias) ao `readme.md` é uma ótima maneira de fornecer informações visuais rápidas sobre o estado do seu projeto, como status de build, cobertura de testes, versão da linguagem Python, etc. Vou adicionar algumas sugestões de badges ao seu `readme.md`:
