from etl.extract import extract_csv
from etl.transform import transform_data, remover_espacos_vazios, ajustar_data_nascimento, preencher_idade
from etl.load import load_data_to_csv

def run_etl(input_file_path, output_file_path, required_columns=None, transformations=None):

    print(f"Extraindo dados de {input_file_path}...")
    try:
        data = extract_csv(input_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {input_file_path} não foi encontrado.")

    if not data:
        raise ValueError(f"Nenhum dado encontrado no arquivo {input_file_path}")

    print(f"Transformando dados extraídos...")

    if not transformations:
        transformations = [
            remover_espacos_vazios,
            ajustar_data_nascimento,
            preencher_idade
        ]

    data = transform_data(data, transformations)

    print(f"Validando dados...")

    print(f"Carregando dados transformados para {output_file_path}...")
    try:
        load_data_to_csv(data, output_file_path)
    except Exception as e:
        raise ValueError(f"Erro ao salvar os dados no arquivo {output_file_path}: {e}")

    print(f"ETL concluído com sucesso. Dados carregados em {output_file_path}")
