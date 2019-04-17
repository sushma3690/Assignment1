#!/usr/bin/env python3
#
# coding: utf-8
import psycopg2
import bleach
import calendar


def question_1():
    db = psycopg2.connect(database='news')
    c = db.cursor()
    c.execute("select articletitle as title, count(*) "
              "as total from mainview group "
              "by articletitle order by total "
              "desc limit 3")
    res = c.fetchall()
    db.close()
    for title, total in res:
        print(title + ' --- ' + str(total) + ' views')


print('Popular three articles of all time :')
question_1()
print('\n')


def question_2():
    db = psycopg2.connect(database='news')
    c = db.cursor()
    c.execute(
        "select name, count(*) as total from mainview "
        "group by name order by total desc;")
    res = c.fetchall()
    db.close()
    for name, total in res:
        print(name + ' --- ' + str(total) + ' views')


print('Popular authors of all time :')
question_2()

print('\n')


def question_3():
    db = psycopg2.connect(database='news')
    c = db.cursor()
    c.execute("SELECT count(t1.status)*100.0/t2.total as "
              "percentage,t1.time::date as date FROM log AS t1 "
              "JOIN ( SELECT count(status) AS total,time::date "
              "FROM log GROUP BY time::date) AS t2 "
              "ON t1.time::date = t2.time::date where "
              "t1.status not like '%200%' "
              "GROUP BY t1.time::date,t2.total "
              "having count(t1.status)*100.0/t2.total > 1.0;")
    res = c.fetchall()
    db.close()
    for percentage, date in res:
        res = str(date).split("-")
        print(calendar.month_name[int(res[1])] +
              ' ' +
              res[2] +
              ',' +
              res[0] +
              ' --- ' +
              str(percentage) +
              ' errors')


print('On which days did more than 1% of requests lead to errors :')
question_3()
