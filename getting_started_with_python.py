#shortcuts:
#execute marked lines: hochstelltaste+enter
#auskommentieren mehrerer ausgewählter zeilen: Ctrl + K then press Ctrl + C

a=1
print(a)
print ("a is =" + str(a))
a+=1
print("Now a is =" + str(a))

b=3**a
print(b)

#modulo
print(20//6) #6 goes 3 times into 20
print(20 % 6) #rest 2

#neutralizing elements in strings
print("He\\She is")

#lines
print("starting \n a \n new \n line")

print("spam" *3)

#input functions -> prompts the user for input and returns what they enter as a string
name=input("Enter your name: ")
print("Hello, " + name)

#walrus operator ->assigning variabels within an expression
print(num:=input("Write your input "))


##Boolean
print(2==3) #False!
print(2!=3) #True

##if loops-> By indents!
if 10>5 :
    print("10 is greater than 5")

if 1>2:
    print ("Greater")
else:
    if 1==2:
        print("equal")
    else:
        if 1<2:
            print("smaller")
        else:
            print("Not comparible")

#shorter : Elif
if 1>2:
    print ("Greater")
elif 1==2:
    print("equal")
elif 1<2:
    print("smaller")
else:
    print("Not comparible")

#NOT -> Contrast / Contrary
if not 1>2:
    print ("not greater")

#######################
# Lists
#########################
#Typically, a list will contain items of a single item type, but it is also possible to include several different types.
words = ["Hello", "world", "!"]  
print(words[0])

#Lists can also be nested within other lists.
number=3
things=["string", 0, [1,2,number], 4.56]
print(things[2])
print(things[2][2])

matrix=[
    [1,2,3],
    [4,5,6]
]

#reassigning
nums=[7,7,7]
nums[2]=8
#nums[3]
print(nums)

words=["a", "b", "c"]
if "c" in words:
    print ("yes")
else:
    print("no")

#list functions --> use with object.function
nums=[1,2,3]
nums.append(4)
len(nums)
nums.insert(0,0) #inserts at index 0 a 0 
print(nums)
print(nums.index(2)) #returns the index where the item is stored within the list
#strip -> remove spaces at beginning and end -> reasonable if you read lines into a list 
words=[" lala ", " huhu ", "kein space nur innen"]
for i in words:
    j=i.strip()
    print(len(j))

#list slices
nums=[1,2,3,4,5,6,7]
slices=nums[3:5]
print(slices)
slices2=nums[:5] 
slices3=nums[:4:2] #everything until exclude 4th element in 2er steps
print(slices3)
print(nums[1:-1]) #righter end is counted backwards meaning we go from 7 one step to left left to 6


#other functions
max(nums) #: Returns the list item with the maximum value
min(nums) #: Returns the list item with minimum value
nums.count(2)#: Returns a count of how many times an item occurs in a list
nums.remove(2)#: Removes an object from a list
nums.reverse()#: Reverses items in a list.

#################
#split--> creates a list
###################
txt = "welcome to the jungle"
x = txt.split('to')
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

#include split parameter delimeter
text='<html><head>'
d='>'
d2=text.split(d)
s =  [e+d for e in text.split(d) if e]
s2 =  [e+d for e in text.split(d)]
#s=text.split('>')
print(s)
print(s2)



################
#while loops
#############
i=1
while i<=5:
    i=i+1
    print(i)

#break -> break the while loop
i = 5
while True: #would go on forever
  print(i)
  i = i - 1
  if i <= 2:
    break

#for loops
letters = ['a', 'b', 'c']

for l in nums:
    print(l)

#range #rcreates (a list) automatically range(start, end, step size)
numbers=list(range(4,14,2))
print(numbers)
number


#functions
def my_func():
    print("hello")

my_func()

#with arguments
def plus_func(variable):
    variable +=1
    return variable

print(plus_func(4))


def maxfun(x,y):
    if x>y:
        return x
    else:
        return y

print(maxfun(3,4))


#functions as input arguments of functions
def add (x,y):
    return x+y

def do_twice(func, x, y):
    return func(func(x,y), func(x,y))

a=5
b=10
print(do_twice(add, a,b))




#everything after return will be ignored
def add_numbers(x,y):
    total=x+y
    return total
    print("This wont be printed")

print(add_numbers(4,5))


#docstrings for comments
def shout(word):
    """
    Print a word with an 
    exclaimation mark following it.
    """
    print(word + "!")

shout("spam")


#modules : Import code that others have created (like packages!)
#not all moduls had to be installed beforehand!
import random
for i in range(5):
    value=random.randint(1,6) #prints 5 random integer values between 1 and 6
    print(value)

#you can also import parts og the modeuls
from math import pi, sqrt
print (pi)

"""
Preinstalles Modules are called the standard library,
 and contains many useful modules. Some of the standard library's:
 string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.
 """

#PIP
 """
 Many third-party Python modules are stored on the Python Package Index (PyPI).
The best way to install these is using a program called pip. This comes installed by default with modern distributions of Python.
 If you don't have it, it is easy to install online. Once you have it, installing libraries from PyPI is easy. 
 Look up the name of the library you want to install, go to the command line (for Windows it will be the Command Prompt), 
 and enter "pip install library_name". Once you've done this, import the library and use it in your code.

Using pip is the standard way of installing libraries on most operating systems, but some libraries have prebuilt binaries for Windows.
 These are normal executable files that let you install libraries with a GUI the same way you would install other programs.

 """





#Exceptions: Error Handling
# TRY FUnction :
#""" 
#The try block contains code that might throw an exception. 
#If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. If no error occurs, the code in the except block doesn't run.
#"""

try:
    num1=7
    num2=0
    print(num1/num2) #not possible-> division by Zero
    print("Done Calculation")
except ZeroDivisionError:
    print("An Error occurred")
    print("due to zweo division")


print(10/2)
print("a")


#several exceptions (except withaout any speficifed exceptions will catch all errors)
try:
    variable=10
    print(variable +  "hello")
    print(variable /2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError): #several Error Occurences
    print("Error occured")

#finally
try: 
    print("Hello")
    print(1/0)
except:
    print("error")
finally:
    print("This will run no matter what")



try:
  print(1 / 0)
except ZeroDivisionError:
  raise ValueError

########
#assertion -> opposite of exception --> Only executes following commands if assert is true. But only works in separate files, as in VS Code it is executed everything separately
#######
print(1)
assert 2+2==4
print(2)
assert 1+1==3
print(3)


#assert with multiple arguments
temp=-10
assert (temp>=0), "Colder than absolute Zero!"

#################################
#opening files and set working directory , get working directory --csv
#################################
import os
os.getcwd()
os.chdir('Documents\-Kopie auf Festplatte\python') # Copy "relative Pfad" by clicking on the folderon the left
#os.path.realpath(__file__)
myfile = open("testfile.txt","r")#-> Have to be in the correct directory , without "r" not possible to use read() function
a=list(myfile) #store file data in a list
a2 = myfile.read()
myfile.close()

#different read modes -> binary mode for non-text files (such as image and sound files).
# write mode
open("testfile.txt", "w")
# read mode
open("testfile.txt", "r")
open("testfile.txt")
# binary write mode -> 
open("testfile.txt", "wb")

file = open("testfile.txt", "r")
for i in range(21):
  print(file.read(4)) # this command gets the following letters unless the file is closed!
file.close()

#After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.
file = open("testfile.txt", "r")
file.read()
print("Re-reading") 
print(file.read())  #-> gives no output!
print("Finished")
file.close()

#readlines for getting lines
file = open("testfile.txt", "r")
print(file.readlines())
file.close()

#write in file
myfile=open("testfile.txt", "w")
amount_written=myfile.write("Mit Python hinzugefügt") #überschreibt aber bisherigen Inhalt! Selbst ohne write Befehl wird durch "w" das file mit Leerem Inahlt überschrieben
myfile.close()
print(amount_written)

myfile=open("testfile.txt", "w")
#myfile.write("Mit Python hinzugefügt") #überschreibt aber bisherigen Inhalt! Selbst ohne write Befehl wird durch "w" das file mit Leerem Inahlt überschrieben
myfile.close()

myfile=open("newfile.txt", "w")
myfile.write("Dieses File wurde komplett mit Python erstellt")
myfile.close()


#####################
#dictonaries
######################

#Dictionaries are data structures used to map arbitrary keys to values.
#Lists can be thought of as dictionaries with integer keys within a certain range.
ages={"Dave": 24, "Mary" : 42, "John": 13}
print(ages["John"])

squares={1:1, 2:4, 3:"error", 4:16}
squares[8]=64 # new assignments

# use " in / not in function" for dictionaries
nums={
    1: "one",
    2: "two", 
    3: "three"
}
print(1 in nums) # --> boolean!
print ("one" in nums) # --> False!

#get function : similar to "index" but also works if entry is not in dictionary (not for lists!!)
print(nums.get(2)) # --> returns the value for key "2"
print(nums.get(4, "not in nums dict")) # argument what is hapenning if key is not in dict

#############################
#tuples -> ~immutable (unchangable) lists butadvantage: They are faster as lists
########################
#attention: are defined with () brackets
tuples=("a", "b", "c")
print(tuples[1]) # calling arguments
tuples[1]="geht nicht weil immutable"
tuple2="one", "two", "three" # also work without brackets
tuple2[1]


##################################
#list comprehension
##########################
listc=[i*3 for i in range(5)]
print(listc)
a = [i for i in range(20) if i%2==0]#get even numbers

#strin formatting ---> to embed non-string within strings---> uses a string's format methode to subsitia a number of arguments in the string
nums=[4,5,6]
#"string".function()
msg="Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2]) #the strucutre is as in list.append --> string.format!!!
print(msg)

        msg2="Numbers: {0} {1} {2}"  #just the string snippet!
        print(msg2)

        msg3="Numbers: {0} {1} {2}". format(nums[0], nums[1]) # does not work
        print(msg3)

        msg4="{0} {1} {0}". format(nums[1], nums[0]) # does work! {0}:=nums[1], {1}:=nums[0] # we dont need the "Numbers"!
        print(msg4)

        msg5="Numbers: {1} {2} {2}". format(nums[1], nums[0]) # doesnot work! counter always starts at 0 and the place {2} is not defined
        print(msg5)

        msg5="Numbers: {1} {1} {1}". format(nums[1], nums[0]) # does  work! counter always starts at 0 which neednt be defined
        print(msg5)

#also with commata , points, etc and with ###NAMED ARGUMENTS###
a="{x}, {y}".format(x=5, y=12) 
print(a)
#
a="{x}. {y}".format(nums[0], y=12) 
print(a)


#itertools (for list bspw)
#standard library with functions , for example infinite iterators
#for example: count->counts up infitely from a value. CYCLE infinitely iterators though a iterable (listor string)
#repeat repeats an object either inf. or specifi number of times
from itertools import count, accumulate, takewhile, chain, product, permutations
for i in count(3):
    print(i)
    if i>=11:
        break

nums =list(accumulate(range(8)))
print(nums)

nums2 =list(chain(range(8)))
print(nums2)
print(list(takewhile(lambda x:x<=6, nums)))

letters=("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

#######################################
#SETS       (similar to lists,  or dictionaries)
#######################################
#there are two ways to create sets!!
#way1
num_set={1,2,3,4,5}
word_set2={"test", "if", "this", "also", "works"}
#way2
word_set = set(["spam", "eggs", "sausage"])
print(3 in num_set)
print("spam" not in word_set)
print("also" in word_set2)
#Attention: to Create empty set it only works set() , not {} as {} defines empty dictionary!

    #Differences to Lists:
    # Unordered -> cant be indexed
    #distinct (as in mathematics!!!)
    #therefore we can use mathematical operations!
    first={1,2,3}
    second={3,4,5}
    print(first | second) #-> union of sets
    print(first&second) #-> intersection
    print(first-second) # -> difference
    print(first ^ second) #symmetric difference =first |second -first &second
    #faster as list (for echking if element is contained)
    #instead of "append" --> add
    nums={1,2,3,4,5}
    nums.add(6)
    nums.remove(1)
    print(nums)

#Altogether:
#  data structures: lists, dictionaries, tuples, sets.

# When to use a dictionary:
# - When you need a logical association between a key:value pair.
# - When you need fast lookup for your data, based on a custom key.
# - When your data is being constantly modified. Remember, dictionaries are mutable.

# When to use the other types:
# - Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
# - Use a set if you need uniqueness for the elements.
# - Use tuples when your data cannot change.


################################
#useful string functions
#######################
    #######
    #string functions
    #######################
#join (join strings)
print(", ".join(["this", "is", "join"]))
a=", ".join(["testing", "this", "without", "separator"])
#replace 
print("to be replaced".replace("to be", "is"))
#startswith/ endswith
print("starts test".startswith("starts"))
#lower/upper
print("This WILL be LowerED".lower())
#split
print("this will be splitted. second line".split(". "))

    #######
    #numeric functions --works for lists and numbers
    #######################
##min /max
print(min(1,2,3,4,5,0,-1))
print(min([1,2,3,4,5,0,-1]))
#abs
print(abs(-99))
#sum
print(sum([-1,3,5,-31]))

    #######
    #list functions --works for lists
    #######################
 nums=[55,212,431,121,4]
 #print([i>5 for i in nums])
#all
if all ([i>5 for i in nums]): #creates a new list with booleans: [true, true, true, true, false] and if all(true.., false)=false
     print("All larger than 5")   
else: 
    print("not all larger than 5")
#any
if any ([i>5 for i in nums]): #creates a new list with booleans: [true, true, true, true, false] and if all(true.., false)=false
     print("All larger than 5")   
else: 
    print("not all larger than 5")

#enumerate  #> prints arguments in list but with number
for v in enumerate(nums):
    print(v)




###################################################
#Lambdas
#creating fucntions "on the fly"-> functions created this way areknown as anonymous
#not as powerful as named functions-> can only do things that require a single expression
#################################################
#lambda functions can be assignted tovariables and used like normal functions
double=lambda x: x*2
print(double(7))

# example
print((lambda x: x**2+5*x+4)(-4)) #first entry defined the fucntion



#map and filter --> combination of function and  lists / iterables
def add_five(x):
    return x+5
nums=[11,22,33,44,55]
result=map(add_five,nums) #map takes a function and an list/iterable as arguments and reteruns a new list/iteralble with the function applied to each argument
result2=list(result)
print(result2)

lambda_variant=lambda x: x+5
print(list(map(lambda_variant,nums)))


#filter
nums=[11,22,33,44,55]
res=list(filter(lambda x: x%2==0,nums)) #remove what doesnt match the condition
print(res)

#Generators -> like lists or tuples
#Dont allow indexing with arbitrary indices, but they can still be iterated through with for loops
#dont have the memory restructions of lists --> can be infinite
#allow to declare a functon that behaves like an interaotr -> can be used in a for loop
def countdown():
    i=5
    while i>0:
        yield i #to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables
        i-=1
for i in countdown():
    print(i)

#can be converted in lists
def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(numbers(11)))


#Summary: Lists, Tuples, Dictionaries, Generators, iterables
#lists
lists=[1,2,3,4,5]
tuples=(1,2,3,4,5)
dictionaries={"a": 1, "b":2}
sets={1,2,3,4,5}
#generators=


#Decoratos-> modify funcitons using other functions, f.e. when you need to extend the functionality of cuntions that dont want to modify
def decor (func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap

def decor2 (func):
    print("=========")
    func()
    print("=========")

def print_text():
    print("Hello world!")

decorated=decor(print_text)
decorated()
# difference without extrawrap function -> directly printed with decorated
##difference between return and print in a function: rprint prints it directly (doesnt need a "print" fucntion when laterwards called the function)
decorated=decor2(print_text)
decorated()
#We can decorate our function by replaying the variable containing the function with a wrapped version
print_text=decor(print_text)
print_text()
#---> Python provides support to wrap a function in a decorator by pre-pendng the function definition with a decorator name and the @symbol
@decor
def print_text():
    print("Hello world!")
##->
print_text()

#############
#Recursion functions
##############
def factorial(x):
    if x==1:  #always write down the BASE CASE! Otherwise runtime error!
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))


