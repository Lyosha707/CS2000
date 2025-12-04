#! /usr/bin/env python3

'''
sql.py

An introduction to SQL using Python's sqlite3 module

'''

## demonstrates python module sqlite3 using examples from the sql tutorial:

## https://sqlbolt.com/lesson/introduction

import sqlite3

## Slade's module for looking at objects and classes
## try display(sqlite3)
##from display import *


## for capturing exception error messages
import sys

## create a connection to database: mydb
connection = sqlite3.connect("mydb.db")
cursor = connection.cursor()

## CREATE command builds a table with the given fields
c1 = """
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    director TEXT,
    year INTEGER, 
    length_minutes INTEGER
);
"""

#cursor.execute(c1)
## here is how you get column names for a table

def desc(table = 'movies'):
    cursor = connection.cursor()
    command = "PRAGMA table_info('{}')".format(table)
    print ("SQL Command: ", command)
    result = cursor.execute(command)
    for r in result:
        print (r)
    
## it is advisable to wrap your database commands with try


## the output here is hardwired for the movies database
def tryit(command):
    cursor = connection.cursor()
    try:
        cursor.execute(command)
        print("fetchall: " + command)
        result = cursor.fetchall() 
        for r in result:
            rformat = "{:3d} {:20} {:15} {:4} {:3}".format(r[0], r[1], r[2], r[3], r[4])
            print(rformat)
        return list(result)
    except:
        e = sys.exc_info()[0]
        print ( "Error: {}".format(e))



c2 = """
INSERT INTO movies
(id, title, director, year, length_minutes)
VALUES
(1, 'Toy Story', 'John Lasseter', 1995, 81);

"""
## cursor.execute(c2)
## can use python to insert a bunch of data:
movie_data = [
    (1, 'Toy Story', 'John Lasseter', 1995, 81),
    (2, "A Bug's Life", 'John Lasseter', 1998, 95),
    (3, 'Toy Story 2', 'John Lasseter', 1999, 93),
    (4, "Monsters, Inc.","Pete Docter", 2001, 92),
    (5, "Finding Nemo","Andrew Stanton", 2003, 107),
    (6, "The Incredibles","Brad Bird", 2004, 116),
    (7, "Cars","John Lasseter", 2006, 117),
    (8, "Ratatouille","Brad Bird", 2007, 115),
    (9, "WALL-E","Andrew Stanton", 2008, 104),
    (10, "Up","Pete Docter", 2009, 101),
    (11, "Toy Story 3","Lee Unkrich", 2010, 103),
    (12, "Cars 2","John Lasseter", 2011, 120),
    (13, "Brave","Brenda Chapman", 2012, 102),
    (14, "Monsters University","Dan Scanlon", 2013, 110) ]


