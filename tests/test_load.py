import pytest
import os
from etl.load import load_data_to_csv

OUTPUT_FILE_PATH = "../data_source/dados_gerados_teste.csv"
LISTA_VAZIA = []

class TestsLoad:

    def test_load_csv_sem_dados(self):
        with pytest.raises(ValueError):
            load_data_to_csv(LISTA_VAZIA, OUTPUT_FILE_PATH)

    def test_load_data_to_csv(self):

        transformed_data = [
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ]

        load_data_to_csv(transformed_data, OUTPUT_FILE_PATH)

        assert os.path.exists(OUTPUT_FILE_PATH), f"O arquivo {OUTPUT_FILE_PATH} não foi criado!"

        if os.path.exists(OUTPUT_FILE_PATH):
            os.remove(OUTPUT_FILE_PATH)
