
##  Question 1.
# Write a program that starts by taking an integer as seconds, then displays the equivalent amount of time in the format of D:H:M:S 

number_of_seconds = int(input('Please enter an integer number of seconds:'))

if number_of_seconds < 0:
    print ('you entered an unvalid number.')
else:
    days= number_of_seconds // (24*60*60)
    remained_seconds= number_of_seconds % (24*60*60)
    
    hours= remained_seconds // (60*60)
    remained_seconds= remained_seconds % (60*60)
    
    minutes= remained_seconds // 60
    
    seconds= remained_seconds % 60

    print (number_of_seconds,'seconds is equivalent to', days, ':', hours, ':', minutes, ':', seconds, '.')


# Question 2.
# Write a program that displays the total admission cost for the group, giving a list of the ages of a group.
# Price of admission based on the age of the visitor is:
#  - 2 years old or less :             No charge.
#  - 3 and 12 years (both inclusive):  14 euro.
#  - 65 years or over :                18 euro.
#  - Others :                          23 euro.

# Test list of ages 
age_list = [3, 33, 42, 70, 65, 1, 10]  

total_cost = 0
for age in age_list:
    if age <= 2:
        total_cost += 0
    elif age >= 3 and age <= 12:
        total_cost += 14
    elif age >= 65:
        total_cost += 18
    else:
        total_cost += 23
        
print ('The total admission cost is', total_cost, 'euros.')


# Question 3.
# 
# Write a program that takes a word from the user and displays the Scrabble score for this word.
# In the Scrabble game, each letter has points associated with it, which are given below as a dictionary. 
# The total score of a word is the sum of the scores of its letters.

letter_to_point = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, \
                   "G":2, "H":4, "I":1, "J":2, "K":5, "L":1, \
                   "M":3, "N":1, "O":1, "P":3, "Q":10,"R":1, \
                   "S":1, "T":1, "U":1, "V":4, "W":4, "X":8, \
                   "Y":4, "Z":10}

word = input ('Please enter a word:')
upper_word = word.upper()

points = 0

for letter in upper_word:
    points = points + letter_to_point[letter]

print ('the Scrabble score for "', word, '" is', points, '.')


# Question 4.
# Write a program that asks to enter the amount of deposit into the savings account each month, the annual interest rate (as a decimal),
# and the number of months, and then displays the amount in the savings account after the given month. 

deposit = float(input ('Please enter the monthly deposit amount:'))
interest = float(input ('Please enter the annual interest rate (as a decimal):')) 
months = int (input ('Please enter the number of months:'))
if deposit < 0 or interest < 0 or months<0:
    print('All inputs should be non_negative')
else:
    saving = 0
    for month in range (1, months+1):
        saving = (deposit + saving) * (1 + (interest/12))
        saving = round (saving,3)
        
    print('The amount in the saving account after', months, 'months, will be', saving )


# Question 5.
# Write a program to find all the Armstrong numbers that are between 0 and 9999 (both inclusive).
# An Armstrong number (also known as a narcissistic number) is a positive integer that is equal to the sum of its own digits, each
# raised to the power of the number of digits in the integer.

list_of_armstromng_nums = []

for number in range (0,10000):
    digits_list = list (str(number))
    
    power = len(digits_list)
        
    sum_of_powered_digits = 0
    
    for digit in digits_list:
        digit = int (digit)
        sum_of_powered_digits = sum_of_powered_digits + (digit** power)
        
    if number == sum_of_powered_digits:
        list_of_armstromng_nums.append(number)

print ('The Armstrong numbers between 0 and 9999 are:', list_of_armstromng_nums)


# Question 6.
# Extract 'hello' from the following nested dictionary using indexing.

nested_dict = {'level_1':[1, 'two', 3.0, '4', {'level_2_1':'not there yet', 'level_2_2':['one', {'getting close':{'almost there':[('so close now', 'not yet'), ('finally','hello')]}}]}]}

## Your program starts from here:
last_item = nested_dict ['level_1'][4]['level_2_2'][1]['getting close']['almost there'][1][1]

print (last_item)
