"""
https://www.w3schools.com/python/python_classes.asp
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""

# 1. create a class
class MyClass:
    x = 5

# 2. create object
cls1 = MyClass()
print(cls1.x)

# 3. the __init__() function
"""
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object is being created
Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# 4. object methods
"""
Objects can also contain methods. Methods in objects are functions that belong to the object.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# 5. the self parameter
"""
Note: The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.
It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class
"""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# 6. modify object properties
p1.age = 40
print(p1.age)


# 7. delete object properties
del p1.age
print(p1.age)

# 8. delete objects
del p1
print(p1.name)

# 9. the pass statement
"""
class definitions cannot be empty, but if you for some reason have a class definition with no content, 
put in the pass statement to avoid getting an error.
"""
class Person:
    pass