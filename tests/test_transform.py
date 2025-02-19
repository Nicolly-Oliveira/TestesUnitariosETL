import pytest
from datetime import datetime
from etl.transform import transform_data, remover_espacos_vazios, ajustar_data_nascimento, calcular_idade, \
    preencher_idade

def test_transform_data():

    raw_data = [
        {"id": "1", "name": " Alice ", "data_nascimento": "10-05-1998", "idade": ""},
        {"id": "2", "name": "José", "data_nascimento": "20/03/1993", "idade": ""},
        {"id": "3", "name": "Bruna", "data_nascimento": "1995-08-15", "idade": "29"}
    ]

    transformations = [
        remover_espacos_vazios,
        ajustar_data_nascimento,
        preencher_idade
    ]
    transformed_data = transform_data(raw_data, transformations)

    assert len(transformed_data) == 3, "A quantidade de dados transformados está incorreta!"
    assert transformed_data[0]["name"] == "Alice", "A transformação do campo 'name' não foi aplicada corretamente."

    assert transformed_data[0]["data_nascimento"] == "10/05/1998", "A data de nascimento não foi ajustada corretamente."
    assert transformed_data[2]["data_nascimento"] == "15/08/1995", "A data de nascimento não foi ajustada corretamente."

    assert transformed_data[0]["idade"] == 26, "A idade não foi calculada corretamente."
    assert transformed_data[1]["idade"] == 31, "A idade não foi calculada corretamente."


def test_ajustar_data_nascimento():
    assert ajustar_data_nascimento({"data_nascimento": "10-05-1998"})["data_nascimento"] == "10/05/1998"
    assert ajustar_data_nascimento({"data_nascimento": "1993/03/20"})["data_nascimento"] == "20/03/1993"
    assert ajustar_data_nascimento({"data_nascimento": "1995-08-15"})["data_nascimento"] == "15/08/1995"
    assert ajustar_data_nascimento({"data_nascimento": "05/04/1986"})["data_nascimento"] == "05/04/1986"
    assert ajustar_data_nascimento({"data_nascimento": "1981.06.12"})["data_nascimento"] == "12/06/1981"


class TestCalcularIdade:

    def test_idade_com_formato_dd_mm_yyyy(self):
        data = "05/04/1988"
        idade = calcular_idade(data)
        assert idade == 36

    def test_idade_com_formato_yyyy_mm_dd(self):
        data = "1988-04-05"
        idade = calcular_idade(data)
        assert idade == 36

    def test_idade_com_formato_yyyy_mm_dd_com_barra(self):
        data = "1988/04/05"
        idade = calcular_idade(data)
        assert idade == 36

    def test_idade_com_formato_dd_mm_yyyy_com_traco(self):
        data = "05-04-1988"
        idade = calcular_idade(data)
        assert idade == 36

    def test_idade_com_formato_yyyy_mm_dd_com_ponto(self):
        data = "1988.04.05"
        idade = calcular_idade(data)
        assert idade == 36

    def test_idade_com_data_invalida(self):
        data = "31/02/1988"
        idade = calcular_idade(data)
        assert idade is None

    def test_idade_com_data_format_incorreto(self):
        data = "invalid_date"
        idade = calcular_idade(data)
        assert idade is None


def test_preencher_idade():
    row = {"name": "João", "data_nascimento": "10/05/1998", "idade": ""}
    result = preencher_idade(row)
    assert result["idade"] == 26

    row = {"name": "Maria", "data_nascimento": "15/08/1985", "idade": "38"}
    result = preencher_idade(row)
    assert not result["idade"] == "35"
