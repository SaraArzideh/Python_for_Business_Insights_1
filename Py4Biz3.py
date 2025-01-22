## for loop

# Write a program that converts from miles to kilometers for 1 to 100 miles.

for miles in range(1,101):
    print (miles, 'miles is equivlent to', round(miles*1.069, 3), 'kilometers.')


# Count the number of even numbers in 0,1,2,,...,8,9,10

count=0
for num in range (11):
    if num%2 == 0:
        count+=1
print ('The number of even numbers between o and 10 is', count)


# Write a program that calculates the average of the integer values in the list of different types of objects.

# Test list:
l = [1, 'nine', 3.56, 8, 14, [1,2], 6, 'list']

sum_of_integers=0
count_of_integers=0
for i in l:
    if type(i)==int:
        count_of_integers += 1
        sum_of_integers += i
print ('The average of the integer values in the given list is:', sum_of_integers/count_of_integers)



# Write a program that print out all the words of a given sentence that start with a letter 's'.

## Test sentence:
s = 'This is the sentence to be used to test your solution to this problem.'

l= s.split()
for word in l:
    if word[0]== "s" or word[0]== "S":
        print (word)
        

## Lists

# Write a program that creates a list, containing all the proper divisors of a positive integer specified by the user.
# The proper divisors of a positive integer n are the positive divisors of n other than n itself. 

number= int(input('Please enter a positive integer'))
list_of_proper_divisors=[1, number]
for i in range (2, number):
    if number % i == 0:
        list_of_proper_divisors.append(i)

list_of_proper_divisors.sort()
print ('The proper divisors of', number, 'are:', list_of_proper_divisors)


# Write a program that displays the distinct numbers of a given list of numbers (if a number appears multiple times, it is displayed only once).

# Test list:
test = [30,0,20,3,2,2,2,2,20,1,2,3,4,5,5,5,6,7,7,7,8,9,10]

new_list = []
for i in test:
    if i not in new_list:
        new_list.append(i)
print (new_list)



# Write a program that checks whether two given words are anagrams. Two words are anagrams if they contain the same letters. For example, "silent" and "listen" are anagrams, and "keen" and "knee" are also anagrams.

word_1= input ('Plesae insert first word')
word_2= input ('Plesae insert second word')

list_1= list(word_1.lower())
list_1.sort()
list_2= list(word_2.lower())
list_2.sort()

if list_1 == list_2:
    print (word_1, 'and', word_2,'are anagrams')
else:
    print (word_1, 'and', word_2,'are not anagrams')
