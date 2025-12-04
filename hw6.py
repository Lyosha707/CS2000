#! /usr/bin/python3

# ********************************************************
# CS 200 HW #3  DUE Thursday, 2/20/2020 at 11:59 pm
#                via the submit system on the Zoo

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

# Reading: Learning Python, Chapters 26 - 32 
# Reading: Python Cookbook, Chapter 8
# Reading: UNIX principle 2

# ********************************************************
# ** problem 0 ** (1 easy point) 
# Replace the number 0 in the definition below to indicate
# the number of hours you spent doing this assignment
# Decimal numbers (eg, 6.237) are fine.  Exclude time
# spent reading.

def hours():
    return 0

# ********************************************************
# ** problem 00 ** (1 fairly easy point)

# Below is a UNIX transcript with one command replaced by XXXX

transcript = '''
bash-4.4$ ls
bash-4.4$ date 
Tue Jan 29 17:08:02 EST 2019
bash-4.4$ xxxx
bash-4.4$ cat file
Tue Jan 29 17:08:11 EST 2019
bash-4.4$ ls -l
total 0
-rw-rw-r-- 1 sbs5 sbs5 29 Jan 29 17:08 file
'''

# define xxxx below to be the correct UNIX command.

def xxxx():
    return "date > file"

# ********************************************************
# ** problem 1 ** (18 points)
# Define a person class

# The basic person has a name and gender.

## Example:

# hamlet = person('hamlet', 'male') => person('hamlet', 'male')
# repr(hamlet) => person('hamlet', 'male')
# str(hamlet) => '<Person Name: hamlet (1)>'

# where (1) indicates the count of person's created so far.
# That is, Hamlet was the first person.

## define the person class, its constructor method, and its
## repr and str print methods, per the following;

class person:

    count = 0

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        person.count += 1
        self.count = person.count
        self.likes = []
        self.friend = []
        self.siblings = []

    def __repr__(self):
        return f"person('{self.name}', '{self.gender}')"

    def __str__(self):
        return f"<Person Name: {self.name} ({self.count})>"

# ********************************************************
# ** problem 2 ** (15 points)
#  add a 'likes' attribute to the person class.

## this will require several steps:
# - modify the __init__() method to include likes
# - create an add_like() method for populating likes
# - create a pp() (pretty print) method for displaying a person's likes

# Examples:

# >>> hamlet.add_like('fencing')
# >>> hamlet.add_like('philosophy')
# >>> hamlet.add_like('fencing')
# >>> hamlet.pp()
# Person Name hamlet
#       Likes: ['fencing', 'philosophy']

# Note that when an item is already on the likes list, it is not repeated.

# ********************************************************
    def add_like(self, item):

        if item not in self.likes:
            self.likes.append(item)

    def pp(self):
        print("Person Name", self.name)

        if self.likes:
            print("        Likes:", self.likes)

        if self.friends:
            print("       Friends: ", self.friends)

# ********************************************************
# ** problem 3 ** (10 points)
#  add a 'friends' attribute to the person class.
#  note that this is reciprocal

# - modify the __init__() method to include friends
# - create an add_friend() method to add a friend
# - modify the pp() method to display friends, if present

# >>> horatio = person('horatio', 'male')
# >>> hamlet.add_friend(horatio)
# >>> hamlet.add_friend(horatio)  ## ignores repeated call
# >>> hamlet.pp()
# Person Name hamlet
#       Likes: ['fencing', 'philosophy']
#       Friends: [person('horatio', 'male')]
# >>> horatio.pp()
# Person Name horatio
#       Friends: [person('hamlet', 'male')]

## Note that pp() does not display any likes for horatio, since
## we have not defined any.  

# ********************************************************
    def add_friend(self, person):
        if other not in self.friends:
                self.friends.append(other)
        if self not in other.friends:
                other.friends.append(self)

# ********************************************************
# ** problem 4 ** (10 points)
#  add a 'siblings' attribute to the person class.
#  note that this is reciprocal

