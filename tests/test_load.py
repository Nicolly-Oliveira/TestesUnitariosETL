import pytest
import os
from etl.load import load_data_to_csv

OUTPUT_FILE_PATH = "/home/nicolly-silva/TesteUnitarioETL/data_source/dados_gerados_teste.csv"


def test_load_data_to_csv():
    # Dados simulados para o carregamento
    transformed_data = [
        {"id": "1", "name": "Alice"},
        {"id": "2", "name": "Bob"}
    ]

    # Teste de Carga
    load_data_to_csv(transformed_data, OUTPUT_FILE_PATH)

    # Verificar se o arquivo foi criado
    assert os.path.exists(OUTPUT_FILE_PATH), f"O arquivo {OUTPUT_FILE_PATH} não foi criado!"

    # Limpeza após o teste
    if os.path.exists(OUTPUT_FILE_PATH):
        os.remove(OUTPUT_FILE_PATH)
