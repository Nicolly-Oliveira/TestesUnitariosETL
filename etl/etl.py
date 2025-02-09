from etl.extract import extract_csv
from etl.transform import transform_data, remover_espacos_vazios, ajustar_data_nascimento, calcular_idade, \
    preencher_idade
from etl.load import load_data_to_csv

def run_etl(input_file_path, output_file_path, required_columns=None, transformations=None):
    """
    Função que executa o processo completo de ETL (Extração, Transformação, Validação e Carga).
    """
    # Passo 1: Extração
    print(f"Extraindo dados de {input_file_path}...")
    try:
        data = extract_csv(input_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {input_file_path} não foi encontrado.")

    if not data:
        raise ValueError(f"Nenhum dado encontrado no arquivo {input_file_path}")

    # Passo 2: Transformação
    print(f"Transformando dados extraídos...")

    # Se nenhuma transformação for fornecida, usa-se o padrão
    if not transformations:
        transformations = [
            remover_espacos_vazios,
            ajustar_data_nascimento,
            preencher_idade  # Preenche idade caso esteja vazio
        ]

    data = transform_data(data, transformations)

    # Passo 3: Validação
    print(f"Validando dados...")

    # Passo 4: Carga
    print(f"Carregando dados transformados para {output_file_path}...")
    try:
        load_data_to_csv(data, output_file_path)
    except Exception as e:
        raise ValueError(f"Erro ao salvar os dados no arquivo {output_file_path}: {e}")

    print(f"ETL concluído com sucesso. Dados carregados em {output_file_path}")
