#! /usr/bin/python3

import sqlite3
## for capturing exception error messages
import sys
## for creating /tmp database file using process id
import os

# ********************************************************
# CS 200 HW #6   DUE Wednesday, 12/3/2025 at 11:59 pm
#                via gradescope
# ********************************************************
# Name:
# Email address:
# ********************************************************

# This file may be opened in python 3
# Lines beginning with hashes are comments.

# If you are asked to write a procedure, please make sure it has 
# the specified name, and the specified number and order of arguments.  
# The names of the formal arguments need not be the same
# as in the problem specification.

# For each problem, the intended inputs to your procedures
# are specified (for example, "positive integers") 
# and your procedures need not do anything reasonable 
# for other possible inputs.

# You may write auxiliary procedures in addition to
# the requested one(s) -- for each of your auxiliary 
# procedures, please include a comment explaining
# what it does, and giving an example or two.

# You may also use procedures you have written 
# elsewhere in this assignment or previous assignments.
# They only need to be defined once somewhere within this file.

# Reading: https://sqlbolt.com/lesson/introduction

# ********************************************************
# ** problem 0 ** (1 easy point) 
# Replace the number 0 in the definition below to indicate
# the number of hours you spent doing this assignment
# Decimal numbers (eg, 6.237) are fine.  Exclude time
# spent reading.

def hours():
    return 0


# ********************************************************
# ** problem 1 (and only) ** (39 points)

## Note: the solution file for the following questions is
## /c/cs200/hws/hw6a.pyc


## Using sqlite3, define tables for person, likes, friends, children,
## and siblings that exhibit the following behavior.
## Use the Hamlet data from hamlet.py.

## You will need to modify the code from sql.py in the lectures directory.
## 


'''
create a connection to a database
create a cursor
create a table 'person'
populate the person table with the Hamlet data
create and populate the following related tables:
  like_table
  friends
  children
  siblings

Once you have done that, you should be able to execute the following queries.

>>> fetchall([], 'person')
SQL Command:  SELECT * FROM person
fetchall:
(1, 'Hamlet', 'male', 25)
(2, 'Claudius', 'male', 55)
(3, 'King Hamlet', 'male', 60)
(4, 'Larry', 'male', 32)
(5, 'Lucy', 'female', 28)
(6, 'Rocky', 'male', 30)
(7, 'Gertrude', 'female', 53)
(8, 'Laertes', 'male', 26)
(9, 'Ophelia', 'female', 19)
(10, 'Polonius', 'male', 59)
(11, 'Horatio', 'male', 22)
[(1, 'Hamlet', 'male', 25), (2, 'Claudius', 'male', 55), (3, 'King Hamlet', 'male', 60), (4, 'Larry', 'male', 32), (5, 'Lucy', 'female', 28), (6, 'Rocky', 'male', 30), (7, 'Gertrude', 'female', 53), (8, 'Laertes', 'male', 26), (9, 'Ophelia', 'female', 19), (10, 'Polonius', 'male', 59), (11, 'Horatio', 'male', 22)]
>>> tryit('select * from person where age < 40')
fetchall: select * from person where age < 40
  1 Hamlet          male      25 
  4 Larry           male      32 
  5 Lucy            female    28 
  6 Rocky           male      30 
  8 Laertes         male      26 
  9 Ophelia         female    19 
 11 Horatio         male      22 
[(1, 'Hamlet', 'male', 25), (4, 'Larry', 'male', 32), (5, 'Lucy', 'female', 28), (6, 'Rocky', 'male', 30), (8, 'Laertes', 'male', 26), (9, 'Ophelia', 'female', 19), (11, 'Horatio', 'male', 22)]
>>> tryit('select * from person where age < 40 and age > 25')
fetchall: select * from person where age < 40 and age > 25
  4 Larry           male      32 
  5 Lucy            female    28 
  6 Rocky           male      30 
  8 Laertes         male      26 
[(4, 'Larry', 'male', 32), (5, 'Lucy', 'female', 28), (6, 'Rocky', 'male', 30), (8, 'Laertes', 'male', 26)]
>>> tryit('select * from person where age < 40 and age > 25' and gender = "male")
  File "<stdin>", line 1
SyntaxError: keyword can't be an expression
>>> tryit('select * from person where age < 40 and age > 25' and gender = "male"')
  File "<stdin>", line 1
    tryit('select * from person where age < 40 and age > 25' and gender = "male"')
                                                                                 ^
SyntaxError: EOL while scanning string literal
>>> tryit('select * from person where age < 40 and age > 25 and gender = "male"')
fetchall: select * from person where age < 40 and age > 25 and gender = "male"
  4 Larry           male      32 
  6 Rocky           male      30 
  8 Laertes         male      26 
[(4, 'Larry', 'male', 32), (6, 'Rocky', 'male', 30), (8, 'Laertes', 'male', 26)]
>>> fetchwherejoin(['name', 'gender', 'Likes'], [], [], [], 'person', 'like_table on person.id = like_table.Person_id')
SQL Command:  SELECT name, gender, Likes FROM person INNER JOIN like_table on person.id = like_table.Person_id
fetchall:
('Hamlet', 'male', 'fencing')
('Hamlet', 'male', 'philosophy')
[('Hamlet', 'male', 'fencing'), ('Hamlet', 'male', 'philosophy')]
>>> fetchwherejoin(['name', 'gender', 'Likes'], [], [], [], 'person', 'friends on person.id = friends.Person_id')
SQL Command:  SELECT name, gender, Likes FROM person INNER JOIN friends on person.id = friends.Person_id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/httpd/html/zoo/classes/cs200/materials/hws/.answers/hw6sqla.py", line 404, in fetchwherejoin
    cursor.execute(command)
sqlite3.OperationalError: no such column: Likes
>>> fetchwherejoin(['name', 'gender', 'Friend_id', 'Fname'], [], [], [], 'person', 'friends on person.id = friends.Person_id')
SQL Command:  SELECT name, gender, Friend_id, Fname FROM person INNER JOIN friends on person.id = friends.Person_id
fetchall:
('Hamlet', 'male', 11, 'Horatio')
[('Hamlet', 'male', 11, 'Horatio')]
>>> fetchwherejoin(['name', 'gender', 'Child_id', 'Cname'], [], [], [], 'person', 'children on person.id = children.Person_id')
SQL Command:  SELECT name, gender, Child_id, Cname FROM person INNER JOIN children on person.id = children.Person_id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/httpd/html/zoo/classes/cs200/materials/hws/.answers/hw6sqla.py", line 404, in fetchwherejoin
    cursor.execute(command)
sqlite3.OperationalError: no such column: children.Person_id
>>> fetchwherejoin(['name', 'gender', 'Child_id', 'Cname'], [], [], [], 'person', 'children on person.id = children.Parent_id')
SQL Command:  SELECT name, gender, Child_id, Cname FROM person INNER JOIN children on person.id = children.Parent_id
fetchall:
('King Hamlet', 'male', 1, 'Hamlet')
('Gertrude', 'female', 1, 'Hamlet')
('Polonius', 'male', 8, 'Laertes')
('Polonius', 'male', 9, 'Ophelia')
[('King Hamlet', 'male', 1, 'Hamlet'), ('Gertrude', 'female', 1, 'Hamlet'), ('Polonius', 'male', 8, 'Laertes'), ('Polonius', 'male', 9, 'Ophelia')]
>>> fetchwherejoin(['name', 'gender', 'Sibling_id', 'Sname'], [], [], [], 'person', 'siblings on person.id = siblings.person_id')
SQL Command:  SELECT name, gender, Sibling_id, Sname FROM person INNER JOIN siblings on person.id = siblings.person_id
fetchall:
('Claudius', 'male', 3, 'King Hamlet')
('Laertes', 'male', 9, 'Ophelia')
('King Hamlet', 'male', 4, 'Larry')
[('Claudius', 'male', 3, 'King Hamlet'), ('Laertes', 'male', 9, 'Ophelia'), ('King Hamlet', 'male', 4, 'Larry')]
'''
def tryit(command):
    pass

