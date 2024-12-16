import logging
import csv
from collections import Counter


logging.basicConfig(
    filename='login.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def realizar_login(user, password):
    if user == "main" and password == "123456":
        logging.info(f"Login bem-sucedido para o utilizador: {user}")
        return True
    else:
        logging.info(f"Tentativa de login falhou para o utilizador: {user}")
        return False


def carregar_dados():
    try:
        with open("caminho/para/seu/arquivo.csv", "r") as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            dados = [linha for linha in leitor]
            for tweet in dados:
                tweet['airline_sentiment'] = tweet.get('airline_sentiment', '')
                tweet['airline'] = tweet.get('airline', '')
            return dados
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        return []


def companhia_com_mais_tweets_negativos(dados):
    negativos = [tweet['airline'] for tweet in dados if tweet['airline_sentiment'] == 'negative']
    contagem = Counter(negativos)
    if contagem:
        return contagem.most_common(1)[0][0]
    else:
        return None


def filtrar_tweets_por_companhia(dados, companhia):
    return [tweet for tweet in dados if tweet['airline'] == companhia]


def listar_companhias(dados):
    companhias = {tweet['airline'] for tweet in dados}
    return list(companhias)


def total_tweets_por_companhia(dados):
    contagem = Counter(tweet['airline'] for tweet in dados)
    return contagem