def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))



################################################
#Object orientated programming (OOP)
###########################################
#Objects are created using classes--> focal pont of OOP
#Class describes that the object will be, separated from the object iself
"""
In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects.
""""

class Cat:
    # The __init__ method is called the class constructor.
  def __init__(self, color, legs): #All methods must have self as their first parameter. 
      # Python adds the self argument to the list for you; you dont need to include it when you call methods. Within a method definition, self refers to the instance calling the method.
    self.color = color 
    self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

####without init functioN?
class Cat2:
    # The __init__ method is not mandatory, only needed when characteristics of element is to be defined
    def do_st(self):
        print("works without an init function")

print(Cat2)

felix = Cat2()
felix.do_st()
Cat2().do_st() #getting the method without using an element in the class


"""
the init method  is called when an instance (object) of the class is created, using the class name as a function.
"""
print(type(felix))

class Dog:
    def __init__(self, name, color):
        self.name=name
        self.color=color
    #classes can have other methods defined to add functionality to them
    def bark(self):
        print("Woof")

fido=Dog("Fido", "brown")
print(fido.name)
fido.bark()

#Trying to access an attribute of an instance that isn't defined causes an AttributeError. This also applies when you call an undefined method.

"""
Inheritance provides a way to share functionality between classes.
For example Cat and Dog have similiar properties. This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
"""
class Animal: #"superclass"
    def __init__(self, name, color): #the init function is not mandatory, only needed when 
        self.name=name
        self.color=color

    def noise(self):
        print("I am an animal")
    def bark(self):
        print("this will be overwritten with the other bark unless its no dog")

