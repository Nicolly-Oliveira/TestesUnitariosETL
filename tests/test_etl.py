import pytest
import os
from etl.etl import run_etl

EXISTING_FILE_PATH = "../data_source/dados_originais.csv"
OUTPUT_FILE_PATH = "../data_source/dados_finais.csv"


def test_etl_process():

    assert os.path.exists(EXISTING_FILE_PATH), f"O arquivo {EXISTING_FILE_PATH} não foi encontrado!"

    run_etl(EXISTING_FILE_PATH, OUTPUT_FILE_PATH)

    assert os.path.exists(OUTPUT_FILE_PATH), f"O arquivo {OUTPUT_FILE_PATH} não foi criado!"

    if os.path.exists(OUTPUT_FILE_PATH):
        os.remove(OUTPUT_FILE_PATH)