def loadmovies():
    for m in movie_data:
        format_str = """INSERT INTO movies 
        (id, title, director, year, length_minutes)
        VALUES ({id}, "{title}", "{director}", "{year}", "{length_minutes}");"""

        sql_command = format_str.format(id=m[0], title=m[1], director=m[2], year = m[3], length_min>
        cursor.execute(sql_command)

## the commit() saves the changes.
connection.commit()

# SQL Lesson 1: SELECT queries 101

def fetchall(fields = [], table = 'movies'):
    cursor = connection.cursor()
    fstr = '*'
    if fields:
        fstr = ', '.join(fields)
    command = "SELECT " + fstr + " FROM " + table
    print ("SQL Command: ", command)
    cursor.execute(command)
    print("fetchall:")
    result = cursor.fetchall() 
    for r in result:
        print(r)
    return list(result)

##  fetchall()
##  fetchall(['title', 'year'])
##  fetchall(['title', 'year', 'year'])

def fetchone(table = 'movies'):
    cursor = connection.cursor()
    command = "SELECT * FROM " + table
    print ("SQL Command: ", command)
    cursor.execute(command)
    print("fetchone:")
    result = cursor.fetchone() 
    print (result)
    return result
        
# SQL Lesson 2: Queries with constraints (Pt. 2)

# fetchwhere(['title', 'year'], ['year > 2000'])
# fetchwhere(['title', 'year'], ['year > 2000', 'year < 2010'])
# fetchwhere(['title', 'year'], ['year < 2000 OR year > 2010'])


def fetchwhere(fields = [], where = [], table = 'movies'):
    cursor = connection.cursor()
    fstr = '*'
    wstr = ' 1=1 '
    if fields:
        fstr = ', '.join(fields)
    if where:
        wstr = ' AND '.join(where)
    command = "SELECT " + fstr + " FROM " + table + " WHERE " + wstr
    print ("SQL Command: ", command)
    cursor.execute(command)
    print("fetchall:")
    result = cursor.fetchall() 
    for r in result:
        print(r)
    return list(result)

# SQL Lesson 3: Queries with constraints (Pt. 2)

# fetchwhere(['title', 'director'], ['director like "Doc"'])
# fetchwhere(['title', 'director'], ['director like "Pete%"'])
# fetchwhere(['title', 'director'], ['director like "%Doc%"'])

# SQL Lesson 4: Filtering and sorting Query results

def fetchwheresort(fields = [], where = [], sort = [], limit = [], table = 'movies'):
    cursor = connection.cursor()
    fstr = '*'
    wstr = ' 1=1 '
    sstr = ''
    if fields:
        fstr = ', '.join(fields)
    if where:
        wstr = ' AND '.join(where)
    command = "SELECT " + fstr + " FROM " + table + " WHERE " + wstr
    if sort:
        sstr = ', '.join(sort)
        command += " ORDER BY " + sstr
    if limit:
        command += " LIMIT " + str(limit)
    print ("SQL Command: ", command)
    cursor.execute(command)
    print("fetchall:")
    result = cursor.fetchall() 
    for r in result:
        print(r)
    return list(result)

# fetchwheresort([], ['year > 2000'], ['title'], 4)

# SQL Lesson 6: Multi-table queries with JOINs

'''
Joins are commonly used to link together tables.

For example, you might have the following tables:

students (id, name, DOB, college, etc.)
course (id, title, department, hours, credithours, etc.)
classroom (id, building, room, size, AV, etc.)

Then you would have other tables linking the above:

enrollment (student.id, course.id, term, status, etc.)
assignedrooms (course.id, classroom.id, time)

This way you can have one student enrolled in multiple courses in
multiple terms, and have a classroom allocated to multiple courses
over time.

This approach is known as normalization.

See https://en.wikipedia.org/wiki/Database_normalization
'''


c10 = """
CREATE TABLE Boxoffice (
    Movie_id INTEGER PRIMARY KEY,
    Rating float,
    Domestic_sales integer,
    International_sales integer
);
"""

'''
Movie_id        Rating  Domestic_sales  International_sales
5       8.2     380843261       555900000
14      7.4     268492764       475066843
8       8       206445654       417277164
12      6.4     191452396       368400000
3       7.9     245852179       239163000
6       8       261441092       370001000
9       8.5     223808164       297503696
11      8.4     415004880       648167031
1       8.3     191796233       170162503
7       7.2     244082982       217900167
10      8.3     293004164       438338580
4       8.1     289916256       272900000
2       7.2     162798565       200600000
13      7.2     237283207       301700000
'''
boxoffice_data = [
    (5,8.2,380843261,555900000),
    (14,7.4,268492764,475066843),
    (8,8,206445654,417277164),
    (12,6.4,191452396,368400000),
    (3,7.9,245852179,239163000),
    (6,8,261441092,370001000),
    (9,8.5,223808164,297503696),
    (11,8.4,415004880,648167031),
    (1,8.3,191796233,170162503),
    (7,7.2,244082982,217900167),
    (10,8.3,293004164,438338580),
    (4,8.1,289916256,272900000),
    (2,7.2,162798565,200600000),
    (13,7.2,237283207,301700000) ]


def loadboxoffice():
    for m in boxoffice_data:
        format_str = """INSERT INTO Boxoffice
        (Movie_id, Rating, Domestic_sales, International_sales)
        VALUES ({id}, {rating}, {domestic}, {international});"""

        sql_command = format_str.format(id=m[0], rating=m[1],
                                        domestic=m[2], international= m[3])
        cursor.execute(sql_command)

# desc('Boxoffice')
# fetchall([], 'Boxoffice')
# fetchwheresort([], [], [], 4, "Boxoffice")

def fetchwherejoin(fields = [], where = [], sort = [], limit = [], table = 'movies', join = []):
    cursor = connection.cursor()
    fstr = '*'
    wstr = ' 1=1 '
    sstr = ''
    if fields:
        fstr = ', '.join(fields)
    command = "SELECT " + fstr + " FROM " + table 
    ## can handle LEFT, RIGHT, OUTER joins
    ## default is INNER join
    if join:
        if (join.lower().find('join') < 0):
            command += " INNER JOIN " + join
        else:
            command += " " + join
    if where:
        wstr = ' AND '.join(where)
        command += " WHERE " + wstr
    if sort:
        sstr = ', '.join(sort)
        command += " ORDER BY " + sstr
    if limit:
        command += " LIMIT " + str(limit)

    print ("SQL Command: ", command)
    cursor.execute(command)
    print("fetchall:")
    result = cursor.fetchall() 
    for r in result:
        print(r)
    return list(result)

# fetchwherejoin([], [], [], [], 'movies', 'Boxoffice ON movies.id = Boxoffice.movie_id')

# Show the sales numbers for each movie that did better internationally rather than domestically

# fetchwherejoin(['title', 'Domestic_sales', 'International_sales'], ['Domestic_sales < Internation>

# SQL Lesson 7: OUTER JOINs

## used when tables have assymetric data - may not have sales data for some movies.

# SQL Lesson 8: A short note on NULLs
## to process or identify missing data
## WHERE column IS / IS NOT NULL
## connection.close()

c12 = """
INSERT INTO movies
(id, title, director, year)
VALUES
(100, 'Gone With the Wind', 'Victor Fleming', 1939);

"""
## cursor.execute(c12)

# fetchwhere([], ['Length_minutes IS NULL'])

# fetchwherejoin([], [], [], [], 'movies', 'LEFT JOIN Boxoffice ON movies.id = Boxoffice.movie_id')

## RIGHT and FULL are not currently supported in sqlite3

## switch order of tables
# fetchwherejoin([], [], [], [], 'Boxoffice', 'LEFT JOIN Movies ON movies.id = Boxoffice.movie_id')


# SQL Lesson 9: Queries with expressions

# use AS for column aliases

# fetchwherejoin(['title', 'International_sales AS Isales', 'Domestic_sales AS Dsales'], ['Dsales <>

# create new column: Sales ratio

# fetchwherejoin(['title', 'International_sales / Domestic_sales AS Sratio'], ['Sratio > .5'], [], >

## create new column: gross sales millions

# fetchwherejoin(['title', '(International_sales + Domestic_sales) / 1000000 AS Gross_sales_MM'], [>

# SQL Lesson 10: Queries with aggregates (Pt. 1)

## average domestic sales

# fetchwherejoin(['AVG(Domestic_sales)'], [], [], [], 'movies', 'LEFT JOIN Boxoffice ON movies.id =>

# how many movies have a rating < 8?

# fetchwherejoin(['COUNT()'], ['Rating < 8'], [], [], 'movies', 'LEFT JOIN Boxoffice ON movies.id =>

## max, min, avg ratings

# fetchwherejoin(['max(Rating)', 'min(Rating)', 'avg(Rating)'], [], [], [], 'movies', 'LEFT JOIN Bo>


# SQL Lesson 11: Queries with aggregates (Pt. 2)

# SQL Lesson 12: Order of execution of a Query

# SQL Lesson 13: Inserting rows

## we did this above after creating the table

# SQL Lesson 14: Updating rows

def updatewhere(pairs = [], where = [], table = 'movies'):
    cursor = connection.cursor()
    fstr = '*'
    wstr = ' 1=1 '
    command = "UPDATE " + table + " SET "
    if pairs:
        count = len(pairs)
        for p in pairs:
            (column, value) = p
            command += column + " = " + str(value)
            if (count > 1):
                command += ", "
                count -= 1
    if where:
        wstr = ' AND '.join(where)
    command += " WHERE " + wstr
    print ("SQL Command: ", command)
    cursor.execute(command)
    ## show results
    fetchall([], table)


# Change title and year - bogus example

# updatewhere([('title', '"s"'), ('year', 1000)], ['year < 2000'])

# SQL Lesson 15: Deleting rows

def deletewhere(where = [], table = 'movies'):
    cursor = connection.cursor()
    wstr = ' 1=1 '
    command = "DELETE FROM " + table 
    if where:
        wstr = ' AND '.join(where)
    command += " WHERE " + wstr
    print ("SQL Command: ", command)
    cursor.execute(command)
    ## show results
    fetchall([], table)


# deletewhere(['year < 2000'])

# SQL Lesson 16: Creating tables

'''
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
);
'''

''' 
Common data types:
 Integer
 Boolean
 Float, Double, Real
 Character(size)
 Varchar(size)
 Text
 Date
 DateTime
 Blob  (binary objects, e.g., video, audio, code)


Common table constraints:
 PRIMARY KEY - most efficient index
 AUTOINCREMENT - useful for id fields
 UNIQUE - no duplicate entries
 NOT NULL - required field
 CHECK (expression) - check for type, range, etc.
 FOREIGN KEY - referential integrity check

'''

# SQL Lesson 17: Altering tables

c12 = '''
ALTER TABLE movies
ADD seenit BOOLEAN DEFAULT FALSE
'''

# cursor.execute(c12)
# desc()

# updatewhere([('seenit', '"TRUE"')], ['year < 2000'])

c13 = '''
ALTER TABLE movies
DROP seenit 
'''
## DROP not supported by sqlite 

c14 = '''
ALTER TABLE movies
RENAME TO films;
'''

# fetchall([], 'films')

# SQL Lesson 18: Dropping tables

c15 = '''
DROP TABLE IF EXISTS films
'''

#################
## from: http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

## should execute "connection.close()" before running doall()
#################

def total_rows(cursor, table_name, print_out=False):
    """ Returns the total number of rows in the database """
    cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = cursor.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]

