import mysql.connector
from mysql.connector import errorcode
import configparser

config = configparser.ConfigParser()
config.read('.my.cnf')
'''
try:
    conn = mysql.connector.connect(read_defualt_file='.my.cnf')
    conn1 = mysql.connector.connect()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Check credentials')

conn.close()

'''
'''
db_config = {
  'user': config['mysql']['user'],
  'password': config['mysql']['password'],
  'host': config['mysql']['host'],
  'database': config['mysql']['database'],
  'raise_on_warnings': True
}
'''
try:
    cnx = mysql.connector.connect(**config['mysql'])
    print('Connected Successfully...')
except:
    print('Error')
cnx.close()