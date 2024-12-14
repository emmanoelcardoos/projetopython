import pandas as pd
import importlib.resources as resources


def carregar_dados():
    """
    Carrega os dados do arquivo CSV e converte a coluna 'tweet_created' para o formato datetime.

    Returns:
        DataFrame: DataFrame com os dados processados.
    """
    try:
        # Carregar o arquivo de dados da subpasta 'dados' dentro da estrutura do pacote
        with resources.open_text("projetopython.dados", "tweets.csv") as arquivo_csv:
            dados = pd.read_csv(arquivo_csv)
        
        # Converter a coluna 'tweet_created' para datetime de forma a ficar mais facl de ler
        dados['tweet_created'] = pd.to_datetime(dados['tweet_created'])
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
    
   
    tweets_por_dia = dados['tweet_created'].dt.date.value_counts()
    
    
    dia_mais_tweets = tweets_por_dia.idxmax()
    total_tweets = tweets_por_dia.max()
    
    print(f"Dia com mais tweets: {dia_mais_tweets}, Total de tweets: {total_tweets}")
    return dia_mais_tweets, total_tweets


def contar_tweets_por_periodo(ano=None, mes=None):
    """
    Conta o número de tweets feitos em um determinado ano ou mês.

    Args:
        ano (int, opcional): Ano a ser filtrado. Obrigatório.
        mes (int, opcional): Mês a ser filtrado. Opcional.

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

    
    if mes:
        filtro = (dados['tweet_created'].dt.year == ano) & (dados['tweet_created'].dt.month == mes)
    else:
        filtro = dados['tweet_created'].dt.year == ano

    total_tweets = dados[filtro].shape[0]
    print(f"Total de tweets no período: {total_tweets}")
    return total_tweets
  


