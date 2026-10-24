# Atividade 3 — Processamento de Linguagem Natural

Resolução das **cinco questões** da lista 3. O notebook reúne código, resultados, gráficos e análises, usando a mesma base de 14.640 tweets das Atividades 1 e 2.

## Arquivos

- [lista3.pdf](lista3.pdf): enunciado.
- [atividade_3_agrupamento_busca.ipynb](atividade_3_agrupamento_busca.ipynb): resolução das questões 1–5.
- [dados/Tweets.csv](dados/Tweets.csv): base de textos e rótulos de sentimento.
- [dados/README.md](dados/README.md): origem e uso dos dados.
- [requirements.txt](requirements.txt): versões das dependências da validação local.
- [executar_notebook.py](executar_notebook.py): execução integral em um kernel novo, com salvamento das saídas.
- [resultados](resultados): tabelas, figuras, predições e grafo exportados.
- [resultados/ambiente_execucao.json](resultados/ambiente_execucao.json): versões efetivamente usadas e parâmetros gerais da execução.

## Executar localmente

Use Python 3.10 de 64 bits. Em um ambiente virtual novo, na pasta `atividade_3`:

```sh
python -m pip install -r requirements.txt
python -m spacy download en_core_web_lg
python executar_notebook.py
```

O executor inicia um kernel com o mesmo interpretador Python usado no comando, executa as células em ordem e salva o notebook a cada célula concluída. Em caso de erro, salva a saída disponível e encerra com falha. Também é possível abrir o notebook em Jupyter ou no VS Code e escolher esse ambiente como kernel.

O modelo spaCy usado na validação é `en_core_web_lg` 3.8.0. Para instalar especificamente essa versão:

```sh
python -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.8.0/en_core_web_lg-3.8.0-py3-none-any.whl
```

Na primeira execução, a questão 3 baixa o modelo `word2vec-google-news-300` (~1,7 GB) para `modelos/`. Essa pasta é ignorada pelo Git. O arquivo temporário só recebe o nome definitivo após o download terminar. São carregadas as primeiras 500 mil entradas, com 300 dimensões. Reserve vários GB de memória para a execução integral; o tempo varia com a máquina, sobretudo nas projeções t-SNE e no treinamento das redes. O notebook limita o paralelismo padrão a quatro threads.

## Executar no Google Colab

1. Abra o `.ipynb` e selecione um ambiente Python.
2. Antes das células da atividade, instale as dependências compatíveis com o Python do Colab:

   ```python
   %pip install pandas numpy scipy matplotlib scikit-learn torch spacy networkx nbformat nbclient ipykernel
   ```

3. Se o Colab solicitar reinício após a instalação, reinicie antes de executar a atividade.
4. Execute as células em ordem e envie `Tweets.csv` quando solicitado. A questão 5 baixa o modelo spaCy automaticamente se necessário.
5. Baixe o notebook executado e a pasta `resultados` pelo painel de arquivos.

O Colab pode usar versões diferentes das fixadas localmente. A última célula registra o ambiente real; pequenas diferenças numéricas podem alterar agrupamentos e projeções. Não é necessário instalar gensim nem usar GPU.

## Conteúdo e resultados

| Questão | Itens | Conteúdo | Diretório |
|---|---|---|---|
| 1 | a, b | K-means, silhueta e escolha de k para TF-IDF e NMF | `resultados/questao_1` |
| 2 | a, b, c | t-SNE, variação de perplexidade e comparação das projeções | `resultados/questao_2` |
| 3 | a, b, c | Word2vec, palavras semelhantes e recuperação de documentos por DM5 | `resultados/questao_3` |
| 4 | a, b | Embedding + LSTM e Embedding + Conv1D, teste e validação cruzada | `resultados/questao_4` |
| 5 | a, b, c, d | POS, frequências, entidades GPE e grafo de coocorrência | `resultados/questao_5` |

A questão 3b inclui os textos completos de todos os documentos recuperados, em tabelas expansíveis no notebook e em `documentos_3b.html` e `documentos_3b.csv`. A questão 4 exporta métricas, predições, curvas de aprendizado e matrizes de confusão. A questão 5 exporta as etiquetas por token (CSV comprimido), entidades, frequências, todas as arestas e o grafo completo em GraphML; a figura mostra as 30 entidades mais frequentes.

## Critérios e limitações

**Base:** todas as questões partem do pré-processamento da questão 5 da Atividade 1: remoção de palavras com dígitos, minúsculas, remoção de pontuação e tokenização. A questão 3 também remove stopwords e palavras sem vetor. A questão 5 aplica spaCy ao texto pré-processado; a análise complementar compara o reconhecimento de entidades com o texto original na mesma amostra de 2.000 tweets.

**Questão 1:** usamos o NMF com oito tópicos da questão 3 da lista 2, interpretando a referência do enunciado à “questão 5 da lista anterior” como referência à modelagem de tópicos. O K-means otimiza distância euclidiana quadrática em vetores normalizados, enquanto a escolha de k usa silhueta com cosseno. Isso não equivale exatamente a K-means esférico, porque os centroides não são normalizados. A função de silhueta é conferida contra o scikit-learn, na base completa, com cálculo em blocos para limitar a memória.

**Questão 2:** o TF-IDF passa por SVD de 50 dimensões antes do t-SNE para reduzir o custo; portanto, a projeção é uma aproximação da representação original. A perplexidade é escolhida pela confiabilidade em uma subamostra fixa de 5.000 documentos. Nos itens a e b, as cores representam os grupos da 1a; no item c, ambas as projeções usam os grupos da 1b, conforme o enunciado. Métricas de confiabilidade de espaços diferentes não constituem comparação direta entre os métodos.

**Questão 3:** o word2vec de notícias em inglês distingue maiúsculas e minúsculas. Usamos as formas minúsculas presentes no vocabulário carregado e descartamos as demais. A cobertura reportada se refere às 500 mil entradas carregadas, e não a todas as três milhões de entradas do modelo. A busca DM5 pode favorecer documentos curtos, pois usa todas as palavras disponíveis quando restam menos de cinco.

**Questão 4:** as redes aprendem embeddings do zero e usam validação interna para parada antecipada. Os classificadores clássicos são retreinados reproduzindo a lista 2. Nesse protocolo anterior, os vetorizadores foram ajustados sobre a base inteira, o que incorpora informação dos textos de teste na representação. Essa limitação é explicitada no notebook: a comparação reproduz os resultados anteriores, mas não isola apenas o efeito das arquiteturas. O vocabulário das redes é construído apenas no subconjunto de ajuste.

**Questão 5:** as etiquetas e entidades são predições automáticas em textos informais e pré-processados. As contagens da comparação original/pré-processado não medem acurácia. As entidades são normalizadas por grafia, sem resolução completa de siglas e nomes alternativos. Cada peso de aresta conta os tweets com o par de entidades distintas; coocorrência não comprova uma rota aérea, e a posição no desenho não corresponde à geografia.

## Entrega

Inclua o notebook executado, a base, as instruções, as dependências e os resultados das cinco questões. Os grandes modelos externos são obtidos pelos procedimentos acima. A última célula verifica a presença de 35 arquivos de resultados e propriedades das tabelas e do grafo, antes de registrar o ambiente.
