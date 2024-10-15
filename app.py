from dados import get_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Obter os dados do arquivo dados.py
data = get_data()

# Remover espaços extras dos nomes das colunas
data.columns = data.columns.str.strip()

# Converter a coluna 'Chance of Admit' para uma variável binária
# Definimos 0.5 como limiar (cutoff) - Se a chance for >= 0.5, classifica como 1 (admitido), caso contrário, 0
data['Chance of Admit'] = (data['Chance of Admit'] >= 0.5).astype(int)

# Definir as variáveis independentes (X) e a dependente (y)
X = data[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research']]
y = data['Chance of Admit']

# Dividir os dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de Regressão Logística com max_iter aumentado para garantir a convergência
model = LogisticRegression(max_iter=1000)

# Treinar o modelo com os dados de treino
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy * 100:.2f}%")

# Relatório de classificação
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

# Matriz de Confusão
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()
