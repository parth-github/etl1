import mysql.connector
from mysql.connector import errorcode
import configparser
from db_queries import select_queries

config = configparser.ConfigParser()
config.read('.my.cnf')

try:
    cnx = mysql.connector.connect(**config['mysql'])
    print('Connected Successfully...')
    cur = cnx.cursor()
    cur.execute(select_queries[0])
    for row in cur:
        print(row)
except Exception as e:
    print(f'Error...{e}')
finally:
    cnx.close()
    print("Connection closed...")