# Atividade 1 — Processamento de Linguagem Natural

Resolução da primeira lista de exercícios, com seis questões. Os resultados da execução estão salvos no notebook.

## Arquivos

- [lista1.pdf](lista1.pdf): enunciado da atividade.
- [atividade_1_senha.ipynb](atividade_1_senha.ipynb): notebook com as seis questões.
- [dados/Tweets.csv](dados/Tweets.csv): base com 14.640 tweets, usada nas questões 4, 5 e 6.
- [dados/README.md](dados/README.md): identificação da fonte da base.
- [resultados](resultados): contagens, vocabulário, matriz esparsa, histograma e resultados da Questão 6.
- [requirements.txt](requirements.txt): versões das bibliotecas utilizadas na execução local.

## Executar no Google Colab

1. Abra o notebook no Google Colab, pela opção de abrir um arquivo do GitHub ou enviando o arquivo `.ipynb`.
2. Execute as células em ordem.
3. Na Questão 4, envie o arquivo `Tweets.csv` quando a célula solicitar. O notebook do GitHub não carrega automaticamente os demais arquivos do repositório no ambiente do Colab.
4. Na Questão 6, os recursos do NLTK serão baixados caso ainda não estejam disponíveis. Essa etapa precisa de acesso à internet.

Os arquivos gerados ficam em `resultados` no ambiente onde o notebook for executado. No Colab, podem ser baixados pelo painel de arquivos.

## Executar localmente

Em um ambiente Python com Jupyter disponível, instale as dependências:

```sh
python -m pip install -r atividade_1/requirements.txt
```

Abra o notebook com a pasta de trabalho definida como `atividade_1`, para que os caminhos relativos de dados e resultados sejam encontrados.

## Conteúdo

1. Verificação de senha forte.
2. Validação básica de e-mail com expressões regulares.
3. Extração de autores, ano, título e editora de referências de livros.
4. Distribuição dos comprimentos dos tweets e histograma.
5. Limpeza dos textos, vocabulário e vetores de contagem; dez palavras mais frequentes.
6. Remoção de stopwords, POS e stemização; exemplos e comparações de frequência.

## Critérios e limitações

A contagem de palavras usa a separação por espaços em branco. O notebook explica as escolhas de limpeza, o uso de recursos em inglês e o armazenamento esparso dos vetores.

A Questão 3 funciona para o exemplo da lista, mas ainda considera editoras sem pontos internos. Uma editora como `W. W. Norton` pode ser separada incorretamente do título.

As etiquetas POS da Questão 6 são estimativas do modelo e podem conter erros nos tweets já limpos.

Os diretórios `.python-deps`, `.matplotlib-cache` e `dados/nltk_data` são recursos locais e estão excluídos do Git. A base de tweets e os resultados da atividade estão incluídos.
