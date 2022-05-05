# LEARNINGS from Reuven

############################################
### Day 2: 21.01.2022
############################################
#Differences between FUNCTIONs and METHODS
from itertools import count
from operator import is_not
import random
random.randint(0, 100)  # this is a function, not a method -- but a function in a module

s='abcd'
s.upper() #method--> you cannot run upper without saying what it is connected to

# print is a function -- it doesn't belong to any object
print('Hello')

s = 'abcd'
x = s.upper()
y=s.upper

print(type(x), type(y))

#Like in mathematics: Difference between function_name() and function_name: function_name is really the function and function_name() is the output of the function
def hello():
    return f'Hello!'
x=hello #the function itself
x() #--> also output of fcuntion
y=hello() #the output of the function

s = 'abc'
if s.isdigit:   # no parentheses -- if is checking if s.isdigit is True -- and (almost) all objects are True!
    print('Yes, it contains only digits!')

#Argument types in Functions (arguments are values, parameters and variables)
# Difference: POSITIONAL and KEYWORD Arguments
def add(first, second):
    total=first+second
    print(total)

#get infos about function arguments
add.__code__.co_argcount
add.__code__.co_varnames  #also gives out total, as it is used within function

add(1,3) #positional
add(second=3,first=1 ) #KEYWORD
add(first=4, 3) #does not work as positional > keyword
add(4, second=3) #works

def add(a,b,c=7,d=10):  #define beforehand so  there is default value!  #but npn-default>default!!! (a=1, b=2, c,d) would not work
    return a+b+c+d

add(2,2,3) #works as for d there is default value, c is overwritten with 3

#WATCH OUT if using "append" or other CHNAGING methods
def add_one(x=[]):
    x.append(1)
    return x
add_one() #print this multiple times, the output will be different!
#Solution: 
def add_one(x=None):  
    if x is None:
        x = []    # this list is defined and assigned at RUN TIME, not compile time
    x.append(1)
    return x

## *ARGS ("Slat Args") --> Variable number of optional arguments

def add (*numbers): #name can be anything
    out=0
    for i in numbers:
        out+=i
    return out

add(2,3,4,523)

#what about lists?
x=[1,2,3]
add(x) #does not work as this is a list!!
#solution:
add(*x) # also add(*[1,2,3]) would work!
#same goes for dicts!
        #what if using *args AND Default Parameter?
        def myfunc(a, b=99, *args):
            return f'{a=}, {b=}, {args=}'

        myfunc(10, 20, 30, 40, 50)  #would kinda not work as it sets b=20!
        # there's no good solution!
        # except for... making b a *keyword-only parameter*
        # if the parameter appears *after* *args, it's keyword only
        def myfunc(a, *args, b=99):
            return f'{a=}, {b=}, {args=}'

        myfunc(10, 20, 30, 40, 50)

#unpacking
t=(1,2,3,4,5) #tuple
a,b, *all=t
print(all) ##gives back a list


 # **KWARGS  
    #always a DICT, takes all of the kexyword elemtents that no one else took (can be empty too), totally independant from *args