# - modify the __init__() method to include siblings
# - create an add_sibling() method to add a sibling
# - modify the pp() method to display siblings, if present

# Examples:

# >>> claudius = person('claudius','male')
# >>> kinghamlet = person('King Hamlet', 'male')
# >>> larry = person('larry', 'male')
# >>> kinghamlet.add_sibling(claudius)
# >>> kinghamlet.add_sibling(larry)
# >>> claudius.pp()
# Person Name claudius
#       Siblings: [person('King Hamlet', 'male')]
# >>> kinghamlet.pp()
# Person Name King Hamlet
#       Siblings: [person('claudius', 'male'), person('larry', 'male')]

## Recent scholarship has discovered another brother: Larry
## However, we may not infer that Larry is also the brother of Claudius.

# ********************************************************
    def add_sibling(self, person):
        pass

# ********************************************************
# ** problem 5 ** (15 points)
#  add 'parent' and 'children' attributes to the person class.
#  note that these are reciprocal

# - modify the __init__() method to include parents and children
# - create an add_parent() method to add a parent
# - create an add_child() method to add a child
# - modify the pp() method to display parents and children, if present

# Examples:

# >>> gertrude = person('gertrude', 'female')
# >>> hamlet.add_parent(gertrude)
# >>> hamlet.add_parent(kinghamlet)
# >>> hamlet.pp()
# Person Name hamlet
#       Likes: ['fencing', 'philosophy']
#       Friends: [person('horatio', 'male')]
#       Parents: [person('gertrude>, person('King Hamlet', 'male')]
# >>> gertrude.pp()
# Person Name gertrude
#       Children: [person('hamlet', 'male')]
# >>> kinghamlet.pp()
# Person Name King Hamlet
#       Siblings: [person('claudius', 'male'), person('larry', 'male')]
#       Children: [person('hamlet', 'male')]


# ********************************************************
    def add_parent(self, person):
        pass

    def add_child(self, person):
        pass

# ********************************************************
# ** problem 6 ** (10 points)
#  add methods to display a person's father or mother

# a mother is a female parent
# a father is a male parent

# You don't need to modify the __init__() method.
# write mother() and father() methods which return the 
# respective people, if present.
# modify the pp() method to show mothers and fathers if present

# Examples:

# >>> hamlet.pp()
# Person Name hamlet
#       Likes: ['fencing', 'philosophy']
#       Friends: [person('horatio', 'male')]
#       Parents: [person('gertrude>, person('King Hamlet', 'male')]
#       Father: person('King Hamlet', 'male')
#       Mother: person('gertrude', 'female')

# ********************************************************
    def mother(self):
        pass

    def father(self):
        pass

# ********************************************************
# ** problem 7 ** (10 points)
#  add methods to display a person's uncles and aunts

# an aunt is a parent's female sibling
# an uncle is a parent's male sibling

# You don't need to modify the __init__() method.
# write uncle() and aunt() methods which return the 
# respective people, if present.
# modify the pp() method to show uncles and aunts if present

# Examples:

# >>> hamlet.pp()
# Person Name hamlet
#       Likes: ['fencing', 'philosophy']
#       Friends: [person('horatio', 'male')]
#       Parents: [person('gertrude>, person('King Hamlet', 'male')]
#       Father: person('King Hamlet', 'male')
#       Mother: person('gertrude', 'female')
#       Uncles: [person('claudius>, person('larry', 'male')]

# ********************************************************
# ** problem 8 ** (10 points)
#  add methods to display a person's sons and daughters

# a daughter is a person's female child
# a son is a person's male child

# You don't need to modify the __init__() method.
# write son() and daughter() methods which return the 
# respective people, if present.
# modify the pp() method to show sons and daughters if present

# Examples:

# >>> laertes = person('laertes', 'male')
# >>> ophelia = person('ophelia', 'female')
# >>> polonius = person('polonius', 'male')
# >>> laertes.add_sibling(ophelia)
# >>> ophelia.add_parent(polonius)
# >>> laertes.add_parent(polonius)
# >>> polonius.pp()
# Person Name polonius
#       Children: [person('ophelia', 'female'), person('laertes', 'male')]
#       Sons: [person('laertes', 'male')]
#       Daughters: [person('ophelia', 'female')]