class Cat(Animal): #"subclass"
    def purr(self):
        print("Purrrrr")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")


fido=Dog("Fido", "brown")
Luna=Cat("Luna", "black")
print(fido.color)
fido.noise()
fido.bark()
Luna.bark() #does work!



class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam() #inheritance related function refers to parent class -> to find the method with a certain name in an objects superclass

B().spam()

#########################
##Magic Methods / Dunders
#######################
# like __<magic method>__
# are used to create functionality that cant be represented as a normal method
# "Operator overloading" --> defining operators for custom classes that allow operators such as + and * to be used on them 

#Example: __add__ for +
class Vector2D:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def __add__(self, other): ##defines what happens when I use + for 2 elements: first+second
        return Vector2D(self.x+other.x, self.y+other.y) #defines new element in vecotr2d

first=Vector2D(5,7)
print(first.x)
second=Vector2D(3,9)
print(second.y)
result=first+second
print(result.x)
print(result.y)

class test_multiply:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def __add__(self, other): ##defines what happens when I use + for 2 elements: first+second
        return Vector2D(self.x*other.x, self.y*other.y) #defines new element in vecotr2d

first2=test_multiply(5,7)
second2=test_multiply(3,9)
result2=first2+second2
print(result2.x)

"""
More Magic Methods:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.

for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

for making classes act like containers
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
__call__ for calling objects as functions
__int__, __str__ -for converting the type
 __repr__ magic for string representation of the instance.

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.

"""

