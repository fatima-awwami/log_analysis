log_analysis
============

The code is a reporting tool that prints out reports (in plain text) based on the data in the news database

Installation:
-----------------------
1- Install python
The program is written in python3. We didn't check if the code runs on python2.
You can find the installation file in the python download webpage.

https://www.python.org/downloads/

3- the database used in this code is PostgreSQL. You need to install the psycopg2 module.
pip install psycopg2

2- Create the required views
Please create below views before you can run the python code.
- news
- date_log
- date_log_error
- error_ratio

CREATE VIEW news As (
SELECT a.title,t.name, split_part(l.path, '/', 3) slug
FROM log l, articles a, authors t
WHERE split_part(l.path, '/', 3) = a.slug
AND t.id = a.author)

CREATE VIEW date_log AS (
SELECT date(time) AS log_date, cast(count(path) as decimal(7,2)) AS log_count
FROM log
GROUP BY date(time))

CREATE VIEW date_log_error AS (
SELECT date(time) AS log_date, cast(count(path) as decimal(7,2)) error_log_count
FROM log
WHERE status like '404%'
GROUP BY date(time))

CREATE VIEW error_ratio AS (
SELECT dl.log_date, cast((dle.error_log_count/dl.log_count)*100.0 as numeric(5,1)) AS log_error_ratio
FROM  date_log dl, date_log_error dle
WHERE dl.log_date = dle.log_date
AND (error_log_count/log_count)*100.0 > 1
ORDER BY cast ((dle.error_log_count/dl.log_count)*100.0 as numeric(5,1)) DESC)

Usage:
-------------
to run the program, run the following command in the terminal. The output will be displayed in the terminal as well.
python logdb.py

Note: You might need to check your version of python when running the file using the above command
python --version

Code output:
-------------
the program output will be a simple text displayed in the terminal
