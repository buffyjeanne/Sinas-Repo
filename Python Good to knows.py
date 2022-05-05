# Python Good to knows
#  -> When using try functions and so on

#always close a file! -> Use Try and finally functions
try:
   f = open("tesfile.txt")
   print(f.read())
finally:
   f.close() #This ensures that the file is always closed, even if an error occurs


#also possible: Use with clause -> only within with clause the file is open
with open("testfile.txt") as f:
   print(f.read())


#pure functions and impure functions
#Definition: "pure function" is a function in mathematical definition, meaning that fun(a) is exact one value and always the same
#advantages pure functions: 
   # more efficient ->result can be referred to the next time the function of that input is needed ->"Memoization"
   #easier tu run in parallel
#examples
def pure_function(x,y):
   temp=x+2*y
   return temp/(2*x+y)

some_list=[]
def impure_function(arg):
   some_list.append(arg)
   #ouput also depends on some_list, which can be different!

####################################
#Object Lifecycle
####################################
#made up of its creation,manipulation, destruction
"""
1. Definition
2. Instantiation when __init__ is called
3. __new__ --> usually overridden only in special cases
4. ready to be used
5. destroyed

Destroyed: memory freed up 
destroyed when reference count (numer of variables and other elements that refer to the object) reaches zero 
if noting is referring nothing can interact with it -> can safely be deleted

in some situations, 2 or more objects can be referred to by each other only and therefore can be deleted as well
the "del" statement reduces the reference count of an object by one and this often leads to its deletion
the magic method: __del__
 "Garbage collection"

 In summary, an object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary).
  The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. 
  When an object's reference count reaches zero, Python automatically deletes it.
Example:
"""
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>


#########################
#Data Hiding
########################
"""
key part of Programming: ENCASULATION -> involes packaging of related variables and functions into a singl easy to use object -> an instance of a class
related: Data Hiding -> details of a class should be hiden -> clean standard interface
(in other programming languages: by private methods and attributes that block external access to certain methods)
(private method= external code is discourages from using)
"""
 
 #Weakly private methods/attributes: "_" at beginning (only a convention). Only effect is that "from module_name import *" wont import variables that start with a single underscore

class Queue:
   def __init__(self, contents):
      self._hiddenlist =list(contents)
   def push(self, value):
      self._hiddenlist.insert(0,value)
   def pop(self):
      return self._hiddenlist.pop(-1)
   def __repr__(self): ##defined method to "represent" when typing print(qiueue)?
      #return "Queue ({})".format(self._hiddenlist)
      return format(self._hiddenlist)

   queue=Queue([1,2,3])
   print(queue)
   queue.push(0)
   print(queue)
   queue.pop()
   print(queue)
   print(queue._hiddenlist)

   #Strongly private methods
   # "__" at beginning  --> cant be accessed from outside the class "mangled"--> to avoid bugs if there are subclasses that have methods/attributes the wit same name
   #Name mangled methods can be still accessed externally but by a different name
   # method "__privatemethod" of class Spam could be accessed externeally with _Spam__privatemethod

class Spam:
   __egg=7
   def print_egg(self):
      print(self.__egg)

s=Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg) #does not work as python protects tmembers by internally changin the name to include a class name


