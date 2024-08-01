from pathlib import Path
import pandas as pd
import os

def read_file(engine):
    path = r'Z:\1. Coordinadores\Asignaciones\Naturgy\Bases\Nueva_asignacion'
    list_file_repository = os.listdir(path)
    dfs = []
    dfs_2=[]
    
    for name in list_file_repository:
        name_file = os.path.join(path, name)
        df_mail = pd.read_excel(name_file, sheet_name='BASE CLIENTE')
        dfs.append(df_mail)
        df_sinfin = pd.read_excel(name_file, sheet_name='SINFIN')
        dfs_2.append(df_sinfin)
        
    df_mail_repository = pd.concat(dfs, ignore_index=True)
    df_sinfin_repository = pd.concat(dfs_2, ignore_index=True)
    

    
    return df_mail_repository, df_sinfin_repository
        
        
