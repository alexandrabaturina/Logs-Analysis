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
print('Three most popular articles:')
for r in result:
    print(r[0] + ' - ' + str(r[1]) + ' views')
print('\n')

try:
    cursor.execute("""select authors.name, count(*) as views
    from log, authors, articles
    where log.path like concat('%', articles.slug) and
    authors.id=articles.author
    group by authors.name order by views desc""")
except psycopg2.Error, e:
    pass
result = cursor.fetchall()
