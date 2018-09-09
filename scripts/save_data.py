import os, psycopg2, json, lib
from psycopg2 import sql

data_file=os.path.join('data','data.json')

#Get JSON data to dict
def ReadJSON(filename):
    with open(filename, 'r') as f:
        data = json.loads(json.load(f))
    return data


#Insert running fact to feed table. It can be used to monitor
def InsertFeed(json_data, cursor):
    s = "INSERT INTO public.feeds(status, updated, encoding) VALUES('%s','%s','%s')" %\
        (json_data['status'], json_data['updated'], json_data['encoding'])
    cursor.execute(s)

#Insert news to db
def InsertEntries(json_data, cursor):
    for entry in json_data['entries']:
        s=sql.SQL("""INSERT INTO public.entries(entry_id, feedburner_origlink, published, title, summary, link) 
            VALUES(%s,%s,%s,%s,%s,%s)""")
        cur.execute(s, [entry['id'], entry['feedburner_origlink'],\
                        entry['published'], entry['title'], entry['summary'], entry['link']])

#Sometimes we need to catch errors ;)
try:
    #Connect to DB
    conn = psycopg2.connect(user="postgres", password="postgres", database='reuters')
    cur = conn.cursor()
    letsgo=lib.CheckDB(cur)
    if letsgo==False or os.path.exists(data_file)!=True:
        raise Exception('spam', 'eggs')
    #Write data to PostgreSQL
    data=ReadJSON(data_file)
    InsertFeed(data, cur)
    InsertEntries(data, cur)
    #Commit and close connection
    conn.commit()
    conn.close()
    #Delete original file
    if os.path.exists(data_file):
        os.remove(data_file)
except:
    print """There some problems, please check: \n
             PostgreSQL is started \n
             PostgreSQL server is reachable \n
             PostgreSQL reuters schema is created \n
             Data file data.json is exist \n
             """


