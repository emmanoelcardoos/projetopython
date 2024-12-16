import csv
import importlib.resources as resources


def ler_dados():
    """
    Lê o arquivo CSV da pasta de dados de forma relativa.
    :return: Dados lidos no formato de lista de dicionários.
    """
    try:
        # Acessando o arquivo CSV com base no pacote correto
        with resources.open_text("projetopython.dados", "tweets.csv") as arquivo_csv:
            dados = list(csv.DictReader(arquivo_csv))  # Lendo os dados como uma lista de dicionários
        print("Dados lidos com sucesso!")
        return dados
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None



