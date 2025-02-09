# tests/test_extract.py
import pytest
import os
from etl.extract import extract_csv

EXISTING_FILE_PATH = "/home/nicolly-silva/TesteUnitarioETL/data_source/dados_originais.csv"


def test_extract_csv():

    # Verificar se o arquivo de entrada realmente existe
    assert os.path.exists(EXISTING_FILE_PATH), f"O arquivo {EXISTING_FILE_PATH} não foi encontrado!"

    # Teste de Extração
    data = extract_csv(EXISTING_FILE_PATH)
    assert len(data) > 0, "Os dados extraídos estão vazios!"
    assert isinstance(data, list), "A extração não retornou uma lista de dados."
    assert "id" in data[0], "Os dados extraídos não contêm o campo 'id'."
