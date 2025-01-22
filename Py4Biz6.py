
## NumPy

import numpy as np
import matplotlib.pyplot as plt


# Question1: 
# Do the followings for this NumPy array: np.array([3,4,6,10,24,89,45,43,46,99,100])

arr = np.array([3,4,6,10,24,89,45,43,46,99,100])

# Extract the numbers which are not divisible by 3
arr_3 = arr%3
arr_3_boolean = arr_3==0
print (arr[arr_3_boolean])

# Extract the numbers which are divisible by 5
arr_5 = arr%5
arr_5_boolean = arr_5==0
print (arr[arr_5_boolean])


# Set the numbers which are divisible by 3 to 0
arr_3 = arr%3
arr_3_boolean = arr_3==0

new_arr = np.where(arr % 3 == 0, 0, arr)
print (new_arr)

# Question2: 
# Write a function to calculate and return the frequency of having a head after tossing a fair coin for a given number of times.  

def frequency_of_head(no_of_toss):
    tosses = np.random.randint (0, 2 , no_of_toss)
    frequency = np.sum (tosses == 1) / no_of_toss
    return frequency
                
no_of_toss = int(input("please enter the number of times"))
frequency = frequency_of_head(no_of_toss)

print ("the frequency of head after", no_of_toss, "times of tosses is:", frequency)

# Test the function
print(frequency_of_head(10))
print(frequency_of_head(100))
print(frequency_of_head(100000))

# Question3: 
# In order to win the top prize in a particular lottery, one must match all 6 numbers on their ticket to the 6 integers 
# between 1 and 49 that are drawn by the lottery organizer. 
# Write a function that generates a random selection of 6 numbers for a lottery ticket, which do not contain any duplicates.
# Your function should return the numbers in ascending order.

def lottery_ticket():
    lottery_num_arr = np.array([])
    
    while len(lottery_num_arr) < 6:
        # Generating a random number between 1 and 49
        random_num = np.random.randint(1, 50)
        
        # Adding the number if it's not already in the array
        lottery_num_arr = np.unique(np.append(lottery_num_arr, random_num))
    
    lottery_num_arr = np.sort(lottery_num_arr)
    return lottery_num_arr

print("lottery ticket number is:", lottery_ticket())

# Test the function
for i in range(10):
    print(lottery_ticket())


## matplotlib

# Question1: 
# Create a line plot for the Nominal GDP of Country A.
# The Normal GDP of Country A between 1950 and 2010 is as follows:
#     gdp_a = np.array([300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3])

gdp_a = np.array([300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3])
years = np.array ([1950, 1960, 1970, 1980, 1990, 2000, 2010])

plt.plot (years, gdp_a, marker = ".")

plt.xlabel ("Year")
plt.ylabel ("Billions of US dollars")
plt.title ("Nominal GDP of Country A")

plt.show()


# Question2:
# Create a line plot for the Nominal GDP of Country A, B and C.
# The Normal GDP of Country A, B and C between 1950 and 2010 is given as follows:
#     gdp_a = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#     gdp_b = [226.0, 362.0, 928.0, 1992.0, 4931.0, 7488.0, 12147.0]
#     gdp_c = [1206.0, 1057.0, 1081.0, 2940.0, 8813.0, 13502.0, 19218.0]

gdp_a = np.array([300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3])
gdp_b = [226.0, 362.0, 928.0, 1992.0, 4931.0, 7488.0, 12147.0]
gdp_c = [1206.0, 1057.0, 1081.0, 2940.0, 8813.0, 13502.0, 19218.0]

years = np.array ([1950, 1960, 1970, 1980, 1990, 2000, 2010])

plt.plot (years, gdp_a, marker = "o", linestyle = "-", color = "b", label = "Country A")
plt.plot (years, gdp_b, marker = "*", linestyle = ":", color = "r", label = "Country B") 
plt.plot (years, gdp_c, marker = "D", linestyle = "-.", color = "g", label = "Country C")

plt.xlabel ("Year")
plt.ylabel ("Billions of US dollars")
plt.title ("Nominal GDP of Country A")

plt.legend ()
plt.show()


# Question3:
# Create bar plots for movies and the number of Oscars they won:
# The movie names and the number of Oscars they each won are given as follows:
#     movie = np.array(["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"])
#     num_oscars = np.array([5, 11, 3, 8, 10])

movie = np.array(["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"])
num_oscars = np.array([5, 11, 3, 8, 10])

plt.bar (movie, num_oscars)

plt.title ("Classic Movies")
plt.ylabel ("#of Academy Awards")

plt.show()

plt.title ("Classic Movies")
plt.xlabel ("#of Academy Awards")
plt.barh (movie, num_oscars)
plt.show ()


# Question4:
# Create a scatter plot which displays the activities of 9 users on an anonymous social networking site. 
# The scatter plot shows the relation between the number of users' friends on the site and the average minutes they spent there daily.
# The number of their friends and the average daily time they spent on the site are given as follows:
#     no_of_friends = np.array([ 70, 65, 72, 63, 71, 64, 60, 64, 67])
#     avg_daily_time = np.array([175, 170, 205, 120, 220, 130, 105, 145, 190])

no_of_friends = np.array([ 70, 65, 72, 63, 71, 64, 60, 64, 67])
avg_daily_time = np.array([175, 170, 205, 120, 220, 130, 105, 145, 190])

plt.scatter (no_of_friends, avg_daily_time)

plt.title ("Daily minutes vs. Number of friends")
plt.xlabel ("Number of friends on the site")
plt.ylabel ("Average daily time (in minutes) spent on the site")

plt.show()