#example
class SpecialString:
    def __init__ (self, cont):
        self.cont=cont

    def __truediv__(self, other):
        line= "=" *len(other.cont)
        return "\n".join([self.cont, line, other.cont])  ##"\n".join (..) means join with new line"
        #return self.cont + other.cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result=other.cont[:index] + ">"+self.cont
            result += ">" +other.cont[index:]
            print(result)

spam = SpecialString("spam")
hello=SpecialString ("Hello world!")
eggs=SpecialString("eggs")
print(spam / hello)
spam>eggs

#example 2
import random
class Vaguelist:
    def __init__(self, cont):
        self.cont=cont
    def __getitem__(self, index):
        return self.cont[index+random.randint(-1, 1)]
    def __len__(self):
        return   len(self.cont)#random.randint(0, len(self.cont)*2)

test=Vaguelist("test")
print(len(test))
vague_list=Vaguelist(["A", "B", "C", "D"])
print(len(vague_list))  #using __len__
print(vague_list[2]) #using getitem




##########
#Class methods
#################
"""until now: methods are called by an instance of a class which is then passed to the self paaramter
Class methods: called by a class, which is passed to the cls parameter
common use: factory methids -> instantiate an instance of a slass usin different parameters than those usually passed to the class contruscotr

Are markt with a classmethod decorator"""

