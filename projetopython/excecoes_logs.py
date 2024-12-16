import logging
import csv
from collections import Counter, defaultdict
from datetime import datetime


# Configuração do logging
logging.basicConfig(
    filename='excecoes_log.py',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def filtro_tweet(data, companhia):
    """
    Filtra tweets para uma companhia específica.
    Args:
        data (list[dict]): Lista de dados carregados.
        companhia (str): Nome da companhia para filtrar.
    Returns:
        list[dict]: Lista filtrada com tweets da companhia.
    """
    try:
        logging.info(f"Filtrando tweets para a companhia: {companhia}")
        return [row for row in data if row.get('airline') == companhia]
    except Exception as e:
        logging.error(f"Erro ao filtrar tweets para a companhia {companhia}: {e}")
        raise


def porcentage_sentimento(data):
    """
    Calcula a porcentagem de sentimentos por companhia.
    Args:
        data (list[dict]): Lista com dados de tweets.
    Returns:
        dict: Porcentagem de sentimentos por companhia.
    """
    try:
        logging.info("Calculando porcentagem de sentimentos por companhia")
        companhia_sentimentos = defaultdict(lambda: Counter())

        # Contagem de sentimentos por companhia
        for row in data:
            companhia = row.get('airline', '')
            sentimento = row.get('airline_sentiment', '')
            companhia_sentimentos[companhia][sentimento] += 1

        # Cálculo das porcentagens
        percentagens = {}
        for companhia, contagens in companhia_sentimentos.items():
            total = sum(contagens.values())
            if total > 0:
                percentagens[companhia] = {
                    sentimento: (count / total) * 100 for sentimento, count in contagens.items()
                }

        return percentagens
    except Exception as e:
        logging.error(f"Erro ao calcular porcentagem de sentimentos: {e}")
        raise


def positive_tweet(data):
    """
    Identifica a companhia com o maior número de tweets positivos.
    Args:
        data (list[dict]): Lista de dados de tweets.
    Returns:
        str: Nome da companhia com mais tweets positivos.
    """
    try:
        logging.info("Identificando companhia com mais tweets positivos")
        companhia_positivos = Counter(
            row.get('airline', '') for row in data if row.get('airline_sentiment') == 'positive'
        )
        return companhia_positivos.most_common(1)[0][0] if companhia_positivos else None
    except Exception as e:
        logging.error(f"Erro ao identificar companhia com mais tweets positivos: {e}")
        raise


def contador_sentiment(data):
    """
    Conta a frequência de sentimentos nos dados.
    Args:
        data (list[dict]): Lista com dados de tweets.
    Returns:
        collections.Counter: Contagem dos sentimentos.
    """
    try:
        logging.info("Contando sentimentos dos tweets")
        return Counter(row.get('airline_sentiment', '') for row in data)
    except Exception as e:
        logging.error(f"Erro ao contar sentimentos: {e}")
        raise


def ler_dados():
    """
    Lê dados de um arquivo CSV sem pandas.
    Retorna:
        list[dict]: Dados carregados do CSV.
    """
    try:
        logging.info("Lendo dados do arquivo CSV")
        with open("caminho/para/seu/arquivo.csv", "r") as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            dados = []
            for row in leitor:
                # Converte datas manualmente se necessário
                if 'tweet_created' in row and row['tweet_created']:
                    try:
                        row['tweet_created'] = datetime.strptime(row['tweet_created'], "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        row['tweet_created'] = None
                dados.append(row)
        logging.info("Dados lidos com sucesso")
        return dados
    except FileNotFoundError as e:
        logging.error(f"Erro: Arquivo não encontrado: {e}")
        raise
    except Exception as e:
        logging.error(f"Erro inesperado ao carregar os dados: {e}")
        raise


def dia_com_mais_tweets(dados):
    """
    Identifica o dia com mais tweets no conjunto de dados.
    Args:
        dados (list[dict]): Lista com dados carregados.
    Returns:
        tuple: O dia com mais tweets e o total.
    """
    try:
        logging.info("Identificando o dia com mais tweets")
        contagem_dias = Counter(
            row['tweet_created'].date() for row in dados if row.get('tweet_created')
        )
        dia_mais_tweets = contagem_dias.most_common(1)[0] if contagem_dias else (None, 0)
        logging.info(f"Dia com mais tweets: {dia_mais_tweets[0]}, Total: {dia_mais_tweets[1]}")
        return dia_mais_tweets
    except Exception as e:
        logging.error(f"Erro ao identificar o dia com mais tweets: {e}")
        raise


def contar_tweets_por_periodo(dados, ano, mes=None):
    """
    Conta tweets em um período específico.
    Args:
        dados (list[dict]): Lista com dados carregados.
        ano (int): Ano para filtro.
        mes (int, opcional): Mês para filtro.
    Returns:
        int: Total de tweets no período.
    """
    try:
        logging.info(f"Contando tweets para o ano {ano}, mês {mes}")
        if mes:
            filtro = [
                row for row in dados
                if row.get('tweet_created') and row['tweet_created'].year == ano and row['tweet_created'].month == mes
            ]
        else:
            filtro = [
                row for row in dados
                if row.get('tweet_created') and row['tweet_created'].year == ano
            ]
        total_tweets = len(filtro)
        logging.info(f"Total de tweets no período: {total_tweets}")
        return total_tweets
    except Exception as e:
        logging.error(f"Erro ao contar tweets por período: {e}")
        raise

