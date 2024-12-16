import csv
import importlib.resources as resources
from datetime import datetime


def carregar_dados():
    """
    Carrega os dados do arquivo CSV e converte a coluna 'tweet_created' para o formato datetime.

    Returns:
        list: Lista de dicionários com os dados processados.
    """
    try:
        
        with resources.open_text("projetopython.dados", "tweets.csv") as arquivo_csv:
            dados = []
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                try:
                    
                    linha['tweet_created'] = datetime.strptime(linha['tweet_created'], "%Y-%m-%d %H:%M:%S")
                    dados.append(linha)
                except ValueError:
                    continue  
        print("Dados carregados com sucesso!")
        return dados
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None


def dia_com_mais_tweets():
    """
    Identifica o dia com o maior número de tweets.

    Returns:
        tuple: Dia com mais tweets (datetime.date) e o número total de tweets nesse dia.
    """
    dados = carregar_dados()
    if dados is None:
        raise ValueError("Não foi possível carregar os dados.")

    contagem_dias = {}
    for tweet in dados:
        data_tweet = tweet['tweet_created'].date()
        if data_tweet in contagem_dias:
            contagem_dias[data_tweet] += 1
        else:
            contagem_dias[data_tweet] = 1

    dia_mais_tweets = max(contagem_dias, key=contagem_dias.get)
    total_tweets = contagem_dias[dia_mais_tweets]

    print(f"Dia com mais tweets: {dia_mais_tweets}, Total de tweets: {total_tweets}")
    return dia_mais_tweets, total_tweets


def contar_tweets_por_periodo(ano=None, mes=None):
    """
    Conta o número de tweets feitos em um determinado ano ou mês.

    Args:
        ano (int, opcional): Ano a ser filtrado.
        mes (int, opcional): Mês a ser filtrado.

    Returns:
        int: Número de tweets no período especificado.

    Raises:
        ValueError: Se o ano não for fornecido.
    """
    if not ano:
        raise ValueError("Por favor, forneça pelo menos o ano.")  

    dados = carregar_dados()
    if dados is None:
        raise ValueError("Não foi possível carregar os dados.")

    total_tweets = 0
    for tweet in dados:
        if tweet['tweet_created'].year == ano:
            if mes:
                if tweet['tweet_created'].month == mes:
                    total_tweets += 1
            else:
                total_tweets += 1

    print(f"Total de tweets no período: {total_tweets}")
    return total_tweets

  


