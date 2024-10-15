# **Regressão Logística Simples**


Este projeto realiza uma análise de Regressão Logística para prever se um aluno será aceito em uma universidade, com base em fatores como pontuações de exames e GPA. O modelo é treinado para prever a Chance de Admissão com base em um limiar de 0.5, transformando a variável de chance contínua em uma classificação binária.

![image](https://github.com/user-attachments/assets/a7635313-7aa8-488f-a888-14cdcf9c47f3)
- A matriz de correlação mostra as relações entre as diferentes variáveis no seu conjunto de dados. A correlação varia de -1 a 1:

1 significa uma correlação positiva perfeita (quando uma variável aumenta, a outra também aumenta).
0 significa que não há correlação linear.
-1 significa uma correlação negativa perfeita (quando uma variável aumenta, a outra diminui).

### dados.py:
Este arquivo contém o código responsável por carregar conjunto de dados:

O arquivo CSV com os dados de admissão é carregado é baixado diretamente do Kaggle, que contém informações sobre admissões universitárias:
- Para acessar o arquivo: Entre na sua conta do Kaggle > settings > API >create new ticket.
- No terminal use: kaggle datasets download -d mohansacharya/graduate-admissions
- O arquivo vem em zip, mas no próprio codigo dados.py já faço a extração.

### Observações:
- Os dados são divididos em 80% para treino e 20% para teste, usando train_test_split.
Treinamento do Modelo:
- Um modelo de Regressão Logística é criado e treinado com os dados de treino.

### Avaliação do Modelo:
- O modelo faz previsões no conjunto de teste, e a acurácia do modelo é calculada.
- Um relatório de classificação é gerado, incluindo métricas como precisão, recall e F1-score.
- Uma matriz de confusão é exibida para mostrar as previsões corretas e incorretas.
- Define as variáveis independentes (GRE Score, TOEFL Score, etc.) e a variável dependente (Chance of Admit).
- Divide o conjunto de dados em treino e teste.
- Cria e treina o modelo de Regressão Logística.
- Faz previsões no conjunto de teste.
- Avalia o modelo usando métricas como acurácia, relatório de classificação e matriz de confusão.

### Principais Métricas Avaliadas:
- Acurácia: Mede a porcentagem de previsões corretas feitas pelo modelo.
- Relatório de Classificação: Exibe métricas de desempenho como precisão, recall e F1-score para cada classe (admitido/não admitido).
- Matriz de Confusão: Mostra a distribuição de previsões corretas e incorretas, ajudando a identificar possíveis falhas do modelo.
![image](https://github.com/user-attachments/assets/2b15beea-5f28-4797-b344-acf451d22b54)

A matriz de confusão mostra como o modelo de Regressão Logística se saiu em prever a variável de saída (admitido ou não admitido). Ela contém quatro quadrantes:

Verdadeiros Negativos (TN): O número de exemplos que eram realmente da classe negativa (não admitido) e foram previstos corretamente como negativos (canto superior esquerdo).
Falsos Positivos (FP): O número de exemplos que eram da classe negativa (não admitido), mas foram previstos como positivos (canto superior direito).
Falsos Negativos (FN): O número de exemplos que eram da classe positiva (admitido), mas foram previstos como negativos (canto inferior esquerdo).
Verdadeiros Positivos (TP): O número de exemplos que eram da classe positiva (admitido) e foram previstos corretamente como positivos (canto inferior direito).
![image](https://github.com/user-attachments/assets/6fd94869-4788-470a-ac56-26a9eeaa8bbc)


