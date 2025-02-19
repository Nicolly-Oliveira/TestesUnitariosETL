# Projeto ETL - Testes Automatizados

Este repositório contém um projeto de **ETL (Extração, Transformação e Carga)**, com testes automatizados usando o framework **pytest** para garantir a integridade do processo de ETL.

## Estrutura do Projeto

- **`etl/`**: Contém os módulos de extração, transformação e carga de dados.
- **`tests/`**: Contém os testes para cada etapa do processo ETL.

## Funcionalidades

- **Extração**: Leitura de dados de um arquivo CSV.
- **Transformação**: Limpeza de dados (remoção de espaços), formatação de data de nascimento e cálculo de idade.
- **Carga**: Salvamento dos dados transformados em um novo arquivo CSV.

## Como Rodar os Testes

1. **Instale o `pytest`**:

   Para rodar os testes, você precisará do **pytest**. Caso não tenha o pytest instalado, instale-o com:

   ```bash
   pip install pytest
   
2. **Rodando os Testes**:

   Para rodar todos os testes do projeto, execute o comando abaixo no terminal:

   ```bash
   pytest nome_arquivo_teste.py
   
2. **Verificando os Resultados**:

   O pytest irá exibir o resultado dos testes diretamente no terminal, indicando se algum teste falhou.
   
   


