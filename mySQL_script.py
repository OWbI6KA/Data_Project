import json
import requests

from mySQL_mondayInfo import apiUrl, headers, data


def connect_monday():
    return requests.post(url=apiUrl, json=data, headers=headers)


def upload_data(req, cursor, cnx):
    print('working')
    data = json.loads(req.text)
    delete = "DELETE FROM monday_data"
    cursor.execute(delete)
    cnx.commit()

    for kek in data['data']['boards'][0]['items']:
        temp = ""
        if kek['subitems'] == None:
            temp = "None"
        else:
            for t in kek['subitems']:
                temp = temp + t['name'] + "; "
        temp = temp[:-2]
        if kek['column_values'][3]['text'] != "":
            r = kek['column_values'][3]['text'].split(' ')[2]
        else:
            r = "Null"
        insert = "INSERT INTO monday_data (task_id,name,subtasks,contributor,people,status,timing) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (int(kek['id']), kek['name'], temp, kek['column_values'][0]['text'], kek['column_values'][1]['text'],
                kek['column_values'][2]['text'], r)
        cursor.execute(insert, data)
        cnx.commit()


def leftJoin(cursor, cnx):
    join = "INSERT INTO table_name_1 (column_1, column_2, column_3, column_4) " \
           "SELECT column_1, column_2, column_3, 2 " \
           "FROM mondayProject.table_name " \
           "WHERE mondayProject.table_name.column_1 " \
           "not in SELECT column_1 " \
           "from mondayProject.table_name_1)"
    cursor.execute(join)
    cnx.commit()
