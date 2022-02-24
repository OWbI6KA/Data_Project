import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal

config = {
    'host': 'mondaydata.database.windows.net',
    'port': '1433',
    'user': 'mondayAdmins@mondaydata',
    'password': 'S3FmZni@xh9rtER',
    'database': 'mondayDatabase',
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': 'DigiCertGlobalRootG2.crt.pem'
}

# config = {
#     'host': 'mondaydata.database.windows.net',
#     'user': 'mondayAdmins@mondaydata',
#     'password': 'S3FmZni@xh9rtER',
#     'database': 'mondayDatabase',
#     'client_flags': [mysql.connector.ClientFlag.SSL],
#     'ssl_ca': 'DigiCertGlobalRootG2.crt.pem'
# }

# Construct connection string

try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM monday_data;")
    rows = cursor.fetchall()
    print("Read", cursor.rowcount, "row(s) of data.")