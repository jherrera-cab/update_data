from sqlalchemy import create_engine
import os
import pandas as pd
from dotenv import load_dotenv


def create_conection(credentials):
    load_dotenv()
    engine_local = create_engine(f"postgresql://{credentials['local']['user']}:{credentials['local']['password']}@{credentials['local']['host']}/{credentials['local']['name']}")
    
    if engine_local.connect():
        print('Conexion exitosa a la DB')
    else:
        print('Falla de conexion en la DB')
        

    return engine_local