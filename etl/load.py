# my_etl/load.py
import csv

def load_data_to_csv(data, output_file_path):
    """
    Função para carregar os dados transformados em um novo arquivo CSV.
    """
    if not data:
        raise ValueError("Nenhum dado para carregar no arquivo.")

    # Obter as chaves do primeiro item para usá-las como cabeçalhos do CSV
    headers = data[0].keys()

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
