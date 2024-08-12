import os
from pathlib import Path
import pandas as pd

path_file = r'Z:\1. Coordinadores\Asignaciones\Naturgy\Bases\Repositorio'

list_file = os.listdir(path_file)

df=[]
for file in list_file:
    name_file = os.path.join(path_file, file)
    df_file = pd.read_excel(name_file)
    df.append(name_file)
    
print(len(df))