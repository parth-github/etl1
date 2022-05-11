import configparser
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
from db_queries import select_queries

config = configparser.ConfigParser()
config.read('.my.cnf')

try:
    cnx = mysql.connector.connect(**config['mysql'])
    print('Connected Successfully...')
    df = pd.read_sql(select_queries[0], cnx)
    #print(df.head)
    print(df.dtypes)
    '''for row in df.iterrows():
        print(row[0:2])'''

except Exception as e:
    print(f'Error...{e}')

finally:
    cnx.close()