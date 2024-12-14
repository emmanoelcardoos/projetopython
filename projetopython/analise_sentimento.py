import logging
import pandas as pd

logging.basicConfig(filename='login.log',level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",datefmt="%Y-%m-%d %H:%M:%S")
def realizar_login(user, password):
    if user == "main" and password == "123456":
        logging.info(f"Login bem-sucedido para o utilizador: {user}")
        return True
    else:
        logging.info(f"Tentativa de login falhou para o utilizador: {user}")
        return False
def companhia_com_mais_tweets_negativos(df):
    negativos = df[df['airline_sentiment'] == 'negative']
    return negativos['airline'].value_counts().idxmax()
    
def filtrar_tweets_por_companhia(df, companhia):
    return df[df['airline'] == companhia]
    
def listar_companhias(df):
    return df['airline'].unique()
    
def total_tweets_por_companhia(df):
    """Calcula o número total de tweets por companhia."""
    return df['airline'].value_counts()




