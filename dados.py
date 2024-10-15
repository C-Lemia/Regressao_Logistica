import pandas as pd
import zipfile
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Defina o caminho para o arquivo zip que você baixou
zip_file_path = 'C:\\Users\\camil\\sentimento\\graduate-admissions.zip'

# Defina o caminho onde o arquivo será extraído
extract_dir = 'C:\\Users\\camil\\sentimento\\extracted_files'

# Extraia o conteúdo do arquivo zip
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)  # Extrai para o diretório especificado

# Listar os arquivos extraídos para garantir que o arquivo correto esteja lá
extracted_files = os.listdir(extract_dir)
print("Arquivos extraídos:", extracted_files)

# Agora carregue o CSV extraído (ajuste o nome do arquivo se necessário)
csv_file_path = os.path.join(extract_dir, 'Admission_Predict.csv')

# Carregar o CSV
data = pd.read_csv(csv_file_path)

# Visualize os primeiros dados
print(data.head())

# Checar por valores faltantes
print(data.isnull().sum())

# Visualizar a correlação entre as variáveis
sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")
plt.show()

# Adicionar uma função para retornar o dataframe
def get_data():
    return data
