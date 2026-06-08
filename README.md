# Sistema de Auxílio ao Diagnóstico de Doenças Cardíacas

Curso: Análise e Desenvolvimento de Sistemas (ADS-5B)

## Integrantes do Grupo e RA
[Gabriel Veloso Barbosa] - RA: [1990821]
[Gabriela Dos Santos Lima] - RA: [2014108]
[Gustavo Lima Dos Santos] - RA: [1992035]

## Links do Projeto
Aplicativo online: [https://proejto-doenca-cardiaca-qt9upcjz9hx2vw8gm2kuom.streamlit.app/]
Dataset original: https://www.kaggle.com/datasets/redwankarimsony/heart_disease_uci

## 1. Descrição do Problema 
O projeto desenvolve um sistema de triagem para analisar o risco de doenças cardíacas usando o dataset heart_disease_uci.csv.

OBJETIVO: Criar um modelo preditivo capaz de sinalizar o risco cardíaco, priorizando o modelo **Recall** para reduzir o máximo de Falsos Negativso. Deixar de diagnosticar um paciente doente, pois liberar um paciente cardíaco sem tratamento é crítico.

No contexto médico, priorizou o aumento do Recall. O objetivo é reduzir ao máximo os Falsos Negativos. Deixar de diagnosticar um paciente doente, já que  liberar um paciente cardíaco sem tratamento é crítico.

## 2. Tipo de Problema de Machine Learning e Metodologia
**Tipo de Aprendizado:** Supervisionado 
**Tarefa:** Classificação Binária (0: Sem risco, 1: Presença de risco)
**Dataset utilizado:** Heart Disease UCI
**Modelos Treinados:** Regressão Logística,SVC e KNN 
**Modelo Final:** SVC, devido ao melhor desempenho e maior sensibilidade dos dados clinicos.

**CORREÇÃO:**
1. Os dados foram divididos de forma balanceada em Treino, Validação e Teste
2. O "StandardScaler" foi ajustado "fit" exclusivo para o conjunto de treino, e só aplicado nos demais conjuntos.
3. O conjutno de validação foi utilzado para calibrar os parâmetros e fixar os valores da variavel "SEED=42"

## 3. Tecnologias Utilizadas
- Python 3.11+
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit


## 4. Análise Exploratória de Dados (EDA)
**Gráficos de pessoas saúdaveis e não saúdaveis:** O gráfico nós mostra quantos pacientes são saúdaveis ou não.
**Distribuição por Gênero:** Foram criadas análises cruzando o Gênero com os casos da doença.
**Distribuição de idade por doença cardíaca:** Foram criadas analises cruzando as idades dos pacientes e se tinha doença cardíaca ou não.
**Outliers:** Identificação e tratamento de valores diferentes em variáveis como Colesterol e Pressão Arterial para não distorcer o modelo.
**Mapa de calor:** Foi uitilizado um mapa de calor para vermos quais variaveis mais influenciam a doença cardíaca.

## 5. Resultados e Desempenho do Modelo
Métricas finais obtidas no conjunto de Teste com o SVC:

* Acurácia: 84.24%
* Precisão: 86.46%
* Recall: 90.20%
* F1-Score: 86.38%
* AUC-ROC: 91.67%

As variáveis com maior peso para o diagnóstico foram o número de vasos coloridos (ca), tipo de dor torácica (cp) e depressão do segmento ST (oldpeak).

## 6. Estrutura do Projeto
Projeto_Doenca_Cardiaca/
│
├── app.py
│
├── models/
│   ├── modelo_doenca_cardiaca.joblib
│   └── scaler_modelo_doenca_cardiaca.joblib
│
├── data/
│   └── heart_disease_uci.csv
│
├── notebooks/
│   └── trabalhoML_Atualizado_P2.ipynb
│
├── reports/
│   └── Relatorio_Projeto_Doenca_Cardiaca.pdf
│
├── README.md
│
└── requirements.txt



## 7. Intruções de Execução
**Execução pelo Notebook:**

1. Abra o Google Colab

2. Abra a pasta "notebooks" de Projetos_Doenca_Cardiaca e abra o arquivo trabalhoML_Atualizado_P2.ipynb.

3- Verifique se o arquivo hear_disease_uci.csv está no caminho correto do codigom e execute em ordem sequencial.

**Execução App Streamlit:**

Caso queria abrir o aplicatio direto, clique no link que está escrito
Links Do Projeto:
**Aplicativo Online**


Caso queria rodar pelo terminal:

1  - Baixar a pasta: Projet_Doenca_Cardiaca

2- Abra o terminal com o caminho da pasta

3- Instale as dependências:
pip install -r requirements.txt

4- Execute para abrir o aplicativo:
stream lit run app.py
Caso ocorra erro de comando não reconhecido, utilize: **python -m streamlit run app.py** 

Logo em seguida o terminal irá informar o endereço do Localhost para acessar o sistema pelo navegador.

## 8.Funcionamento
1- O usuario infroma os dados sobre o paciente no App

2- Os dados são normalizados utilizando o scaler salvo

3- O modelo processa as informações

4- O aplicativo retorna a previsão, indicando possivel doença cardíaca ou não.

## 9. Limitações do Projeto
O volume de dados utilizados para o treinamento, é relativamente pequeno. Para que o algoritmo tivesse mais confiabilidade, o necessario é um treinamento com uma base de dados maior.

## 10. Conclusão
O proejto atingiu as métricas esperadas ao aplicar o que foi ensinado em sala de aula e estudado por fora. Solucionado o problema de vazamento de dados que teve na primeira entrega deste projeto e as incoerências do Notebook e Relatório. 
TeVe um Recall de 90.20% utilizando o algoritmo SVC, o App em todo mostra que estatiscamente eficiente e seguro para atuar como um apoio na identificação de possiveis doenças cardíacas, tentando minimizar ao maximo as triagens feitas em ambientes clinicos.
## Autores
Gabriel Veloso Barbosa/
Gabriela Dos Santos Lima/
Gustavo Lima Dos Santos/