class Rectangle:
   def __init__(self, width, height):
      self.width=width
      self.height=height
   def calculate_area(self):
      return self.width *self.height
   
   @classmethod
   def new_square(cls, side_length):
      return cls(side_length, side_length) ##ruft die obige initiale funktion wieder auf?

square=Rectangle.new_square(5)
print(square.calculate_area())



class Rectangle:
   def __init__(self, width, height):
      self.width=width
      self.height=height
   def calculate_area(self):
      return self.width *self.height
   
square=Rectangle(5,3)
square.calculate_area()
print(square.calculate_area())


######################
#Static methods
#####################
"""Simiar to class methods except they dont receive additional arguemnts -> identical to normal functions that belont to a class
Market with "staticmethod decorator"

"""
class Pizza:
   def __init__(self, toppings):
      self.toppings=toppings

   @staticmethod
   def validate_topping(topping):
      if topping=="pineapple":
         raise ValueError ("No pineapples!")
      else:
         return True

ingredients=["cheese", "onions", "spam"]
if all (Pizza.validate_topping(i) for i in ingredients):
   pizza=Pizza(ingredients)

#Properties
"""
a way of customizing access to instance attributes.
@Property: which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
One common use of a property is to make an attribute read-only.

Can also be set by defining setter/getter functions
setter: set value
getter: gets value

"""

