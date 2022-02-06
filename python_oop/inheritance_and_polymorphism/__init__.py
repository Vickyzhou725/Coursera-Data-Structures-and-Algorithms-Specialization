"""
https://www.w3schools.com/python/python_inheritance.asp
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""

# 1. create a parent class
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print("Inside Person print_name")
        print(self.first_name, self.last_name)

p = Person("Kobe", "Bryant")
p.print_name()

# 2. create a child class
"""
Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class
Now the Student class has the same properties and methods as the Person class.
"""
class Student(Person):
    pass

s = Student("Michael", "Jordan")
print(s.first_name, s.last_name)
s.print_name()

# 3. add the __init__() function and calling parent methods
"""
Note: The child's __init__() function overrides the inheritance_and_polymorphism of the parent's __init__() function.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
To keep the inheritance_and_polymorphism of the parent's __init__() function, add a call to the parent's __init__() function
"""
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

    def welcome(self):
        print("Inside Student welcome")
        Person.print_name(self)

s = Student("Michael", "Jordan")
print(s.first_name, s.last_name)
s.print_name()
s.welcome()

# 4. use the super() function to inherit parent methods and properties
"""
Python also has a super() function that will make the child class inherit all the methods and properties from its parent
By using the super() function, you do not have to use the name of the parent element or the self parameter
it will automatically inherit the methods and properties from its parent.
"""
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def welcome(self):
        print("Inside Student welcome")
        super().print_name()

s = Student("Michael", "Jordan")
print(s.first_name, s.last_name)
s.print_name()
s.welcome()
# 5. properties adding and constructor overriding
"""
By overriding the __init__() function, you'll be able to add your own properties
"""
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Inside Student welcome")
        super().print_name()

s = Student("Michael", "Jordan", 2019)
print(s.first_name, s.last_name, s.graduation_year)
s.print_name()
s.welcome()

# 7. methods overriding
"""
If you add a method in the child class with the same name as a function in the parent class, 
the inheritance_and_polymorphism of the parent method will be overridden.
By overriding parent class methods, we can change the behavior of exist methods
"""
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Inside Student welcome")
        super().print_name()

    def print_name(self):
        print(self.first_name, self.last_name, self.graduation_year)

s = Student("Michael", "Jordan", 2019)
print(s.first_name, s.last_name, s.graduation_year)
s.print_name()
s.welcome()


# 7. constructor overloading
"""
Note: Python does not support constructor overloading.
We can only achieve overloading based on function to take multiple arguments
"""

# 7.1 calling methods from __init__
class eval_equations:

    # single constructor to call other methods
    def __init__(self, *inp):

        # when 2 arguments are passed
        if len(inp) == 2:
            self.ans = self.eq2(inp)

        # when 3 arguments are passed
        elif len(inp) == 3:
            self.ans = self.eq1(inp)

        # when more than 3 arguments are passed
        else:
            self.ans = self.eq3(inp)

    def eq1(self, args):
        x = (args[0] * args[0]) + (args[1] * args[1]) - args[2]
        return x

    def eq2(self, args):
        y = (args[0] * args[0]) - (args[1] * args[1])
        return y

    def eq3(self, args):
        temp = 0
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = temp
        return z


inp1 = eval_equations(1, 2)
inp2 = eval_equations(1, 2, 3)
inp3 = eval_equations(1, 2, 3, 4, 5)

print("equation 2 :", inp1.ans)
print("equation 1 :", inp2.ans)
print("equation 3 :", inp3.ans)

# 7.2 using @classmethod decorator
"""
This decorator allows a function to be accessible without instantiating the class. 
The functions can be accessed both by the instance of the class and the class itself
"""
class eval_equations:

    # basic constructor
    def __init__(self, a):
        self.ans = a

    # expression 1
    @classmethod
    def eq1(cls, args):
        # create an object for the class to return
        x = cls((args[0] * args[0]) + (args[1] * args[1]) - args[2])
        return x

    # expression 2
    @classmethod
    def eq2(cls, args):
        y = cls((args[0] * args[0]) - (args[1] * args[1]))
        return y

    # expression 3
    @classmethod
    def eq3(cls, args):
        temp = 0

        # square of each element
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = cls(temp)
        return z


li = [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]
i = 0

# loop to get input three times
while i < 3:

    inp = li[i]

    # no.of.arguments = 2
    if len(inp) == 2:
        p = eval_equations.eq2(inp)
        print("equation 2 :", p.ans)

    # no.of.arguments = 3
    elif len(inp) == 3:
        p = eval_equations.eq1(inp)
        print("equation 1 :", p.ans)

    # More than three arguments
    else:
        p = eval_equations.eq3(inp)
        print("equation 3 :", p.ans)

    # increment loop
    i += 1
# 8. methods overloading
"""
Note: Python does not support method overloading. 
We may overload the methods but can only use the latest defined method.
"""
# 8.1 function takes multiple arguments
# Function to take multiple arguments
def add(datatype, *args):
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

# 8.2 using multiple dispatch decorator
from multipledispatch import dispatch


# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 2 arguments
product(2, 3, 2)  # this will give output of 12
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997