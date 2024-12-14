from processo_temporal import carregar_dados, dia_com_mais_tweets, contar_tweets_por_periodo
from analise_sentimento import (
    open_file,
    filtro_tweet,
    porcentage_sentimento,
    positive_tweet,
    contador_sentiment,
)
import os


def main():
    # Caminho relativo para o arquivo de dados
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório atual
    file_path = os.path.join(base_dir, "dados", "Tweets.csv")  # Caminho para o CSV com base na estrutura

    # **Carregar os dados do CSV** - primeira etapa
    print("Carregando os dados do arquivo...")
    dados = carregar_dados()
    print(f"Dados carregados com sucesso! Total de tweets: {len(dados)}\n")

    # ---------------------- Análise Temporal ----------------------------
    print("Identificando o dia com mais tweets...")
    dia_mais_tweets, total_tweets = dia_com_mais_tweets(dados)
    print(f"Dia com mais tweets: {dia_mais_tweets}, com {total_tweets} tweets.\n")

    # Contando os tweets por período (ano/mes)
    ano = 2015
    print(f"Contando tweets para o ano de {ano}...")
    total_tweets_ano = contar_tweets_por_periodo(dados, ano=ano)
    print(f"Total de tweets em {ano}: {total_tweets_ano}\n")

    mes = 2  # Fevereiro
    print(f"Contando tweets para {ano}-{mes:02d}...")
    total_tweets_mes = contar_tweets_por_periodo(dados, ano=ano, mes=mes)
    print(f"Total de tweets em {ano}-{mes:02d}: {total_tweets_mes}\n")

    # ---------------------- Análise de Sentimentos ----------------------------
    print("\nAbrindo e processando análises de sentimentos...")
    data = open_file(file_path)

    # Filtrando os dados de uma companhia específica
    companhia_especifica = "Delta"
    print(f"\nFiltrando tweets da companhia: {companhia_especifica}")
    tweets_delta = filtro_tweet(data, companhia_especifica)
    print(f"Total de tweets da {companhia_especifica}: {len(tweets_delta)}")
    print(f"Exemplo de tweets: {tweets_delta[:3]}\n")  # Exibindo os 3 primeiros tweets da companhia Delta

    # Calculando a porcentagem de sentimentos por companhia
    print("\nCalculando porcentagens de sentimentos por companhia...")
    percentagens = porcentage_sentimento(data)
    for companhia, sentimentos in percentagens.items():
        print(f"{companhia}: {sentimentos}")

    # Identificando a companhia com mais tweets positivos
    print("\nIdentificando a companhia com mais tweets positivos...")
    companhia_mais_positiva = positive_tweet(data)
    print(f"Companhia com mais tweets positivos: {companhia_mais_positiva}")

    # Contando os sentimentos gerais em todos os dados
    print("\nContando os sentimentos gerais em todos os tweets...")
    sentimentos = contador_sentiment(data)
    print(f"Contagem de sentimentos: {sentimentos}")


if __name__ == "__main__":
    main()


