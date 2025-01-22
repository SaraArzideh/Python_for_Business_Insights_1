## for loop, list comprehension, lambda expression and the map() function

# Write a program which can convert a given list of temperatures in Celsius to Fahrenheit. 
# The conversion formula between Celsius (C) and Fahrenheit (F) is : F = 1.8 * C + 32

# Method 1: for loop

# Test list:
temperature_c = [39.2, 36.5, 37.3, 37.8]

temprature_f = []
for c in temperature_c:
    temprature_f.append(c*1.8 + 32)
print (temprature_f)

# Method 2: list comprehension

# Test list:
temperature_c = [39.2, 36.5, 37.3, 37.8]

temprature_f = []
[temprature_f.append(c*1.8 + 32) for c in temperature_c]
print (temprature_f)

# Method 3: lambda expression and the map() function together 

# Test list:
temperature_c = [39.2, 36.5, 37.3, 37.8]

list (map(lambda c : c*1.8 + 32, temperature_c))


# Write a program, which filters out the even numbers of the given list, and saves the odd numbers in a new list.

# Method 1: for loop

# Test list:
test_list = range(11)

odd_list = []
for num in test_list:
    if num %2 != 0:
        odd_list.append(num)
print (odd_list)

# Method 2: list comprehension

# Test list:
test_list = range(11)

odd_list = []
[odd_list.append(num) for num in test_list if num % 2 != 0]
print (odd_list)

# Method 3: list comprehension combined by a lambda expression

# Test list:
test_list = range(11)

list (filter(lambda num: num%2 != 0, test_list))


# Write a program that returns a list of four tuples, with each tuple consisting of:one order number, the corresponding book title and the overall cost.
# In each nested list, there are five values, which are: [Order Number, Book Title, Author, Quantity, Price per Item]

orders = [ ["34587", "Learning Python",       "Mark Lutz",   4, 40.95], 
           ["98762", "Programming Python",    "Mark Lutz",   5, 56.80], 
           ["77226", "Head Firstbb Python",   "Paul Barry",  3, 32.95], 
           ["88112", "Einführung in Python3", "Bernd Klein", 3, 24.99] ]

# Method 1: for loop

list_of_tuples = [] 
for order in orders:
    list_of_tuples.append((order[0], order[1], round(order[3] * order[4], 2)))
print (list_of_tuples)

# Method 2: List comprehension

list_of_tuples = []
[list_of_tuples.append((order[0], order[1], round(order[3] * order[4], 2))) for order in orders]
print (list_of_tuples)

# Method 3: Combination of a lambda expression and the map() function:

list (map(lambda order:(order[0], order[1], round(order[3] * order[4], 2)) , orders))


# Write a function which returns a list of boolean values indicating whether the corresponding element of list is greater than the given number.

# Method 1: for loop

def elementwise_greater_than_version_1(l, n):
    """
    Return a list with the same length as l, where the value at index i is 
    True if l[i] is greater than n, and False otherwise.
    """
    result = []
    for num in l:
        result.append(num > n)
    return result

# test the function:
elementwise_greater_than_version_1([1, 2, 3, 4, 5], 2)

# Method 2. list comprehension

def elementwise_greater_than_version_2(l, n):
    """
    Return a list with the same length as l, where the value at index i is 
    True if l[i] is greater than n, and False otherwise.
    """
    return [num>n for num in l]    

# Test the function:
elementwise_greater_than_version_2([1, 2, 3, 4, 5], 2)

# Method 3: # lambda expression

def elementwise_greater_than_version_3(l, n):
    """
    Return a list with the same length as l, where the value at index i is 
    True if l[i] is greater than n, and False otherwise.
    """
    return list(map(lambda num: num>n , l))
    
# Test the function:
elementwise_greater_than_version_3([1, 2, 3, 4, 5], 2)
