import pandas as pd
import numpy as np

def outlier_por_desvio_padrao (dataset, coluna):
    
    column_as_list = dataset[coluna].to_list()

    desvio_padrao = np.std(column_as_list, ddof=0)
    outlier = []
    fator_de_mult = 5

    for dado in column_as_list: 
        if dado >= (desvio_padrao*fator_de_mult):
            outlier.append(dado)

    return outlier