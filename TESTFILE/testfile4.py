import string
#WAP TO PRINT OCCURANCE OF EACH LETTER IN STRING
input = "pythonDeveloper"

occurance= {}
for letter in input:
    if letter in occurance:
        occurance[letter] += 1
    else:
        occurance[letter] = 1

# printing result
print("Occurrence of all characters in pythonDeveloper is :\n " + str(occurance))


#WAP TO PRINT  OCCURANCE VOWEL IN STRING

def Check_Vow(string, vowels):
    check = [each for each in string if each in vowels]
    print(len(check))
    print(check)


# Driver Code
string = "PYTHONDEVELOPER"
vowels = "AEIOU"
Check_Vow(string, vowels)



x = input("Type a number: ")
y = input("Type another number: ")
z = input("enter 3rd number :")


sum = int(x) + int(y) +int(z)

print("The sum is: ", sum)