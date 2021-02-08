r=12
pie=3.14285714286
volume=(4.0/3.0)*pie*(r*r*r)
print("volume of the sphere="+str(volume))



s = "we are learning python, we are att the begning statge"
========================
# convert the strin into substring and then check which string contaning python
s = "we are learning python, we are att the begning statge"
# strings=s.split(',')
# for string in strings:
#     if "python" in string:
#         print(string," contaning python")
#     else:
#         print(string,"not contaning python")
=====================
# 2. By using slice operator:
# Syntax:
# list2= list1[start:stop:step]

n=[1,2,3,4,5,6,7,8,9,10]

for i in n:
    if i%2==0:
        print(i," devisible by 2")
    else:
        print(i, " not devisible by 2")
=====================


s = "we are learning python, we are att the begning statge"
========================
# convert the strin into substring and then check which string contaning python
s = "we are learning python, we are att the begning statge"
# strings=s.split(',')
# for string in strings:
#     if "python" in string:
#         print(string," contaning python")
#     else:
#         print(string,"not contaning python")
=====================
# 2. By using slice operator:
# Syntax:
# list2= list1[start:stop:step]

n=[1,2,3,4,5,6,7,8,9,10]

for i in n:
    if i%2==0:
        print(i," devisible by 2")
    else:
        print(i, " not devisible by 2")
=====================
From Rajesh Thakur to Everyone:  06:53 PM
#Count function
#2. count():
       #It returns the number of occurrences of specified item in the list

n=[5, 2, 2, 2, 2, 3, 3]

unique_list=[5,2,3]


for i in unique_list:
    print("occurance of ", i, n.count(i))


# print()
# print("occurance of 2 ",n.count(2))
# print("occurance of 3 ",n.count(3))
# 3. index() function:
# returns the index of first occurrence of the specified item

n=[5, 2, 2, 2, 2, 3, 3]
print(n.index(2))
From Rajesh Thakur to Everyone:  07:04 PM
#___________________________________ Append+++++++++++++++++++++___________________
list = []
print("Before adding the elements ",list)
list.append("Rajesh")
list.append("Sangita")
list.append("Guriya")
print("after adding the Elements ",list)
# 2. insert() function:
# To insert item at specified index position


list = [1,2,3,6,4,5,6]
#list.insert("index No","value")
list.insert(-3,12344)
print(list)
From Rajesh Thakur to Everyone:  07:09 PM
#++++++++++++++++++Extends()___________________+++++============================================

# 3. extend() function:
# To add all items of one list to another list
list = ['paneer','Mashroom']
list1 = ['rice','wheet','pulse']
list.extend(list1)
print(list)


==========================
# =================================remove()=======================================
# 4. remove() function:
# We can use this function to remove specified item from the list.If the item present
# multiple times then only first occurrence will be removed.
#n = [1,2,3,4,4,4]

# n=[10,20,10,30]
# n.remove(10)
# print(n)


# 5. pop() function:
# It removes and returns the last element of the list.
# This is only function which manipulates list and returns some element.

n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n.pop())
print(n.pop())
print(n.pop())



n=[10,20,30,40]
#print(n[::-1])
n.reverse()
print(n)


x= [1,2,3,4,5]
y = [11,22,33,44,55]
x=y  # Deep copy
y[1]=777
print(x)
print(y)
#### Shallow copy()

x= [1,2,3,4,5]
y = [11,22,33,44,55]
x=y.copy()  # shollow copy
y[1]=777
print(x)
print(y)


#============================================= Aithematic operation on list==================
# x=["Dog","Cat","Rat"]
# y=["Rat","Cat","Dog"]
# print(x>y)
# print(x>=y)

# ====================================== Menbership operator
n=[10,20,30,40]
print (10 in n)
print (11 in n)
##  ============================== clear()-====================
#We can use clear() function to remove all elements of List.
n=[10,20,30,40]
n.clear()
print(n)



#1. Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple
#object,we cannot perform any changes in that object.
#Hence Tuple is Read Only version of List.

#If our data is fixed and never changes then we should go for Tuple.
# Insertion Order is preserved
# Duplicates are allowed
# Heterogeneous objects are allowed.

t = []  ### List
t = (10,'rajesh',10.5)   ### tuple
print(type(t))



t = []  ### List
t = (10,'rajesh',10.5,2,4,5,5,5,5)   ### tuple
print(type(t))
print(t[1:])
print(t[::-1])
print(t.count(5))


