## Built-in Types of Python (Numeric Types and Strings)

# Write a program that asks to enter the width and length of a room in meters and print the area of the room.

l = float(input('Please enter the length of the room in meter? '))
w = float(input('Please enter the width of the room in meter? '))
area = l*w

print ("The area of the room is", area )


# Write a program that takes a positive integer, n, and then displays the sum of all the integers from 1 to n. 
# The sum of the first n positive integers can be computed using the formula: n * (n + 1) / 2

n = int(input('Please enter a positive integer number!'))
sum = n*(n+1)/2
print ("The sum of the first", n, "positive integers is", sum)


# A savings account earns 4 percent interest per year and is added to the balance of the savings account. 
# Write a program that takes the amount of the money deposited and then displays the amount in the account after 1, 2, and 3 years.

s = float(input('Please enter your deposit amount, to calculate the amount of your saving in next 3 years!'))
year_one = s + (0.04*s)
year_two = year_one + (0.4*year_one)
year_three = year_two + (0.04*year_two)
print ("The amount of your saving account at the end of first year will be", year_one)
print ("The amount of your saving account at the end of second year will be", year_two)
print ("The amount of your saving account at the end of third year will be", year_three)


# Write a program that takes a four-digit integer and displays the sum of the digits in the number. 

n = input("Please enter a 4-digit integer! I'll return the sum of digits in your number!")
sum = int(n[:1]) + int(n[1:2]) + int(n[2:3]) + int(n[3:]) 

print ("the sum of digits in your number is", sum)


# Write a program which can return a string made up of the first and the last elements from a given string.

s = input("Please enter a string!")
sum = s[0] + s[-1] 

print ("A string made up of the first and the last elements of the given string is", sum)


# Write a program which can return a string made up of the first 2 and the last 2 elements from a given string.

s = input("Please enter a string!")
sum = s[:2] + s[-2:] 

print ("A string made up of the first 2 and the last 2 elements of the given string is", sum)


# Write a program that can change a given string to a new string, in which the first and last elements of the given string are exchanged.

s = input("Please enter a string!")
sum = s[-1]+ s[1:-1] + s[0] 

print ("The first and last elements of the given string are exchanged! The new string is:", sum)