def myfunc(a, b, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'
myfunc(10,20) #works
myfunc(10, 20, 30) #does not work! As this is no kind of dict
myfunc(10, 20, x=100, y=200, z=[10, 20, 30]) #does WORK


myfunc(10, 20, a=100, b=200) #WHY NOT?? A is defined within function!!

#get single key,value pairs for the dict fro **kwargs
def write_config(filename, **kwargs):
    with open(filename, 'w') as f:        # open our file for writing
        for key, value in kwargs.items(): # go through each key-value pair
            f.write(f'{key}={value}\n')   # write the key-value pair with key=value to our file
            
write_config('config.txt', a=100, b=200, c=300) 
d= {'a':1, 'b':2, 'd':3}
write_config('config.txt',**d)   # d only does not work (note: this is overwriting the file!)

len(obj='abcd') #does not work as len is positional only!
help(len) ##--> defined by / --> positional only before /

#SCOPING : ORder of where are variables defined
# L=LOCAL
# E=Enclosing
# G= GLobal
# B=Builtin'
x=100
'x' in globals() #true
del(x)
'x' in globals() #false

x = 100
def myfunc():
    x = 200
    print(f'In myfunc, x = {x}') # is x local? YES, value is 200
print(f'Before, x = {x}')   # is x global? yes, 100
myfunc()
print(f'After, x = {x}') # is x global? yes, 100

x = 100

#####
#this example does not work with the function, as the function does not know x
x = 100
def myfunc():
    x += 1   #  same as x = x + 1  ##looks at the rifght side first (x+1)
    print(f'In myfunc, x = {x}') 
    
print(f'Before, x = {x}')   
myfunc()
print(f'After, x = {x}')     


# I prefer, if I really need to modify global variables from my function, to use the __main__ module
import __main__
x = 100
def myfunc():
    __main__.x = 200   # this means: assign to the global variable x!
    print(f'In myfunc, x = {x}') 
    
print(f'Before, x = {x}')   
myfunc()
print(f'After, x = {x}')     

#difference between operators + and append
xscalar=100
xlist=[1,2,3]

def myfunc(x1,x2):
    x1+=1
    x2.append(1)
    print(x1)
    print(x2)

myfunc(xscalar, xlist)  # does the function
print(xscalar)  #same as before
print(xlist) #changed also after function!!


#KEYWORDS reserved but some redefineable!
# certain words in Python are reserved, or "keywords"
# you cannot assign them a new value
while = 10

#Builtins namespace
#Many, many common names in Python aren't reserved keywords. They are defined in "builtins". There are only about 25 keywords; everything else is in builtins. For example:

#list
#dict
#int
#len
sum = 10 + 20 + 30
sum([10, 20, 30])  #OH NO! Now this doesnt work anymore"
del(sum)
#which builtins are there?
dir(__builtins__)


############################################
### Day 3: 28.01.2022
############################################

# in Lambda Functions: Only expressions -- no statements allowed. Which means: No def, if, for, while, etc.
#IF : The normal if is a statement, not an expression. So you cannot use if in a lambda body.
#But... there is an alternative version of if, which is an expression:
#RESULT_IF_TRUE if CONDITION else RESULT_IF_FALSE

#COMPREHENSIONS
#When to use Comprehensions? (As opposed to a regular for loop?)
"""I start with an iterable of some sort (i.e., an object that knows how to behave in a for loop)
I want to get a list back, based on that iterable
I can write a Python expression that describes the "mapping" from the first to the second
In contract to a loop it does not create new values when you do [i**2 for i in range(3)] for i"""

#Concat elements from a list by join --> only works for strings not integers!
mylist = [10, 20, 30]
'*'.join(str(elem) for elem in mylist)

s = '1 2 4 gg b 2 4'
sum([int(one_number)                #select
    for one_number in s.split()     #from
    if one_number.isdigit() ])      #where


#Exercises with Test Data set in git Repo
import os
os.getcwd()
os.chdir('C:\\Users\\sina.herbst\\Documents\\git_repositories\\Sinas-Repo\\advanced-exercise-files')

[int(numb) 
for numb in open('nums.txt')
if numb.strip().isdigit()]  #we need strip() which also works as a if function (in this example it could be only numb.strip())

#does not work!
[int(numb) 
for numb in open('nums.txt')
if numb.isdigit()]  #we need strip() to exclude whitespaces! As int(' ') = [] --> whereas int() =0

#we could also instead of if include the strip into the "from" part
sum([int(num)
     for num in open('nums.txt').read().split()])  # but we need read!!

[one_line
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith('#')     # you can have more than one "if" line .. they are "and"ed together
 if not one_line.startswith('\n')]

#fast way to create a dict from a list of 2 element tuples
mylist = [('a', 1), ('b', 2), ('c',3)]
dict(mylist)

from collections import Counter
c = Counter([one_line.split(':')[-1].strip()
         for one_line in open('linux-etc-passwd.txt')
         if not one_line.startswith(('#', '\n'))])

c.most_common() 

#Set Comprehension --> remember Sets are unique!
# let's get integers from the user and sum the *DIFFERENT* or *UNIQUE* numbers we got
s='1 3 5 1 1 3 3 3 3'
sum({int(one_number)
        for one_number in s.split()})  #the {} marks the set! 1+3+5=9

c=Counter()
from collections import Counter
Counter([oneline.split()[0] for oneline in open('mini-access-log.txt')]).most_common(5)

###########################
#DICT comprehension
words = 'this is a bunch of words for my Python course'
# I want a dict from this sentence, where the keys are words and the values are lengths of words

{part:len(part) for part in words.split()}
#alternative but the first is cooler!!
dict ([(part, len(part)) for part in words.split()])

#Create a dict whose keys are usernames and whose values are shells from linux-etc-passwd.txt.
{ oneline.split(':')[0] : oneline.split(':')[-1] 
for oneline in open('linux-etc-passwd.txt')}

#alternative
{fields[0] : fields[-1]
 for one_line in open('linux-etc-passwd.txt')
 if not one_line.startswith(('\n', '#'))
 if (fields := one_line.strip().split(':'))}  #this is always true but it moreover defines fields as this!!

 ##################
 # NESTED Comprehension
 mylist = [[10, 20, 30], [40, 45, 50, 55, 60], [65, 70, 75], [80, 85, 90, 95], [100, 115, 120]]
 # how can I create a single, flat list from mylist?
 [oneitem   for oneelement in mylist    
            for oneitem in oneelement  ] 

#turn two parts into dictionary! (also list possible!)
dict(zip('abc', [10, 20, 30]))

# each "for" can have a condition and thus stop the next phase from running
[one_item
 for one_sublist in mylist
 if len(one_sublist) > 3
 for one_item in one_sublist
 if one_item>45]

 [(x,y)
 for x in range(3)
 for y in range(3)]

'''
Control-a: start of line
Control-e: end of line
Control-k: delete to the end of the line'''
# bash is from the GNU folks, who make Emacs

# control-r means: search backwards in your shell history


############################################
### Day 4: 04.02.2022
############################################

#sorting
numbers=[-1, 47, 3, -45, -17, 15, 12, 1, 50, -12]

# list.sort (a) modifes the list, (b) returns None, (c) only works on lists
numbers.sort()  # this modifies the list in-place!  It returns None
# don't make this VERY VERY common mistake:
numbers = numbers.sort()  ##would return numbers = Nine!


# much better (and more modern) is to use the builtin function "sorted"
sorted(numbers)  # this returns a new list (always a list) based on the original values, sorted

#sort by absolute value?
sorted(numbers, key=abs)  #not abs() !!! can be any function or method i n python which return as comparable value 
words = 'This is a bunch of words for my Python course with Xing'.split()