from etl.etl import run_etl

# Caminho dos arquivos de entrada e saída
input_file_path = "data_source/dados_originais.csv"
output_file_path = "data_source/dados_finais.csv"

# Execute o processo ETL
if __name__ == "__main__":
    run_etl(input_file_path, output_file_path)
