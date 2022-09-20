import pandas as pd
import numpy as np

# Cargo una lista de dataframes por cada hoja en el archivo
dataframes = pd.read_excel('static/excel/CPdescarga.xls', sheet_name=None)

estados = set()
municipios = set()
estados_list = []

# Recorro cada uno de los sheets
for key in dataframes:
    if key == 'Nota':
        continue
    
    dt = dataframes[key]
    estados_dt = dt['d_estado'].unique()
    
    estados.update(estados_dt)
    
    print(dt)
    # estados_list.
    

print(sorted(estados))