# ********************************************************
    def son(self):
        pass

    def daughter(self):
        pass


# ********************************************************
# ********************************************************

class person:
    ''' Class for person, including friends and relatives.'''
    
    count = 0

    def __init__(self, name, gender):
        ''' Constructor for person(name, gender) '''
        self.count = self.__class__.count
        self.__class__.count += 1
        self.name = name
        self.gender = gender
        self.likes = []
        self.friends = []
        self.children = []
        self.siblings = []
        self.parents = []
        

    def __repr__(self):
        ''' return string that can be evaluated to recreate this instance. '''
        return "person('{self.name}', \'{self.gender}\')".format(self=self) 
        # return 'person({}, {})'.format(repr(self.name), repr(self.gender))

    def __str__(self):
        ''' String representation of person.  '''
        return "<Person Name: {} ({})>".format(self.name, self.count)
    def pp(self):
        ''' Pretty print person. '''
        p = "Person Name " + self.name
        if self.likes:  p += "\n\tLikes: " + str(self.likes)
        if self.friends:    p += "\n\tFriends: " + str(self.friends)
        if self.siblings:   p += "\n\tSiblings: " + str(self.siblings)
        if self.parents:    p += "\n\tParents: " + str(self.parents)
        if self.children:   p += "\n\tChildren: " + str(self.children)
        if self.father():   p += "\n\tFather: " + repr(self.father())
        if self.mother():   p += "\n\tMother: " + repr(self.mother())
        if self.uncle():   p += "\n\tUncles: " + str(self.uncle()) 
        if self.aunt():   p += "\n\tAunts: " + str(self.aunt())    
        if self.son():   p += "\n\tSons: " + str(self.son()) 
        if self.daughter():   p += "\n\tDaughters: " + str(self.daughter()) 
        return (p)
        
    def add_like(self,item):
        ''' Add like to list without duplication. '''
        if item not in self.likes:
            self.likes.append(item)

    def add_friend(self,item):
        ''' Add friend to list without duplication. Make reciprocal. '''
        if item not in self.friends:
            self.friends.append(item)
            item.add_friend(self)
    
    def add_sibling(self,item):
        ''' Add sibling to list without duplication.  Make reciprocal. '''
        if item not in self.siblings:
            self.siblings.append(item)
            item.add_sibling(self)        
  
    def add_parent(self, item):
        ''' Add parent to list without duplication.  Add child to parent. '''
        if item not in self.parents:
            self.parents.append(item)
            item.add_child(self) 
    def add_child(self, item):
        ''' Add child to list without dulication.  Add parent to child. '''
        if item not in self.children:
            self.children.append(item)
            item.add_parent(self) 
  
    def father(self):
        ''' Get father (male parent). '''
        for p in self.parents:
            if p.gender == 'male':
                return p
        return None       

    def mother(self):
        ''' Get mother (female parent). '''
        for p in self.parents:
            if p.gender == 'female':
                return p
        return None  

    def uncle(self):
        ''' Get uncles (male siblings of parent). '''
        u = []
        for p in self.parents:
            for s in p.siblings:
                if s.gender == 'male':
                    u.append(s)
        return u       

    def aunt(self):
        ''' Get aunts (female siblings of parents). '''
        a = []
        for p in self.parents:
            for s in p.siblings:
                if s.gender == 'female':
                    a.append(s)
        return a
    
    def son(self):
        ''' Get sons (male children). '''
        s = []
        for p in self.children:
            if p.gender == 'male':
                s.append(p)
        return s
    
    def daughter(self):
        ''' Get daughters (female children) '''
        d = []
        for p in self.children:
            if p.gender == 'female':
                d.append(p)
        return d



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

  print ('xxxx')
  test(xxxx(), "cannot test without giving it away")

  print ('person class')
  hamlet = person('hamlet', 'male')
  test(repr(hamlet), "person('hamlet', 'male')")
  test(str(hamlet), "<Person Name: hamlet (0)>")

  print ('add_like')
  hamlet.add_like('fencing')
  hamlet.add_like('philosophy')
  hamlet.add_like('fencing')
  test(hamlet.pp(), "Person Name hamlet\n\tLikes: ['fencing', 'philosophy']")

  print ('add_friend')
  horatio = person('horatio', 'male')
  hamlet.add_friend(horatio)
  hamlet.add_friend(horatio)  ## ignores repeated call

  test(hamlet.pp(), "Person Name hamlet\n\tLikes: ['fencing', 'philosophy']\n\tFriends: [person('ho>

  test(horatio.pp(), "Person Name horatio\n\tFriends: [person('hamlet', 'male')]")

  print ('add_sibling')
  claudius = person('claudius','male')
  kinghamlet = person('King Hamlet', 'male')
  larry = person('larry', 'male')     
  lucy = person('lucy', 'female')
  rocky = person('rocky', 'male')
  gertrude = person('gertrude', 'female')
  laertes = person('laertes', 'male')
  ophelia = person('ophelia', 'female')
  polonius = person('polonius', 'male')

  hamlet.add_sibling(rocky)
  rocky.add_parent(gertrude)
  polonius.add_sibling(lucy)
  kinghamlet.add_sibling(claudius)
  kinghamlet.add_sibling(larry)
  test(claudius.pp(), "Person Name claudius\n\tSiblings: [person('King Hamlet', 'male')]")
  test(kinghamlet.pp(), "Person Name King Hamlet\n\tSiblings: [person('claudius', 'male'), person('>

  print ('add_parent')
  print ('add_child')
  print ('mother')
  print ('father')
  print ('aunt')
  print ('uncle')
  print ('son')
  print ('daughter')

  hamlet.add_parent(gertrude)
  hamlet.add_parent(kinghamlet)
  test(hamlet.pp(), "Person Name hamlet\n\tLikes: ['fencing', 'philosophy']\n\tFriends: [person('ho>

  test(gertrude.pp(), "Person Name gertrude\n\tChildren: [person('rocky', 'male'), person('hamlet',>

  test(kinghamlet.pp(), "Person Name King Hamlet\n\tSiblings: [person('claudius', 'male'), person('>

  laertes.add_sibling(ophelia)
  ophelia.add_parent(polonius)
  laertes.add_parent(polonius)
  test(polonius.pp() ,"Person Name polonius\n\tSiblings: [person('lucy', 'female')]\n\tChildren: [p>

  print("this is a test of the person class")
  cast = [hamlet, laertes, gertrude, ophelia, polonius, horatio, kinghamlet, larry, lucy, rocky]
  for x in cast: print(x.pp())

hamlet = person('hamlet', 'male')
hamlet.add_like('fencing')
hamlet.add_like('philosophy')
hamlet.add_like('fencing')
horatio = person('horatio', 'male')
hamlet.add_friend(horatio)
hamlet.add_friend(horatio)## ignores repeated call
claudius = person('claudius','male')
kinghamlet = person('King Hamlet', 'male')
larry = person('larry', 'male') 
lucy = person('lucy', 'female')
rocky = person('rocky', 'male')
gertrude = person('gertrude', 'female')
laertes = person('laertes', 'male')
ophelia = person('ophelia', 'female')
polonius = person('polonius', 'male')
hamlet.add_sibling(rocky)
rocky.add_parent(gertrude)
polonius.add_sibling(lucy)
kinghamlet.add_sibling(claudius)
kinghamlet.add_sibling(larry)
hamlet.add_parent(gertrude)
hamlet.add_parent(kinghamlet)
laertes.add_sibling(ophelia)
ophelia.add_parent(polonius)
laertes.add_parent(polonius)
cast = [hamlet, laertes, gertrude, ophelia, polonius, horatio, kinghamlet, larry, lucy, rocky]
for x in cast: print(x.pp())


if __name__ == '__main__':
     main()