def table_col_info(cursor, table_name, print_out=False):
    """ Returns a list of tuples with column informations:
        (id, name, type, notnull, default_value, primary_key)
    """
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()

    if print_out:
        print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
        for col in info:
            print(col)
    return info

def values_in_col(cursor, table_name, print_out=True):
    """ Returns a dictionary with columns as keys and the number of not-null
        entries as associated values.
    """
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()
    col_dict = dict()
    for col in info:
        col_dict[col[1]] = 0
    for col in col_dict:
        cursor.execute('SELECT ({0}) FROM {1} WHERE {0} IS NOT NULL'.format(col, table_name))
        # In my case this approach resulted in a better performance than using COUNT
        number_rows = len(cursor.fetchall())
        col_dict[col] = number_rows
    if print_out:
        print("\nNumber of entries per column:")
        for i in col_dict.items():
            print('{}: {}'.format(i[0], i[1]))
    return col_dict


## should execute "connection.close()" before running doall()
def doall():
    sqlite_file = 'mydb.db'
    table_name = 'movies'

    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    total_rows(cursor, table_name, print_out=True)
    table_col_info(cursor, table_name, print_out=True)
    values_in_col(cursor, table_name, print_out=True) # slow on large data bases


    
#############
## from: https://docs.python.org/2/library/sqlite3.html
#############

def evalsql():
    con = sqlite3.connect("mydb.db")
    con.isolation_level = None
    cur = con.cursor()

    buffer = ""

    print ("Enter your SQL commands to execute in sqlite3.")
    print ("Enter a blank line to exit.")

    while True:
        line = input()
        if line == "":
            break
        buffer += line
        print (buffer)
        if sqlite3.complete_statement(buffer):
            try:
                buffer = buffer.strip()
                cur.execute(buffer)
                if buffer.lstrip().upper().startswith("SELECT"):
                    print (cur.fetchall())
                buffer = ""
            except sqlite3.Error as e:
                print ("An error occurred:", e.args[0])
                buffer = ""

    con.close()
