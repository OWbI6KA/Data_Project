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
                                      database='Monday')
        cursor = cnx.cursor()
        print('done')
        return cnx, cursor

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
    cnx, cursor = main()
    req = mySQL_script.connect_monday()
    schedule.every(10).seconds.do(mySQL_script.upload_data, req, cursor, cnx)
    while True:
        schedule.run_pending()
        time.sleep(1)
