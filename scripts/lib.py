#
#Common function to reuse in scripts to check PostgreSQL schema existance
#

#Flag to check table or database are exist
scl_c="case when Count(*)>0 then 1 else 0 end as flag"

#Googled queries to check existance
sql_checkdb="SELECT %s FROM pg_catalog.pg_database WHERE datname = 'reuters';" % scl_c
sql_checkfeed="SELECT %s FROM pg_tables where schemaname='public' and tablename='feeds';" % scl_c
sql_checkentry="SELECT %s FROM pg_tables where schemaname='public' and tablename='entries';" % scl_c


#Summarize tests and return the verdict
def CheckDB(cursor):
    result=False
    cursor.execute(sql_checkdb)
    db_exist=cursor.fetchone()[0]
    cursor.execute(sql_checkfeed)
    feed_exist=cursor.fetchone()[0]
    cursor.execute(sql_checkentry)
    entry_exist=cursor.fetchone()[0]
    if db_exist+feed_exist+entry_exist==3:
        result=True
    return result
