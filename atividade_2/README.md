# Atividade 2 — Processamento de Linguagem Natural

Resolução da segunda lista de exercícios, com três questões. Os resultados da execução estão salvos no notebook.

## Arquivos

- [lista2.pdf](lista2.pdf): enunciado da atividade.
- [atividade_2_topicos.ipynb](atividade_2_topicos.ipynb): notebook com as três questões.
- [dados/Tweets.csv](dados/Tweets.csv): mesma base de 14.640 tweets da Atividade 1.
- [dados/README.md](dados/README.md): identificação da fonte da base.
- [resultados](resultados): tabelas de similaridade, métricas e matrizes de confusão da classificação, e tópicos das questões 1, 2 e 3.
- [requirements.txt](requirements.txt): versões das bibliotecas utilizadas na execução local.

## Executar no Google Colab

1. Abra o notebook no Google Colab, pela opção de abrir um arquivo do GitHub ou enviando o arquivo `.ipynb`.
2. No início da sessão, instale as dependências que não vêm pré-instaladas no Colab:
   ```sh
   !pip install scikit-learn bertopic sentence-transformers umap-learn hdbscan
   ```
3. Execute as células em ordem. Se o arquivo `Tweets.csv` não for carregado automaticamente, envie-o quando solicitado na célula de carregamento da base (o notebook do GitHub não carrega os demais arquivos do repositório no ambiente do Colab).

Os arquivos gerados ficam em `resultados` no ambiente onde o notebook for executado. No Colab, podem ser baixados pelo painel de arquivos.

## Executar localmente

Em um ambiente Python com Jupyter disponível, instale as dependências:

```sh
python -m pip install -r atividade_2/requirements.txt
```

Abra o notebook com a pasta de trabalho definida como `atividade_2`, para que os caminhos relativos de dados e resultados sejam encontrados.

## Conteúdo

1. Similaridade entre documentos: para 5 tweets escolhidos aleatoriamente, o documento mais parecido na base, usando CountVectorizer e TF-IDF com similaridade do cosseno, com justificativa por par.
2. Classificação de texto: sentimento do tweet (positivo/neutro/negativo) com Regressão Logística, Naive Bayes e SVM linear, sobre representações CountVectorizer e TF-IDF, com matrizes de confusão, métricas micro/macro e validação cruzada.
3. Modelagem de tópicos: comparação entre NMF (sobre a matriz TF-IDF) e BERTopic, com 8 tópicos em cada método, palavras mais relevantes por tópico e tópico mais relevante de 5 documentos.

## Critérios e limitações

**Base:** as três questões reaproveitam, sem alterações, a função de pré-processamento da Questão 5 da Atividade 1 (remoção de palavras com dígitos, minúsculas, remoção de pontuação, tokenização por espaços), aplicada a `Tweets.csv`. Não é aplicada a limpeza adicional da Questão 6 (stopwords, POS, stemização), pois a lista 2 pede apenas os textos pré-processados "como na primeira lista", entendido como o nível da Questão 5.

**Questão 1:** os 5 documentos de consulta são escolhidos por amostragem aleatória com semente fixa, não manualmente. A similaridade é calculada apenas entre os 5 documentos de consulta e o restante da base (fatia 5×N), evitando montar a matriz de similaridade completa entre todos os ~14,6 mil documentos.

**Questão 2:** o rótulo usado é `airline_sentiment`, com desbalanceamento relevante (negativo ≈ 62,7%, neutro ≈ 21,2%, positivo ≈ 16,1%), o que explica F1 macro sistematicamente menor que F1 micro nos resultados. O enunciado combina "validação cruzada" com uma divisão 70%/30% treino/teste; o notebook reporta as duas coisas separadamente: uma divisão estratificada única (para as matrizes de confusão e métricas pontuais) e uma validação cruzada estratificada de 5 partições (para uma estimativa mais robusta). Optamos por Regressão Logística, Naive Bayes e SVM linear (via `LinearSVC`, mais escalável que `SVC(kernel='linear')`), em vez de k-NN e Random Forest, por serem mais adequados a vetores esparsos de alta dimensionalidade.

**Questão 3:** o método clássico escolhido foi o NMF, aplicado diretamente sobre a matriz TF-IDF; o número de tópicos (k = 8) foi escolhido por inspeção qualitativa, já que a curva de erro de reconstrução não apresenta um cotovelo nítido. O BERTopic usa sua configuração padrão (embeddings semânticos + UMAP + HDBSCAN + c-TF-IDF interno para extrair as palavras de cada tópico), diferente da matriz TF-IDF (scikit-learn) usada como entrada do NMF — essa distinção é discutida no notebook. A execução completa do BERTopic sobre os ~14,6 mil tweets levou cerca de 40 segundos em CPU, o que dispensou qualquer amostragem da base. Boa parte da separação de tópicos em ambos os métodos é orientada pelo nome da companhia aérea mencionada no tweet, um efeito esperado nesta base.

A base de tweets e os resultados da atividade estão incluídos no repositório.
