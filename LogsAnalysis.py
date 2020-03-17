#!/usr/bin/python
import psycopg2
DBNAME = "news"
connection = psycopg2.connect(database=DBNAME)
cursor = connection.cursor()
