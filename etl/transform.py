from datetime import datetime

def transform_data(data, transformations=None):
    """
    Função para transformar os dados de acordo com uma lista de funções de transformação.
    """
    if not transformations:
        transformations = []

    for transformation in transformations:
        data = [transformation(row) for row in data]
    return data


def remover_espacos_vazios(row):
    """
    Remove espaços extras de todas as strings no row.
    """
    return {key: value.strip() if isinstance(value, str) else value for key, value in row.items()}


# Função para ajustar o formato da data de nascimento para dd/mm/aaaa
def ajustar_data_nascimento(row):
    """
    Ajusta a data de nascimento no formato dd/mm/aaaa.
    """
    data_nascimento = row.get("data_nascimento", "")
    formatos = ['%d-%m-%Y', '%Y/%m/%d', '%Y-%m-%d', '%m/%d/%Y', '%d.%m.%Y', '%Y.%m.%d']

    if data_nascimento:
        for formato in formatos:
            try:
                nascimento = datetime.strptime(data_nascimento, formato)

                # Se o formato for '%m/%d/%Y', há a possibilidade de inversão de mês e dia.
                # Verifique se o mês é maior que 12, o que indicaria uma confusão entre dia e mês.
                if formato == '%m/%d/%Y':
                    if nascimento.month > 12:
                        nascimento = nascimento.replace(day=nascimento.month, month=nascimento.day)

                # Garantir que a data final está no formato correto (dd/mm/yyyy)
                row["data_nascimento"] = nascimento.strftime('%d/%m/%Y')
                break
            except ValueError:
                continue

    return row


def calcular_idade(data_nascimento):
    """
    Calcula a idade com base na data de nascimento em vários formatos.
    """
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
            continue  # Se o formato falhar, tenta o próximo

    # Se nenhum formato funcionar, retorna None ou alguma outra indicação de erro
    return None


def preencher_idade(row):
    """
    Preenche o campo de idade com base na data de nascimento, caso o campo idade esteja vazio.
    """
    if row.get("idade") in [None, ""]:
        data_nascimento = row.get("data_nascimento")
        if data_nascimento:
            row["idade"] = calcular_idade(data_nascimento)
    return row