def fetchall(fields = [], table = 'person'):
    pass

def fetchwhere(fields = [], where = [], table = 'person'):
    pass

def fetchwherejoin(fields = [], where = [], sort = [], limit = [], table = 'person', join = []):
    pass



# ********************************************************

### test function from google python course
### =======================================
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if (hasattr(expected, '__call__')):
        OK = expected(got)
    else:
        OK = (got == expected)
    if OK:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('hours')
  print('# is it greater than 0?')
  test(hours(), lambda x: x > 0)

  test(fetchall([], 'person'), [(1, 'Hamlet', 'male', 25), (2, 'Claudius', 'male', 55), (3, 'King Hamlet', 'male', 60), (4, 'Larry', 'male', 32), (5, 'Lucy', 'female', 28), (6, 'Rocky', 'male', 30), (7, 'Gertrude', 'female', 53), (8, 'Laertes', 'male', 26), (9, 'Ophelia', 'female', 19), (10, 'Polonius', 'male', 59), (11, 'Horatio', 'male', 22)])

  test(tryit('select * from person where age < 40'), [(1, 'Hamlet', 'male', 25), (4, 'Larry', 'male', 32), (5, 'Lucy', 'female', 28), (6, 'Rocky', 'male', 30), (8, 'Laertes', 'male', 26), (9, 'Ophelia', 'female', 19), (11, 'Horatio', 'male', 22)])

  test(tryit('select * from person where age < 40 and age > 25'), [(4, 'Larry', 'male', 32), (5, 'Lucy', 'female', 28), (6, 'Rocky', 'male', 30), (8, 'Laertes', 'male', 26)])

  test(tryit('select * from person where age < 40 and age > 25 and gender = "male"'), [(4, 'Larry', 'male', 32), (6, 'Rocky', 'male', 30), (8, 'Laertes', 'male', 26)])

  test(fetchwherejoin(['name', 'gender', 'Likes'], [], [], [], 'person', 'like_table on person.id = like_table.Person_id'), [('Hamlet', 'male', 'fencing'), ('Hamlet', 'male', 'philosophy')])

  test(fetchwherejoin(['name', 'gender', 'Friend_id', 'Fname'], [], [], [], 'person', 'friends on person.id = friends.Person_id'), [('Hamlet', 'male', 11, 'Horatio')])
  
  test(fetchwherejoin(['name', 'gender', 'Child_id', 'Cname'], [], [], [], 'person', 'children on person.id = children.Parent_id'), [('King Hamlet', 'male', 1, 'Hamlet'), ('Gertrude', 'female', 1, 'Hamlet'), ('Polonius', 'male', 8, 'Laertes'), ('Polonius', 'male', 9, 'Ophelia')])

  test(fetchwherejoin(['name', 'gender', 'Sibling_id', 'Sname'], [], [], [], 'person', 'siblings on person.id = siblings.person_id'),  [('Claudius', 'male', 3, 'King Hamlet'), ('Laertes', 'male', 9, 'Ophelia'), ('King Hamlet', 'male', 4, 'Larry')])


if __name__ == '__main__':
     main()
