from etl.etl import run_etl

input_file_path = "data_source/dados_originais.csv"
output_file_path = "data_source/dados_finais.csv"

if __name__ == "__main__":
    run_etl(input_file_path, output_file_path)