class Pizza:
   def __init__(self, toppings):
       self.toppings=toppings

    @property
    def pineapple_allowed(self):
        return False

pizza=Pizza(["tomato", "cheese"])
print(pizza.pineapple_allowed)



###############################################
#Regular Expressions   --    string manipulation
#########################################
"""
Language: Domain specific language (DSL) --> present in most modern programming languages (not only python)
Main tasks:
1. string match a pattern? (for example, is it email adress?
2. substitutions in a string
"""
#re.match to see if it matches the beginnin of a string
import re 
pattern= r"spam"  #to avoid confusion, we use raw strings as r"expression"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No Match")


if re.match(pattern, "eggsmamsausagespam"):
    print("Match")
else: 
    print ("No match")

if re.search(pattern, "eggsmamsausagespam" ): #finds match anywhere in the string
    print("Match")
else: 
    print ("No match")

print(re.findall(pattern,  "eggsmamsausagespam" )) #returns list of all substrings that patch the pattern
print(re.findall(pattern,  "spamspamsspa" ))
if re.finditer(pattern,  "eggsmamsausagespam" ): #does the sam as findall, but returns an iterator
    print("match")
else:
    print("no match")

#severa methods coming from amtch!
pattern = r"pam"
match= re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span()) #returns tuple!

#search and replace
#sytnax : re.sub(pattern, repl, string, count=0) replaces all occurrences of pattern iwth repl (if count=n>0 then only the first n occurences)
str ='My name is David. Hi David.'
pattern =r"David"
newstr=re.sub(pattern, "Amy", str) #count=1 only the first David is replaced
print(newstr)

pattern2="David"
newstr2=re.sub(pattern2, "Amy", str) #
print(newstr2)

#####
#Metacharacters  --making regular expressions more powerful than normal stirng methods
#######
""" 
conceopts like "one or more repetitions of a vowel"
Problem: Using Symbols like "$" --> using backslash to "escape": /$
Problem2: Backslash  also have an escaping function in normal python strings -->putting 3 or 4 backslashes in a roow to do all the escaping
avoid: use raw string : normal string with "r" in front of it
"""
#

pattern= r"gr.y"  # . stans for any sinlge character

if re.match(pattern, "grey"):
    print("Match1")

if re.match(pattern, "gra2y"):
    print("Match2")

if re.match(pattern, "blue"):
    print("Match3")

pattern2= r"gr..y"  # . stans for any sinlge character
if re.match(pattern2, "gr42y"):
    print("Match2")



####
# New metacharacters: ^ and $ --> stand fpr start and end
import re
pattern2 = r"^gr.y$"
pattern= r"gr.y"
if re.match(pattern2, "grey"):
    print("Match1")
if re.search(pattern2, "sgrays"): #does not match as it does not start with gr
    print("Match with pattern2")

if re.search(pattern, "sgrays"): 
    print("Match with pattern")


#character classes : See if any of the characters fits
pattern = r"[aeiou]"  
 if re.search(pattern, "grey"):
     print("match 1")

 if re.search(pattern, "qwertyuiop"):
     print("match 2")
 if re.search(pattern, "rythm myths"):
     print("match 3")


#[a-z], [G-P], [0-3], [A-Za-z] ...
pattern=r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8" ):
    print( "Match 1")

