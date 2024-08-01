from dotenv import load_dotenv
import os

load_dotenv()
def read_credentials():
    credentials={}
    host_local=os.getenv('host_local')
    name_db_local= os.getenv('name_db_local')
    user_local= os.getenv('user_local')
    password_local=os.getenv('password_local')


    host_sinfin=os.getenv('host_sinfin')
    name_db_sinfin= os.getenv('name_db_sinfin')
    user_sinfin= os.getenv('user_sinfin')
    password_sinfin=os.getenv('password_sinfin')
    
    credentials = {'local':{
                        'host': host_local, 
                        'name':name_db_local, 
                        'user': user_local, 
                        'password':password_local
                        },
                   'sinfin':{
                        'host': host_sinfin, 
                        'name':name_db_sinfin, 
                        'user': user_sinfin, 
                        'password':password_sinfin                       
                   }
                   }
    
    return credentials