# Note :- those function which is used to fetch the data in the list same fuction we can use in
# tuple

#2. Those fun which used to manuplate the data in list that fuction we can not use in tuple



t = []  ### List
t = (10,'rajesh',10.5,2,4,5,5,5,5)   ### tuple
t = list(t)
print(type(t))
t.append("Anthony")
print(t)
t = tuple(t)
print(type(t))



# # If we want to represent a group of unique values as a single entity then we should go
# #for set.
#Duplicates are not allowed
#Insertion order is not preserved.But we can sort the elements.
#  so index() will not allowed
# Indexing and slicing not allowed for the set.
# Heterogeneous elements are allowed.
#Set objects are mutable i.e once we creates set object we can perform any changes in
    #that object based on our requirement.
# We can represent set elements within curly braces and with comma seperation
# We can apply mathematical operations like union,intersection,difference etc on set
# objects.




=============================
# # If we want to represent a group of unique values as a single entity then we should go
# #for set.
#Duplicates are not allowed
#Insertion order is not preserved.But we can sort the elements.
#  so index() will not allowed
# Indexing and slicing not allowed for the set.
# Heterogeneous elements are allowed.
#Set objects are mutable i.e once we creates set object we can perform any changes in
    #that object based on our requirement.
# We can represent set elements within curly braces and with comma seperation
# We can apply mathematical operations like union,intersection,difference etc on set
# objects.

# Creation of Set
s={10,20,30,40,40}
#list = [1,2,3,4,5]
print(s)
print(type(s))
s = list(s)
print(type(s))

#================================
l = [10,20,30,40,10,20,10]
l = set(l)
print(type(l))



# Creation of Set
s={10,20,30,40,40}
#list = [1,2,3,4,5]
print(s)
print(type(s))
s = list(s)
print(type(s))

#================================
l = [10,20,30,40,10,20,10]
l = set(l)
print(type(l))
==========================
#print(range(5))
s =set(range(5))
print(s)

s =list(range(5))
print(s)


==========================
#print(range(5))
s =set(range(5))
print(s)

s =list(range(5))
print(s)
From Rajesh Thakur to Everyone:  08:15 PM
=========================
#===============================
#Important functions of set:
# 1. add(x):
s={10,20,30}
s.add(40)
s.add(50)
print(s)



#We can use List,Tuple and Set to represent a group of individual objects as a single entity.
# If we want to represent a group of objects as key-value pairs then we should go for
#Dictionary.
#rollno----name
#phone number--address
#ipaddress---domain name

# Duplicate keys are not allowed but values can be duplicated.
# Hetrogeneous objects are allowed for both key and values.
# insertion order is not preserved
# Dictionaries are mutable
# Dictionaries are dynamic
# indexing and slicing concepts are not applicable
#
# Note: In C++ and Java Dictionaries are known as


=======
#d = {} or d = dict()
d = dict()
d[100] = "raj"
d[200] = "thakur"
d[300]= "singh"
d[400] ="MS"
d[100]="Sudhanshu"

print(d)




==========================
#d = {} or d = dict()
d = dict()
d[100] = "raj"
d[200] = "thakur"
d[300]= "singh"
d[400] ="MS"
d[100]="Sudhanshu"

print(d)
From Rajesh Thakur to Everyone:  08:39 PM
=====================
#Q. Write a program to enter name and percentage marks in a dictionary and
# display information on the screen


# rajesh                   80.5
# mahesh                   70.5
# MS                       84.5
# sudhanshu                94.5

record = {}
n=int(input("Enter number of students: "))
for i in range(1,n+1):
    name = input("Enter the Student name")
    marks = float(input("Enter the % of the marks of the student"))
    record[name]=marks

print("name of the Students","\t","% of marks")
for x in record:
    print('\t',x,'\t',record[x])



# How to update dictionaries?

# If the key is not available then a new entry will be added to the dictionary with the
# specified key-value pair
# If the key is already available then old value will be replaced with new value.

d = {100:"raj",200:"thakur",300:"MS"}
d[100] = "chotaBheem"
d[101] = "Raju"
print(d[102])



# How to delete elements from dictionary?

d = {100:"raj",200:"thakur",300:"MS"}

del d[100]

print(d)
d[100] = "rajesh"
print(d)


# clear()
# To remove all entries from the dictionary

d = {100:"raj",200:"thakur",300:"MS"}
print(d)
d.clear()
print(d)
d[100]="rajesh"
print(d)

