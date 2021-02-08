import string

input = "pythonDeveloper"

occurance= {}
for letter in input:
    if letter in occurance:
        occurance[letter] += 1
    else:
        occurance[letter] = 1

# printing result   
print("Occurrence of all characters in pythonDeveloper is :\n " + str(occurance))


#rajeshthakur1r@gmail.com
#Parameters
#Parameters are inputs to the function. If a function contains parameters,then at the time
#of calling,compulsory we should provide values otherwise,otherwise we will get error.


def math_operation(x,y):
    return x+y,x*y

def sub(x,y):
    return x-y

add,mul = math_operation(2,5)
sub=sub(add,5)
print("the substraction result is ",sub)
print("The multiplication result is ",mul)


def f1():
    print("hello")
def f2():
    f1()

f2()
# Write a function which will identify the Even and odd Number
def is_even(num):
    if num%2 ==0:
        print(num," is a even number")
    else:
        print(num," is not an even number")

is_even(5)
is_even(6)


#####################################
# write a program to segrigate list in eveen and odd list
def seg_even_odd(l):
    even_list=[]
    odd_list = []
    for i in l:
        if i % 2 ==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list,odd_list


even_list,odd_list=seg_even_odd([1,2,3,4,5,6])
print("even list ",even_list)
print("odd list ",odd_list)
###############################################


#stepts

# Python code to count and display number of vowels
# Simply using for and comparing it with a
# string containg all vowels
def Check_Vow(string, vowels):
    check = [each for each in string if each in vowels]
    print(len(check))
    print(check)


# Driver Code
string = "PYTHONDEVELOPER"
vowels = "AEIOU"
Check_Vow(string, vowels)


# Count vowels in a different way
# Using dictionary
def Check_Vow(string, vowels):
    # casefold has been used to ignore cases
    st = string.casefold()

    # Forms a dictionary with key as a vowel
    # and the value as 0
    #c = {}.fromkeys(vowels, 0)
    count={}.fromkeys(vowels,0)

    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1
    return count


# Driver Code
vowels = 'aeiou'
string = "Geeks for Geeks"
print(Check_Vow(string, vowels))