import csv
import os

def extract_csv(file_path):
    """
    Função para extrair os dados de um arquivo CSV existente.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado!")

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

