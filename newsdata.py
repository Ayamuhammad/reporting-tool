#python version: 3.7.2
#This reporting tool is a Python program using the psycopg2 module to connect to the database.
import psycopg2

DBNAME = "news"
#'''
def get_articles():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""select title, count(*) as sum
                      from articles join log
                      on concat('/article/', articles.slug) = log.path
                      where log.status like '%200%'
                      group by log.path, articles.title
                      order by sum desc
                      limit 3;""")
    result = cursor.fetchall()
    print result
    db.close()
#'''
#'''
def get_authors():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""select authors.name, count(*) as sum
                      from articles join authors
                      on articles.author = authors.id join log
                      on concat('/article/', articles.slug) = log.path where
                      log.status like '%200%'
                      group by authors.name
                      order by sum desc;""")
    result = cursor.fetchall()
    print result
    db.close()
#'''
#'''
def get_errors():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""select *
                      from (select a.day, cast((100*b.hits) as numeric) / cast(a.hits as numeric) as subqq
                            from (select date(time) as day, count(*) as hits
                                  from log
                                  group by day) as a join (select date(time) as day, count(*) as hits
                                                           from log
                                                           where status like '%404%'
                                                           group by day) as b on a.day = b.day)
                      as sqq where subqq > 1.0;""")
    result = cursor.fetchall()
    print result
    db.close()
#'''
if __name__ == '__main__':
#'''
    print ""
    print "Q1. what are the most popular three articles of all time?"
    print "A1"
    get_articles()
#'''
#'''
    print ""
    print "Q2. who are the most popular article authors of all time?"
    print "A2"
    get_authors()
#'''
#'''
    print ""
    print "Q3. on which days did more than 1% of requests lead to errors?"
    print "A3"
    get_errors()
#'''
