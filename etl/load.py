import csv

def load_data_to_csv(data, output_file_path):

    if not data:
        raise ValueError("Nenhum dado para carregar no arquivo.")

    headers = data[0].keys()

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
