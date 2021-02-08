print("hellos")


i =2
b = 2

print("the value of i ",i)
print("the value of b ", b)
print("The type of b ",type(b))
print("the type of i ",type(i))

print("The addition of i and b",(i+b))





i =2.3
b = "3"

b = int(b)

print("the value of i ",i)
print("the value of b ", b)
print("The type of b ",type(b))
print("the type of i ",type(i))
print("The addition of i and b",(i+b))


# type casting
# upcasting
# down casting
# int -- 2byte
# char ---1 Byte
# float =   4
# double = 8 byte

i =2
b = 2

print("the value of i ",i)
print("the value of b ", b)
print("The type of b ",type(b))
print("the type of i ",type(i))

print("The addition of i and b",(i+b))
i =2.3
b = "3"

b = int(b)

print("the value of i ",i)
print("the value of b ", b)
print("The type of b ",type(b))
print("the type of i ",type(i))

print("The addition of i and b",(i+b))


# type casting
# upcasting
# down casting
# int -- 2byte
# char ---1 Byte
# float =   4
# double = 8 byte

i = int(input("Hey user's fellow please enter a number"))

b = int(input("Hey user's fellow please enter another number"))

print("the value of i ",i)
print("the value of b ", b)
print("The type of b ",type(b))
print("the type of i ",type(i))

print("The addition of i and b",(i+b))


# type casting
# upcasting
# down casting
# int -- 2byte
# char ---1 Byte
# float =   4
# double = 8 byte


##  List
# List is the data staructure in which we can add the hetrogenous data
# List is mutable in nature
# Growable in nature
# the items is going to be store as per their insertion order

# How to define the list
l = [1,2,'rajesh',1.3]

print(type(l))
print(l)
print(l[0])
print(l[2])

# Slicing
print(l[1:])
print(l[:3])
print(l[1:3])

l.append("Sangita")

print(l)




# To check the Length
print(len(l))


l = [3,4,4,5,6,"raj","kumar","xyz"]
for i in l:
    print(i,"1")


# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.
num = int(input("Hey user which table you want"))
for i in range(1,11):
    mul = num*i
    print(str(num)+"*"+str(i)+'='+str(mul))

for i in range(10):
    print(i)
    if i == 5:
        break


for i in range(10):

    if i == 5:
        continue
    print(i)


#Write a Python program to find the volume of a sphere with diameter 12cm
diameter =12
a=4/3*3.14*6*6*6
print(a)



# function
# n1 = 2
# n2 = 3
# print(n1+n2)

# If a group of statements is repeatedly required then it is not recommended to write these
# statements everytime seperately.

#We have to define these statements as a single unit and
#we can call that unit any number of times based on our requirement without rewriting.

#Python supports 2 types of functions
#1. Built in Functions
# 2. User Defined Functions

# 1. Built in Functions:
# The functions which are coming along with Python software automatically,are called built
# in functions or pre defined functions

# Eg:
# id()
# type()
# input()
# eval()
# etc..
==========================


#              Checked Exception                                                      Runtime Exception
# Checked Exception are those which will check at compile time     inchecked Exception are those which will check at runtime time

# In any programming language there are 2 types of errors are possible.
# 1. Syntax Errors
# 2. Runtime Errors

     # a. Aithematic Error    8/0
     # b. Array Outof Bound
From Rajesh Thakur to Everyone:  06:01 PM
=========================
#What is Exception:
#An unwanted and unexpected event that disturbs normal flow of program is called
#exception.

#Eg:
# ZeroDivisionError
# TypeError
# ValueError
# FileNotFoundError
# SleepingError
try:
    # we use to keep the code from where the Exception might be occur

except Exception as e:
    # except the Exception whic created in try bllock

    # Q.What is an Exception?
    # Q. What is the purpose of Exception Handling?
    # Q. What is the meaning of Exception Handling?

    # Default Exception Handing in Python:

    # Every exception in Python is an object.For every exception type the corresponding classes aren available.

    print("Hello")

    try:
        print(10 / 2)
    except Exception as z:
        print("a number can not be devided by zero:-", z)

    print("Hi")

    # Note:- if try block will get Excuted Successully then Except block will not excute
    # but if try block will get fail to Excute then except block will excute





  #Every exception in Python is an object.For every exception type the corresponding classes aren available.

print("Hello")

try:
    print(10 / 0)

except Exception as z:
    print("a number can not be devided by zero:-",z)

except TypeError as t:
    print("The is block excuted due to the the Type Error")

except ValueError as z:
    print("this block Excuted due to the Zero Devisional Error")

    # Default Exception Handing in Python:

    # Every exception in Python is an object.For every exception type the corresponding classes aren available.

    print("Hello")

    try:
        print(10 / 0)

    except Exception as z:
        print("a number can not be devided by zero:-", z)

    except TypeError as t:
        print("The is block excuted due to the the Type Error")

    except ValueError as z:
        print("this block Excuted due to the Zero Devisional Error")
    try:
        x = int(input("Enter First Number: "))
        y = int(input("Enter Second Number: "))
        print(x / y)

    except ZeroDivisionError as z:
        print("Can't Divide with Zero")

    except TypeError as t:
        print("please provide int value only")

    except Exception as e:
        print(e)

    print("Finally Excuted Successfully")

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x / y)


except TypeError as t:
    print("please provide int value only")

finally:  # Finally block will always Excute even try or Except feell to Excute

    print("Finally Block Excuted Successfully")

print("Finally Excuted Successfully")






opps
#OOps:- is is just increase the reausiblity of the code

class Mobile_shop:
    pass

a = Mobile_shop()

a2 = Mobile_shop()

a.mobile = "Samsung"
a.tv = "TV"
a.ref = "LG Refregetor"

a2.mobile = "Apple"
a2.ref = "werlfool"

print(type(a))
print(a.mobile)

print(a2.mobile)

print(type(a2))

