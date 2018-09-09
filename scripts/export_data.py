#
#Export to CSV data/data_yyyymmdd_yyyymmdd.csv
#


import re, csv, lib, psycopg2, os
from psycopg2 import sql


#Check User input
def WaitForDate(fromto):
    result=""
    while bool(re.match(r"^\d{8}$", result))==False:
        print("Please, type date %s in YYYYMMDD format, e.g. 20180910" % fromto)
        result = raw_input('--> ')
    return result

date_from=WaitForDate('FROM')
date_to=WaitForDate('TO')


#Sometimes we need to catch errors ;)
try:
    #Connect to DB
    conn = psycopg2.connect(user="postgres", password="postgres", database='reuters')
    cur = conn.cursor()
    letsgo=lib.CheckDB(cur)
    #Format and SQL query, parse strings to timestamps
    #Add distinct or better something smarter to get_data.py to deduplicate news
    s=sql.SQL("""SELECT id, entry_id, feedburner_origlink, published, title, summary, link
            FROM public.entries
            WHERE to_timestamp(published, 'DY, DD Mon YYYY HH24:MI:SS') BETWEEN 
            TO_TIMESTAMP(%s,'YYYYMMDD') AND TO_TIMESTAMP(%s,'YYYYMMDD')""")
    cur.execute(s, [date_from, date_to])
    data=cur.fetchall()

    #Write to file    
    data_file=os.path.join('data','data_%s_%s.csv' % (date_from, date_to))

    with open(data_file,'wb') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['id','entry_id','feedburner_origlink','published','title','summary','link'])
        for row in data:
            csv_out.writerow(row)
        
except:
    print """There some problems, please check: \n
             PostgreSQL is started \n
             PostgreSQL server is reachable \n
             PostgreSQL reuters schema is created \n
             """



