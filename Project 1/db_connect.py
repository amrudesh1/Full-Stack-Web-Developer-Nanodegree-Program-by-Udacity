#!/usr/bin/env python3
import psycopg2
db = psycopg2.connect("dbname=news user=postgres password=root")
cursor = db.cursor()  # No newline at end of file
