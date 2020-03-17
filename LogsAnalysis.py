#!/usr/bin/python
import psycopg2
DBNAME = "news"
connection = psycopg2.connect(database=DBNAME)
cursor = connection.cursor()

try:
    cursor.execute("""select articles.title, count(*) as views
        from log, articles
        where log.path like concat('%', articles.slug)
        group by articles.title order by views desc limit 3""")
except psycopg2.Error, e:
    pass
result = cursor.fetchall()
