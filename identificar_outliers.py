import pandas as pd
import numpy as np

def outlier_por_desvio_padrao (dataset, coluna):
    
    column_as_list = dataset[coluna].to_list()

    standard_deviation = np.std(column_as_list, ddof=0)
    mean = np.mean(column_as_list)
    outlier = []
    fator_multiplicacao = 3

    for data in column_as_list: 
        if data >= mean + (standard_deviation*fator_multiplicacao):
            outlier.append(data)
        if data <= mean + (standard_deviation*fator_multiplicacao) * -1:
            outlier.append(data)

    return outlier