if re.search(pattern, "1ab" ):
    print( "Match 2")

#invert with ^ : --> match any character other than the ones included
# ( $ or . have no meaining within character class! 1 ^ has only a meaning if its the first character in a class)
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet" ):  
    print( "Match 1")

if re.search(pattern, "B" ):  # no Match as this consits only of capital letters
    print( "Match 2")

if re.search(pattern, "CAPITALLETTERS and small letters" ):  #Match as also spaces and small letters are included
    print( "Match 3")

# * and ? -> numbers of repetitions
# * : 0 or more repetions of the previous thing -> match as many reps as possible ("previous thing = single character, class, group of characters in parentheses")
pattern = r"egg(spam)*" #parentheses refer to the *
if re.search(pattern, "egg" ):  
    print( "Match 1")

if re.search(pattern, "eggspamspamegg" ):  # no Match as this consits only of capital letters
    print( "Match 2")

if re.search(pattern, "spam" ):  #Match as also spaces and small letters are included
    print( "Match 3")

# + : one more rep
pattern = r"g+"
if re.match(pattern, "g" ):  
    print( "Match 1")

if re.match(pattern, "ggggggg" ):  # starts with g and anything more , so matches
    print( "Match 2")

if re.match(pattern, "agg" ):  #Match needs it to start with g, ere not the case
    print( "Match 3")

# ? : 0 or one repetitions
pattern= r"ice(-)?cream"
if re.match(pattern, "ice-cream" ):  
    print( "Match 1")

if re.match(pattern, "icecream" ): 
    print( "Match 2")

if re.match(pattern, "ice-cre" ):  
    print( "Match 3")

# curly braces {} : represent number of reps between two numbers
# {x,y} : between x and y pres of sth --{0,1}: same thing as ?
# if first number missing-> taken to be zero, second number a sdefault= inf
pattern = r"9{1,3}$" 
pattern2= r"9{1,3}" 
if re.match(pattern2, "9" ):  
    print( "Match 1")

if re.match(pattern2, "999" ):  
    print( "Match 2")

if re.match(pattern2, "9999" ):  #Matches only pattern2, as does not have to end with at most 999
    print( "Match 3")


####
#Groups  -- created by surrounding part of regex with parenthesis  --> group can be given as an aarguement to metacharasters such as * and ?
###
import re
pattern= r"egg(spam)*"  ## --> spam represents here a group
if re.match(pattern, "egg" ):  
    print( "Match 1")

if re.match(pattern, "eggspamspamspamegg" ):  
    print( "Match 2")

if re.match(pattern, "spam" ):  #Matches only pattern2, as does not have to end with at most 999
    print( "Match 3")

# group functions
#group(0) or group() returns whole match, gorup(n) : where n>0, returns nth from the left, groups() return all groupy from 1
pattern=r"a(bc)(de)(f(g)h)i"
match =re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

#########################################
#Only for Working PC
#####################################
 ##Connection to Exasol (simple)
C = pyexasol.connect(dsn='10.12.240.200..234:8563',user='BU_RED_ETL_GENERAL', password='<password>') #type in password!

  # or by storing passwords in  path C:\Users\sina.herbst in .pyexasol.ini file
  #with :
[my_exasol]
dsn=10.12.240.200..234:8563
user=BU_RED_ETL_GENERAL 
password=<password>  #no ''!
#

C = pyexasol.connect_local_config('my_exasol') 

##----------------------------
#Reading data into Dataframe - 2 ways
##----------------------------
#1) 
ql_stmt = """
SELECT ID, GESPR_CHSERGEBNIS_DETAILS_KOMMENTAR__C
	FROM BU_RED_ETL.SALESFORCE_TASKS s
	WHERE id='00T1i000025piGdEAI'
                
"""
results = C.execute(sql_stmt) 
df1 = pd.DataFrame(results, 
                   columns = ['ID', 'GESPR_CHSERGEBNIS_DETAILS_KOMMENTAR__C']                   
                  )

#2)
df2 = C.export_to_pandas("SELECT *FROM BU_RED_ETL.SALESFORCE_TASKS WHERE id='00T1i000025piGdEAI'")


#writing from dataframe into exasol table

