#!/usr/bin/env python3
#
# a program to do log analysis on news website database

import psycopg2

db = psycopg2.connect("dbname=news")
cursor = db.cursor()


def get_articles():
    cursor.execute("SELECT title, count(slug) AS views FROM news \
    GROUP BY title ORDER BY count(slug) DESC LIMIT 3")
    articles = cursor.fetchall()
    return articles


def get_authors():
    cursor.execute("SELECT name, count(slug) AS views FROM news GROUP \
    BY name ORDER BY count(slug) DESC")
    authors = cursor.fetchall()
    return authors


def get_errors():
    cursor.execute("SELECT to_char(log_date, 'Month dd, yyyy'), \
    log_error_ratio FROM error_ratio")
    errors = cursor.fetchall()
    return errors


print("\n-- The most popular three articles of all time -- \n")
for row in get_articles():
    print("\"{}\" - {} views".format(row[0], row[1]))

print("\n-- The most popular article authors of all time -- \n")
for row in get_authors():
    print("\"{}\" - {} views".format(row[0], row[1]))

print("\n-- Days did more than 1% of requests lead to errors --\n")
for row in get_errors():
    print("{} - {}% errors".format(row[0], row[1]))

db.close()
