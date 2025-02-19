from datetime import datetime

def transform_data(data, transformations=None):
    if not transformations:
        transformations = []

    for transformation in transformations:
        data = [transformation(row) for row in data]
    return data


def remover_espacos_vazios(row):

    return {key: value.strip() if isinstance(value, str) else value for key, value in row.items()}


def ajustar_data_nascimento(row):

    data_nascimento = row.get("data_nascimento", "")
    formatos = ['%d-%m-%Y', '%Y/%m/%d', '%Y-%m-%d', '%m/%d/%Y', '%d.%m.%Y', '%Y.%m.%d']

    if data_nascimento:

        if not isinstance(data_nascimento, str):
            data_nascimento = str(data_nascimento)

        for formato in formatos:
            try:
                nascimento = datetime.strptime(data_nascimento, formato)

                if formato == '%m/%d/%Y':
                    if nascimento.month > 12:
                        nascimento = nascimento.replace(day=nascimento.month, month=nascimento.day)

                row["data_nascimento"] = nascimento.strftime('%d/%m/%Y')
                break

            except ValueError:
                continue

    return row

def calcular_idade(data_nascimento):

    formatos = ['%d/%m/%Y', '%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%d.%m.%Y', '%Y.%m.%d']

    for formato in formatos:
        try:
            nascimento = datetime.strptime(data_nascimento, formato)
            hoje = datetime.today()
            idade = hoje.year - nascimento.year
            if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
                idade -= 1
            return idade
        except ValueError:
            continue

    return None


def preencher_idade(row):

    if row.get("idade") in [None, ""]:
        data_nascimento = row.get("data_nascimento")
        if data_nascimento:
            row["idade"] = calcular_idade(data_nascimento)
    return row