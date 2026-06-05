# Sistema de Auxílio ao Diagnóstico de Doenças Cardíacas

Curso: Análise e Desenvolvimento de Sistemas (ADS-5B)

## Integrantes do Grupo e RA
[Gabriel Veloso Barbosa] - RA: [1990821]
[Gabriela Dos Santos Lima] - RA: [2014108]
[Gustavo Lima Dos Santos] - RA: [1992035]

## Links do Projeto
Aplicativo online: [O link será inserido após o deploy]
Dataset original: https://www.kaggle.com/datasets/redwankarimsony/heart_disease_uci
Vídeo Aluno 1: [Link do Drive]
Vídeo Aluno 2: [Link do Drive]
Vídeo Aluno 3: [Link do Drive]

## 1. Descrição do Problema 
O projeto desenvolve um sistema de triagem para analisar o risco de doenças cardíacas usando o dataset heart_disease_uci.csv.

No contexto médico, priorizou o aumento do Recall. O objetivo é reduzir ao máximo os Falsos Negativos. Deixar de diagnosticar um paciente doente, já que  liberar um paciente cardíaco sem tratamento é crítico.

## 2. Tipo de Aprendizado e Metodologia
Tipo de Aprendizado: Supervisionado Tarefa: Classificação Binária (0: Sem risco, 1: Presença de risco)
Algoritmo Escolhido: SVC

Para corrigir os problemas de validação da P1 e eliminar o vazamento de dados "data leakage":
1. Os dados foram divididos de forma balanceada em Treino, Validação e Teste.
2. O StandardScaler foi aplicado corretamente no conjunto de treino e apenas transformado nos demais.
3. O conjunto de validação foi utilizado para calibrar os parâmetros e fixar a reprodutibilidade com a variavel SEED = 42.

- Python 3.11+
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit


## 3. Análise Exploratória de Dados (EDA)
Distribuição por Gênero: Foram criadas análises cruzando o Gênero com os casos da doença.
Outliers: Identificação e tratamento de valores diferentes em variáveis como Colesterol e Pressão Arterial para não distorcer o modelo.

## 4. Resultados e Desempenho do Modelo
Métricas finais obtidas no conjunto de Teste com o SVC:

* Acurácia: 84.24%
* Precisão: 86.46%
* Recall: 90.20%
* F1-Score: 86.38%
* AUC-ROC: 91.67%

As variáveis com maior peso para o diagnóstico foram o número de vasos coloridos (ca), tipo de dor torácica (cp) e depressão do segmento ST (oldpeak).

## 5. 📂 Estrutura do Projeto
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



## 6. Como executar
1  - Baixar a pasta: Projet_Doenca_Cardiaca

2- Abra o terminal com o caminho da pasta

3- Instale as dependências:
pip install -r requirements.txt

4- Execute para abrir o aplicativo:
stream lit run app.py
Caso não for, rode:
python -m streamlit run app.py

Após isso, vai aparecer o localhost para acessar o aplicativo.

## 7.Funcionamento
1- O usuario infroma os dados sobre o paciente

2- Os dados são normalizados utilizando o scaler salvo

3- O modelo processa as informações

4- O aplicativo retorna a previsão, indicando possivel doença cardíaca.

## Autores
Gabriel Veloso Barbosa
Gabriela Dos Santos Lima
Gustavo Lima Dos Santos
