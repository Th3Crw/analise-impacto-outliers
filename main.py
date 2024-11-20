import pandas as pd
import numpy as np
from identificar_outliers import *

arquivo = r"C:\Users\joaou\Desktop\Analise do Impacto de Outliers\data sample\idades_alunos.xlsx"
coluna = "Idades"
dataset = pd.read_excel(arquivo)

outliers = print(outlier_por_desvio_padrao(dataset, coluna))


