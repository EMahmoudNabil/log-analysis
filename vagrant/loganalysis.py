#!/usr/bin/env python3
#!/usr/bin/env python3
# Log Analysis Project
# Udacity Nanodegree Program - Full Stack Web Developer


import psycopg2


# Connect to an existing database
try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print("I am unable to connect to the database")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)
# Open a cursor to perform database operations
cur = db.cursor()

# Query the database "news" to answer the following questions
# 1. What are the most popular 3 articles of all time?
# Answer: "top_articles" -- ### views

cur.execute('''SELECT b.title, count (*)
FROM articles AS b
JOIN log AS c
ON substring(path,10,length(path)) = b.slug
GROUP BY
b.title
ORDER BY
count(*) DESC
LIMIT 3;''')

top_articles = cur.fetchall()

print("")
print ("What are the most popular 3 articles of all time?")
for ele1, ele2 in top_articles:
    print '"{:>}" -- {:<6} views'.format(ele1, ele2)
print( "")

# 2. Who are the most popular article authors of all time?
# Answer is list sorted with most views at the top
# Answer: top_authors -- ### views

cur.execute('''SELECT a.name, count (*)
FROM authors AS a
JOIN articles AS b
ON a.id = b.author
JOIN log AS c
ON substring(path,10,length(path)) = b.slug
GROUP BY
a.name
ORDER BY
count (*) DESC;''')

top_authors = cur.fetchall()

print("Who are the most popular article authors of all time?")
for ele1, ele2 in top_authors:
    print('{:>30} -- {:<6} views'.format(ele1, ele2))
print ("")

# 3. On which days did more than 1% of requests lead to errors?
# Answer: long date (top_errors) -- #% errors

cur.execute('''SELECT
tot.log_dt,
err.err_count,
tot.total_count,
err.err_count/(tot.total_count/1.0) AS pct_err
FROM
(SELECT
date(time) AS log_dt,
count(*) AS total_count
FROM
log
GROUP BY
date(time)) AS tot
JOIN (SELECT
date(time) AS log_dt,
count(*) AS err_count
FROM
log
WHERE
status != '200 OK'
GROUP BY
date(time)) AS err
ON tot.log_dt=err.log_dt
WHERE err.err_count/(tot.total_count/1.0)>0.01;''')

top_errors = cur.fetchall()

print ("On which days did more than 1% of requests lead to errors?")
for ele1, ele2, ele3, ele4 in top_errors:
    print( '                  {:%B-%d-%Y} -- {:.2%} errors'.format(ele1, ele4))
print ("")

# Close communication with the database
cur.close()
db.close()
