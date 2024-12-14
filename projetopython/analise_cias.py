def filtro_tweet(data: List[Dict[str, str]], companhia: str) -> List[Dict[str, str]]:
   
    return [row for row in data if row['airline'] == companhia]

def porcentage_sentimento(data: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    
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
    
def positive_tweet(data: List[Dict[str, str]]) -> str:
    
    companhia_positivos = Counter(
        row['airline'] for row in data if row['airline_sentiment'] == 'positive'
    )
    return companhia_positivos.most_common(1)[0][0]
    

def contador_sentiment(data: List[Dict[str, str]]) -> Counter:
    
     sent_count= Counter(row['airline_sentiment'] for row in data)
    return sent_count
