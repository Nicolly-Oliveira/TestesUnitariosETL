import pytest
from etl.extract import extract_csv

EXISTING_FILE_PATH = "../data_source/dados_originais.csv"
NO_EXISTING_FILE_PATH = "../data_source/dados_fake.csv"

class TestsExtract:

    def test_extract_csv_diretorio_invalido(self):
        with pytest.raises(FileNotFoundError):
            extract_csv(NO_EXISTING_FILE_PATH)

    def test_extract_csv_sucesso(self):
        data = extract_csv(EXISTING_FILE_PATH)
        assert len(data) > 0

    def test_extract_csv_como_lista(self):
        data = extract_csv(EXISTING_FILE_PATH)
        assert isinstance(data, list)

    def test_extract_csv_campos_obrigatorios(self):
        data = extract_csv(EXISTING_FILE_PATH)
        assert "id" in data[0]
        assert "nome" in data[1]
        assert "data_nascimento" in data[2]
        assert "idade" in data[3]
        assert "cidade" in data[4]