test=df1['ID'] #get df1 from above
df1=pd.DataFrame(df1)
sql_stmt = """
CREATE OR REPLACE TABLE tmp_tables.test_example  ( 
                Id VARCHAR(18)
                )
"""
results = C.execute(sql_stmt) 
C.import_from_pandas(df1, ('tmp_tables','test_example'))

#######################################################################
# SALESFORCE DATA SALESFOFCE CONNECTION SFDC
########################################################################

#1) Reading SFDC Data Into Dataframe
##reading directly from sfdc

import pandas as pd
from simple_salesforce import Salesforce
import os

# Input Salesforce credentials:
os.chdir('C:\\Users\\sina.herbst\\Documents')  #later with basehook in airflow, currently on working on Sinas local machine
import sfdc_config
sf = Salesforce(username=sfdc_config.username,password=sfdc_config.password,security_token=sfdc_config.token) 
#reading data into df
sf_data = sf.query_all("SELECT Id , Description FROM Task where Id='00T1i000025piGdEAI'")
sf_df = pd.DataFrame(sf_data['records']).drop(columns='attributes')

####SFDC Report Salesforce Report Connection 
#works but limits to 2k rows
'''
from salesforce_reporting import Connection, ReportParser
import pandas as pd
your_token='<see 1password>'
your_username='<see 1password>'
your_password='<see 1password>'
sf = Connection(username=your_username,password=your_password,security_token=your_token)
#report = pd.DataFrame(sf.get_report('00O1i000001nXNmEAM'))
report = pd.DataFrame(ReportParser(sf.get_report('00O1i000001nXNmEAM')).records_dict())
'''

#got from https://stackoverflow.com/questions/22853232/importing-salesforce-report-data-using-python#comment101771947_51885281
import pandas as pd
import csv
import requests
from io import StringIO
from simple_salesforce import Salesforce
import pyexasol
import os
C = pyexasol.connect_local_config('my_exasol') 

# Input Salesforce credentials:
import os
os.chdir('C:\\Users\\sina.herbst\\Documents')  #later with basehook in airflow, currently on working on Sinas local machine
import sfdc_config
sf = Salesforce(username=sfdc_config.username,password=sfdc_config.password,security_token=sfdc_config.token) 


# Basic report URL structure:
orgParams = 'https://xing-e-recruiting.my.salesforce.com/' # you can see this in your Salesforce URL
exportParams = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'

# Downloading the reports:
##ACCOUNT
reportId_account = '00O1i000001nXNmEAM' # You find this in the URL of the report in question between "Report/" and "/view"
reportUrl_account = orgParams + reportId_account + exportParams
reportReq_account = requests.get(reportUrl_account, headers=sf.headers, cookies={'sid': sf.session_id})
reportData_account = reportReq_account.content.decode('utf-8')
reportDf_account = pd.read_csv(StringIO(reportData_account))
#converting dates into data format
reportDf_account['Übergabe an Farmer']= pd.to_datetime(reportDf_account['Übergabe an Farmer'])



for file in Rfiles_with_sql:
#file=Rfiles_with_sql[151] #testing
#file=Rfiles_with_sql[1]
    file1=open(file[0],'r')
    lines=file1.readlines()
    script=''
    for rawline in lines:
        #combine the lines
        line = rawline.strip()
        line = ' '.join(line.split())
        #script=script+' ' +line  #'\n'+line
        script=script+ '/splitit/' +line
    cl_script=script.split('sqlQuery')
    cl_script=cl_script[1:]  #remove first entry as there is no sql query
    #for any entry in cl_scripts there should be now an sql. 
    #We collect the single sql in sqls
    R_sqls=[]
    for block in cl_script:
        sql_start_pos = block.find('("') #beginning of sql
        block_cut=block[sql_start_pos:] #first remove until start
        #there could be several ") that are not yet the ending. We say that its the ending as soon as it is the same number of ( as of )
        d='")'
        #split by ") but include d
        block_parts=[e+d for e in block_cut.split(d) if e]
        #add part until we have same number of ") as of "(
        part=block_parts[0]  
        for i in range(len(block_parts)):
            if part.count('(')==part.count(')'):
                R_sql=part[2:len(part)-2]
            else:
                part=part+block_parts[i]
        #print(sql)
        R_sqls.append(R_sql)
    #file_sqls.append(sqls)
