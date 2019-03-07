# How to run the program

##### Step one: prepare the software
* install vagrant last version
* install virtual box
* install python
* up the machine into vagrant and login

##### step two: create views
-I have attached a full guide for create views commands and their output tables, the file named `views queries and tables.txt` for easier checking if needed, here they are for quick copying:
1- CREATE VIEW authcles as select articles.author, articles.title, articles.slug, articles.time, articles.id, authors.name from articles join authors on articles.author = authors.id;

2- CREATE VIEW bad_clicks as (SELECT date(time), COUNT(*) AS bad_c from log where status = '404 NOT FOUND' group by date(time) order by date(time));

3- CREATE VIEW all_clicks as (SELECT date(time), COUNT(*) AS all_c from log group by date(time) order by date(time));

4- CREATE VIEW clicksbg as (select * from all_clicks join bad_clicks using (date));

5- CREATE VIEW clicksbg_h as (select * from clicksbg where 1/(all_c/100) < (bad_c*100)/all_c);


##### step three: run the python file
`$python  python source_code.py`
