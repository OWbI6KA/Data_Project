import json, time, requests, schedule
import mysql.connector
from mysql.connector import errorcode
from config import userHost, userName, userPassword, db_name
import pyodbc
import textwrap

driver = '{ODBC Driver 18 for SQL Server}'

server_name = 'mondaydata'
database_name = 'mondayDatabase'

# config = {
#     'host': 'mondaydata.database.windows.net',
#     'user': 'mondayAdmins@mondaydata',
#     'password': 'S3FmZni@xh9rtER',
#     'database': 'mondayDatabase',
#     'client_flags': [mysql.connector.ClientFlag.SSL],
#     'ssl_ca': 'DigiCertGlobalRootG2.crt.pem'
# }
driver = '{ODBC Driver 18 for SQL Server}'

server_name = 'mondaydata'
database_name = 'mondayDatabase'

server = '{server_name}.database.windows.net, 1433'.format(server_name=server_name)

username = 'mondayAdmins'
password = "S3FmZni@xh9rtER"

connection_string = textwrap.dedent(f'''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
    driver=driver,
    server=server,
    database=database_name,
    username=username,
    password=password
))


cnxn: pyodbc
# Construct connection string
def create_connection():

def main():
    create_connection()
    return 0


if __name__ == '__main__':
    main()
