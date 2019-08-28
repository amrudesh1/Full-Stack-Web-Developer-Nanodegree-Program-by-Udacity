#!/usr/bin/env python3
import db_connect as db


def get_top_articiles_fromDB():
    sql = """SELECT title, count(title) AS views
            FROM articles, log
            WHERE log.path=CONCAT('/article/',articles.slug)
            AND log.status LIKE '%200%'
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;"""
    db.cursor.execute(sql)
    return db.cursor.fetchall()


def get_popular_article_authors_fromDB():
    sql = """SELECT authors.name, count(*) as views FROM articles inner
            JOIN authors on articles.author = authors.id inner
            JOIN log on log.path LIKE concat('%', articles.slug, '%')
            WHERE log.status LIKE '%200%'
            GROUP BY authors.name
            ORDER BY views DESC;"""
    db.cursor.execute(sql)
    return db.cursor.fetchall()


def get_fail_days_fromDB():
    sql = """SELECT * FROM (SELECT date(time),round(100.0*sum(CASE log.status
            WHEN '200 OK'  THEN 0 ELSE 1 END)/count(log.status),3)
            AS error FROM log
            GROUP BY date(time)
            ORDER BY error DESC) AS subquery
            WHERE error > 1;"""
    db.cursor.execute(sql)
    return db.cursor.fetchall()


def close_conn():
    """ Function to close the connection to the database """
    if db.cursor:
        db.cursor.close()
    if db.db:
        db.db.close()


def print_table(fun):
    if fun == get_top_articiles_fromDB:
        count_type = ' views'
        print('Top 3 Articles:')
    elif fun == get_popular_article_authors_fromDB:
        count_type = ' views'
        print('Top Authors:')
    else:
        count_type = '% errors'
        print('Days With More Than 1% Errors:')
    rows = fun()
    for row in rows:
        print("%s - %s%s" % (str(row[0]), str(row[1]), count_type))
    print()


if __name__ == '__main__':
    print_table(get_top_articiles_fromDB)
    print_table(get_popular_article_authors_fromDB)
    print_table(get_fail_days_fromDB)
    close_conn()
