# Atividade 3 — Processamento de Linguagem Natural

Resolução das questões 1 a 3 da terceira lista de exercícios. As questões 4 (redes LSTM e Conv1D) e 5 (spaCy) não fazem parte desta entrega. Os resultados da execução estão salvos no notebook.

## Arquivos

- [lista3.pdf](lista3.pdf): enunciado da atividade.
- [atividade_3_agrupamento_busca.ipynb](atividade_3_agrupamento_busca.ipynb): notebook com as três questões.
- [dados/Tweets.csv](dados/Tweets.csv): mesma base de 14.640 tweets das Atividades 1 e 2.
- [dados/README.md](dados/README.md): identificação da fonte da base.
- [resultados](resultados): curvas de silhueta e grupos (questão 1), projeções t-SNE e confiabilidade por perplexidade (questão 2), palavras e documentos recuperados (questão 3).
- [requirements.txt](requirements.txt): versões das bibliotecas utilizadas na execução local.

## Executar no Google Colab

1. Abra o notebook no Google Colab, pela opção de abrir um arquivo do GitHub ou enviando o arquivo `.ipynb`.
2. Execute as células em ordem. Se o arquivo `Tweets.csv` não for carregado automaticamente, envie-o quando a célula de carregamento solicitar.
3. Na Questão 3, o modelo word2vec (~1,6 GB) é baixado para a pasta `modelos` na primeira execução. Essa etapa precisa de acesso à internet.

Os arquivos gerados ficam em `resultados` no ambiente onde o notebook for executado. No Colab, podem ser baixados pelo painel de arquivos.

## Executar localmente

Em um ambiente Python com Jupyter disponível, instale as dependências:

```sh
python -m pip install -r atividade_3/requirements.txt
```

Abra o notebook com a pasta de trabalho definida como `atividade_3`. A execução completa leva cerca de 15 minutos (16 núcleos), a maior parte nos t-SNE, e a Questão 3 usa cerca de 1 GB de memória. A pasta `modelos` é ignorada pelo Git.

## Conteúdo

1. Agrupamento: k-means com k de 2 a 30, usando o coeficiente de silhueta médio (distância do cosseno) sobre (a) TF-IDF e (b) o espaço latente do NMF, com os gráficos de k contra silhueta média.
2. Projeção multidimensional: t-SNE do TF-IDF colorido pelos grupos da 1a, variação da perplexidade (5, 30, 100 e 300), e escolha da perplexidade pela confiabilidade (`trustworthiness`) para o TF-IDF e para o NMF, com as melhores projeções lado a lado.
3. Buscadores com word2vec: 5 palavras de consulta ausentes dos textos, as 3 palavras mais parecidas da base com seus documentos, e a busca de documentos pela média das 5 menores distâncias (DM5).

## Critérios e limitações

**Base:** pré-processamento da Questão 5 da Atividade 1 (o mesmo da Atividade 2). Nenhum tweet fica vazio. A Questão 3 acrescenta stopwords (lista em inglês do scikit-learn) e o filtro pelo vocabulário do modelo.

**Método de tópicos:** o enunciado cita a "questão 5 da lista anterior", mas a modelagem de tópicos é a Questão 3 da lista 2. Usamos o NMF com 8 tópicos dessa questão, refeito no notebook com os mesmos hiperparâmetros.

**Questão 1:** o k-means e a silhueta usam a distância do cosseno (vetores normalizados). A silhueta é exata, calculada com a soma dos vetores de cada grupo em vez da matriz de distâncias, e foi conferida contra o scikit-learn. O melhor k do TF-IDF (29) fica na borda do intervalo testado e a curva é quase plana (silhueta ≈ 0,02), então não indica agrupamento real. No NMF o pico em k = 8 (0,483) é nítido, mas o valor não é comparável ao do TF-IDF.

**Questão 2:** o t-SNE do TF-IDF é aplicado após redução a 50 dimensões com SVD truncado (17,5% da variância), pois o t-SNE sobre a matriz esparsa completa é impraticável. A perplexidade foi escolhida pela confiabilidade em uma subamostra de 5.000 documentos (TF-IDF: 200, na borda da grade; NMF: 30); a confiabilidade não é comparável entre os dois métodos.

**Questão 3:** o modelo é o `word2vec-google-news-300` (inglês, notícias), limitado às 500 mil palavras mais frequentes. O gensim não instala no Python 3.14 usado aqui, então o arquivo binário é lido diretamente com NumPy. O vocabulário distingue maiúsculas, e como os textos estão em minúsculas só entram palavras cuja forma minúscula existe no modelo: 58,3% das palavras distintas da base têm vetor e 84 tweets ficam sem palavras. As palavras de consulta (`jetliner`, `hijacking`, `parachute`, `helicopter`, `aviator`) foram escolhidas entre candidatas ligadas ao tema e verificadas como ausentes dos textos; várias candidatas comuns (`airplane`, `cockpit`, `runway`) aparecem nos tweets e foram descartadas. O DM5 favorece documentos curtos, pois com menos de cinco palavras a média usa todas.

A base de tweets e os resultados da atividade estão incluídos no repositório. O modelo word2vec não está.
