# import json, time, requests, schedule
# import mysql.connector
# from mysql.connector import errorcode
# from config import userHost, userName, userPassword, db_name
# import pyodbc
# import textwrap

# driver = '{ODBC Driver 18 for SQL Server}'
#
# server_name = 'mondaydata'
# database_name = 'mondayDatabase'
#
# # config = {
# #     'host': 'mondaydata.database.windows.net',
# #     'user': 'mondayAdmins@mondaydata',
# #     'password': 'S3FmZni@xh9rtER',
# #     'database': 'mondayDatabase',
# #     'client_flags': [mysql.connector.ClientFlag.SSL],
# #     'ssl_ca': 'DigiCertGlobalRootG2.crt.pem'
# # }
# driver = '{ODBC Driver 18 for SQL Server}'
#
# server_name = 'mondaydata'
# database_name = 'mondayDatabase'
#
# server = '{server_name}.database.windows.net, 1433'.format(server_name=server_name)
#
# username = 'mondayAdmins'
# password = "S3FmZni@xh9rtER"
#
# connection_string = textwrap.dedent(f'''
#     Driver={driver};
#     Server={server};
#     Database={database};
#     Uid={username};
#     Pwd={password};
#     Encrypt=yes;
#     TrustServerCertificate=no;
#     Connection Timeout=30;
# '''.format(
#     driver=driver,
#     server=server,
#     database=database_name,
#     username=username,
#     password=password
# ))
#
#
# cnxn: pyodbc
# # Construct connection string
# # def create_connection():
# #
# # def main():
# #     create_connection()
# #     return 0
#
#
# # if __name__ == '__main__':
# #     main()


# import schedule
# import time
#
#
# def printing():
#     print('Я блять работаю')
#
#
# schedule.every(10).seconds.do(printing(),int)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

import time
import schedule
import mysql.connector
from mysql.connector import errorcode

import mySQL_script


def main():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='nuqboc-zubQi6-vywpyk',
                                      host='34.65.206.211',
                                      database='monday')
        cursor = cnx.cursor()
        print('done')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print('dont work')
        cnx.close()

if __name__ == "__main__":
    main()
