
## if-elif-else structure

# The employees of a company are rated at the end of each year for possible salary raise. 
# The rating that could be awarded to an employee is 0.0 (unacceptable), 0.4 (acceptable), or 0.6 (exceptional). 
# No other values are to be used for the rating. The amount of an employee's salary raise is 3000.00 euro multiplied by their rating.
# Write a program that takes a rating and indicates whether the corresponding performance.
# The amount of the employee's salary raise should also be returned.

rating = float(input('Please enter the rating amount:'))
if rating == 0.0:
    print ('the rating is unacceptable, and the salary raise will be:', rating*3000.00, 'euros')
elif rating == 0.4:
    print ('the rating is acceptable, and the salary raise will be:', rating*3000.00, 'euros')
elif rating == 0.6:
    print ('the rating is exceptional, and the salary raise will be:', rating*3000.00, 'euros')
else:
    print ('the rating is invalid')


# Write a program that takes a letter of the English alphabet from the user. 
# The program should display a message indicating that the entered letter is a vowel or consonant.

letter = input('Please enter a letter of the English alphabet:')
vowels={"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}

if letter in vowels:
    print (letter, 'is a vowel!')
elif letter == "y" or letter== "Y":
    print ('Sometimes y is a vowel, and sometimes y is a consonant!')
else:
    print (letter, 'is a consonant!')

 
# Write a program that takes the name of a month as a string and returns the number of days in that month.

month = input('Please enter name of month:')
length_of_month={"January":31, "Febuary":[29, 30], "March":31,
                 "April":30, "May":31, "June":30,
                 "July":31, "August":31, "September":30,
                 "October":31, "November":30, "December":31}

if month in length_of_month:
    print ('The lenghth of', month, 'is',length_of_month[month])

else:
    print ('The input month is not valid')


# Body mass index (BMI) is calculated by person's weight in kilograms dividing by the square of the person's height in meters. 
# The interpretation of BMI for people of 18 years and older is as follows:
# 
#         BMI below 18.5:                                 Underweight
#         BMI between 18.5 and 24.9 (both inclusive):     Normal
#         BMI between 25.0 and 29.9 (both inclusive):     Overweight
#         BMI of 30.0 and above:                          Obese
#         
# Write a program that displays the BMI and the corresponding interpretation for the weight and height specified by the users.

weight = float(input('Please enter your weight in Kilogrms:'))
height = float(input('Please enter your height in meters:'))

BMI_Index = weight / (height**2)

if BMI_Index < 18.5:
    print ('Your Body Mass Index is:', BMI_Index, 'You are Underweight!')
elif BMI_Index <= 24.9:
    print ('Your Body Mass Index is:', BMI_Index, 'You have Normal weight!')
elif BMI_Index <= 29.9:
    print ('Your Body Mass Index is:', BMI_Index, 'You are Overweight.')
else:
    print ('Your Body Mass Index is:', BMI_Index, 'You have obese.')


## while loop

# Write a program that converts from miles to kilometers for 1 to 100 miles. 

x = 1

while x <= 100:
    miles= 1.609*x
    print (x, 'miles is equivalent to', miles , 'kilometers.')
    x+=1


# Write a program using a while loop, which finds the greatest common divisor of two positive integers. 
# The greatest common divisor of two +integers, is the greatest int such that the remainder when dividing both by it is 0.

x = 15
y = 35
z = x
while z > 0:
    if (x % z == 0) and (y % z == 0):
        print ('the greatest common divisor of', x, 'and', y, 'is:', z)
        break
    z -= 1
