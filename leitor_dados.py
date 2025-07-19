import pandas as pd

def ler_dados_csv(caminho_arquivo = 'datatable.csv'):
    try:
        df = pd.read_csv(caminho_arquivo)
        return df
    except FileNotFoundError as e:
        print(f"{e}: Arquivo {caminho_arquivo} não encontrado.")
        return None