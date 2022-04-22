import time
import schedule
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root',
                                      password='nuqboc-zubQi6-vywpyk',
                                      host='34.65.206.211',
                                      database='Monday')
cursor = cnx.cursor()
print('done')

insert = "INSERT INTO table_name (task_id,name,subtasks,contributor,people,status,timing,ref) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
data = (1,1,1,1,1,1,1,1)
cursor.execute(insert, data)
cnx.commit()