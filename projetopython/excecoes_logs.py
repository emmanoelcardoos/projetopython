import logging
import pandas as pd
from collections import Counter, defaultdict
from typing import List, Dict
import importlib.resources as resources

logging.basicConfig(
    filename='excecoes_log.py',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def filtro_tweet(data: List[Dict[str, str]], companhia: str) -> List[Dict[str, str]]:
    try:
        logging.info(f"Filtrando tweets para a companhia: {companhia}")
        return [row for row in data if row['airline'] == companhia]
    except Exception as e:
        logging.error(f"Erro ao filtrar tweets para a companhia {companhia}: {e}")
        raise

def porcentage_sentimento(data: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    try:
        logging.info("Calculando porcentagem de sentimentos por companhia")
        companhia_sentimentos = defaultdict(lambda: Counter())
        for row in data:
            companhia = row['airline']
            sentimento = row['airline_sentiment']
            companhia_sentimentos[companhia][sentimento] += 1

        percentagens = {}
        for companhia, contagens in companhia_sentimentos.items():
            total = sum(contagens.values())
            percentagens[companhia] = {
                sentimento: (count / total) * 100 for sentimento, count in contagens.items()
            }

        return percentagens
    except Exception as e:
        logging.error(f"Erro ao calcular porcentagem de sentimentos: {e}")
        raise

def positive_tweet(data: List[Dict[str, str]]) -> str:
    try:
        logging.info("Identificando companhia com mais tweets positivos")
        companhia_positivos = Counter(
            row['airline'] for row in data if row['airline_sentiment'] == 'positive'
        )
        return companhia_positivos.most_common(1)[0][0]
    except Exception as e:
        logging.error(f"Erro ao identificar companhia com mais tweets positivos: {e}")
        raise

def contador_sentiment(data: List[Dict[str, str]]) -> Counter:
    try:
        logging.info("Contando sentimentos dos tweets")
        return Counter(row['airline_sentiment'] for row in data)
    except Exception as e:
        logging.error(f"Erro ao contar sentimentos: {e}")
        raise

def ler_dados():
    try:
        logging.info("Lendo dados do arquivo CSV")
        with resources.open_text("projetopython.dados", "tweets.csv") as arquivo_csv:
            dados = pd.read_csv(arquivo_csv)
        logging.info("Dados lidos com sucesso")
        return dados
    except FileNotFoundError as e:
        logging.error(f"Arquivo não encontrado: {e}")
        raise
    except pd.errors.ParserError as e:
        logging.error(f"Erro ao analisar o arquivo CSV: {e}")
        raise
    except Exception as e:
        logging.error(f"Erro inesperado ao ler os dados: {e}")
        raise

def carregar_dados():
    try:
        logging.info("Carregando e processando os dados")
        with resources.open_text("projetopython.dados", "tweets.csv") as arquivo_csv:
            dados = pd.read_csv(arquivo_csv)
        dados['tweet_created'] = pd.to_datetime(dados['tweet_created'])
        logging.info("Dados carregados e processados com sucesso")
        return dados
    except FileNotFoundError as e:
        logging.error(f"Arquivo não encontrado: {e}")
        raise
    except pd.errors.ParserError as e:
        logging.error(f"Erro ao processar o arquivo CSV: {e}")
        raise
    except Exception as e:
        logging.error(f"Erro inesperado ao carregar os dados: {e}")
        raise

def dia_com_mais_tweets():
    try:
        logging.info("Identificando o dia com mais tweets")
        dados = carregar_dados()
        tweets_por_dia = dados['tweet_created'].dt.date.value_counts()
        dia_mais_tweets = tweets_por_dia.idxmax()
        total_tweets = tweets_por_dia.max()
        logging.info(f"Dia com mais tweets: {dia_mais_tweets}, Total: {total_tweets}")
        return dia_mais_tweets, total_tweets
    except Exception as e:
        logging.error(f"Erro ao identificar o dia com mais tweets: {e}")
        raise

def contar_tweets_por_periodo(ano=None, mes=None):
    try:
        if not ano:
            raise ValueError("Ano não especificado")
        logging.info(f"Contando tweets para o ano: {ano}, mês: {mes}")
        dados = carregar_dados()
        if mes:
            filtro = (dados['tweet_created'].dt.year == ano) & (dados['tweet_created'].dt.month == mes)
        else:
            filtro = dados['tweet_created'].dt.year == ano
        total_tweets = dados[filtro].shape[0]
        logging.info(f"Total de tweets no período: {total_tweets}")
        return total_tweets
    except ValueError as e:
        logging.error(f"Erro de valor: {e}")
        raise
    except Exception as e:
        logging.error(f"Erro ao contar tweets por período: {e}")
        raise
