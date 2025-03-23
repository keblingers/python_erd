from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

def get_variables(db):
    load_dotenv()
    uname = os.environ['UNAME'].split(",")
    passwd = os.environ['PASSWD'].split(",")
    database = os.environ['DATABASE'].split(",")
    host = os.environ['HOST'].split(",")
    db_type = os.environ['DB_TYPE'].split(",")
    db_driver = os.environ['DB_DRIVER'].split(",")

    df = pd.DataFrame(list(zip(uname,passwd,database,host,db_type,db_driver)),columns=['username','passwd','database','host','db_type','db_driver'])
    data = df.query("database == @db")

    return data['username'].iloc[0],data['passwd'].iloc[0],data['database'].iloc[0],data['host'].iloc[0],data['db_driver'].iloc[0]

def sqlalchemy_conn():
    uname, passwd, dbname, hostname, dbdriver = get_variables()
    try:
        engine = create_engine(f'{dbdriver}://{uname}:{passwd}@{hostname}/{dbname}')
        connected = engine.connect()
        return connected
    
    except Exception as error:
        print(error)
    

if __name__ == '__main__':
    sqlalchemy_conn()