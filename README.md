  

Este pacote permite realizar análises de sentimentos, processar dados de tweets, identificar padrões temporais, analisar sentimentos associados a companhias aéreas e fornecer insights como percentuais
de sentimentos, o maior número de tweets positivos e análises baseadas em dados temporais.

Funcionalidades  

1: Leitura de Dados**  
- Leitura de um arquivo CSV com dados de tweets.  
- Estruturação e tratamento adequado dos dados carregados.  

2: Análise de Sentimento**  
Funções para:  
- Contar o número total de tweets por sentimento (**positivo**, **negativo**, **neutro**).  
- Calcular a percentagem de cada tipo de sentimento para cada companhia aérea.  
- Identificar a companhia aérea com o maior número de tweets positivos.  
- Analisar o número médio de retweets por tipo de sentimento.

---

3: Análise de Companhias Aéreas**  
Funções para:  
- Listar todas as companhias aéreas mencionadas no dataset.  
- Identificar a companhia com mais tweets negativos.  
- Calcular o número total de tweets por companhia aérea.  
- Filtrar tweets de uma companhia aérea específica para análise detalhada.

---

4: Processamento Temporal**  
Funções para análise de padrões temporais:  
- Identificar o dia com maior número de tweets.  
- Contar quantos tweets foram postados em um determinado mes ou ano.

---

5:  Exceções e Logs**  
- O sistema captura erros na leitura do arquivo.  
- Registra eventos importantes no processo de execução, como início da leitura do CSV, erros e conclusão da análise no **log.txt**.


