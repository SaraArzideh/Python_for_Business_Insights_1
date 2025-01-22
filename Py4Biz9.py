## Moving Average

import numpy as np
import matplotlib.pyplot as plt

# Question 1. 
# Write a function that perform moving average forecasting (k) on a list, print forecasted values and total squared error.

# Moving average (k=2) for time series forecasting:
# 1. Initialize L_f with the first two values of L: L_f[0] = L[0], L_f[1] = L[1].
# 2. For t >= 2, compute L_f[t] = (L[t-1] + L[t-2]) / 2.
# 3. Forecast error: e_i = L[i] - L_f[i].
# 4. Total squared error = sum of all e_i^2.
# Example: L = [6,8,4,9,3,7], L_f = [6,8,7.0,6.0,6.5,6.0], error = 31.25.

def moving_average(list_of_values, k):
    
    list_of_forcasted_values = []
    
    for i in range(k):
        list_of_forcasted_values.append(list_of_values[i])
       
    for t in range(k, len(list_of_values)):
        sum_of_previous_values = 0
        
        for n in range (1, k+1):
            sum_of_previous_values += list_of_values[t-n]
            n += 1
            
        list_of_forcasted_values.append(round(sum_of_previous_values / k, 2))
         
    total_squared_error = 0
    for i in range(len(list_of_values)):
        forecast_error = list_of_values[i] - list_of_forcasted_values[i]
        total_squared_error += forecast_error**2
        
    print (list_of_forcasted_values)
    print (total_squared_error)

# Test the function
L = [6,8,4,9,3,7]
moving_average(L, 2)
# The forecasted values and the total squared error are: [6, 8, 7.0, 6.0, 6.5, 6.0], 31.25

# Test the function again 
L = [88,44,60,56,70,91,54,60,48,35,49,44,61,68,82,71,50]

for k in range(2,5):
    moving_average(L, k)
    print("\n") 
# The forecasted values and the total squared error for each k are:
# [88, 44, 66.0, 52.0, 58.0, 63.0, 80.5, 72.5, 57.0, 54.0, 41.5, 42.0, 46.5, 52.5, 64.5, 75.0, 76.5], 3815.75
# [88, 44, 60, 64.0, 53.33, 62.0, 72.33, 71.67, 68.33, 54.0, 47.67, 44.0, 42.67, 51.33, 57.67, 70.33, 73.67], 4197.689
# [88, 44, 60, 56, 62.0, 57.5, 69.25, 67.75, 68.75, 63.25, 49.25, 48.0, 44.0, 47.25, 55.5, 63.75, 70.5], 4618.1875


# Question 2.
# Write a program to simulate a variation of the Craps dice game:
# - Roll 2 dice and check their sum.
#   - 'Lose' if sum is 2, 3, or 12 (craps). 'Win' if sum is 7 or 11 (natural).
#   - Otherwise, set the sum as the "point" and continue rolling:
#       - 'Lose' if 7 is rolled; 'Win' if the "point" is rolled again.
#       - Display results of each roll. Examples:
#          - Roll 2 + 1 = 3 -> You lose.
#          - Roll 3 + 4 = 7 -> You win.
#          - Roll 5 + 4 = 9 -> Roll again; continue until win/lose.

def crap ():
    for n in range (1, 7):
        for m in range (1, 7):
            roll_sum = n + m
            if roll_sum in [2, 3, 12]:
                print ("You rolled", n,"+", m, "=", roll_sum, "Craps, You lose!")
                print ()
            elif roll_sum in [7, 11]:
                print ("You rolled", n,"+", m, "=", roll_sum, "Natural, You win!")
                print ()
            else:
                point = roll_sum
                print ("You rolled", n,"+", m, "=", roll_sum, "Your point is",point, ". Roll again!")
                    
                for a in range (1, 7):
                    for b in range (1, 7):
                        roll_sum2 = a + b
                        if roll_sum2 == 7:
                            print ("... You rolled", a,"+", b, "=", roll_sum2, ". You lose!")
                            print ()
                        elif roll_sum2 == point:
                            print ("... You rolled", a,"+", b, "=", roll_sum2, ". You win!")
                            print ()
                        else:
                            #while (a+b != 7 and a+b != point):
                            print ("... You rolled", a,"+", b, "=", roll_sum2, ". Your point was", point, ". Roll again!")
                print ()
crap ()


# Question 3. 
# write a function to generate a EuroJackpot ticket number as follows:
# - 5 unique regular numbers (1-50) in ascending order.
# - 2 unique Euro numbers (1-12) in ascending order.
# - Print the regular and Euro numbers.

def euro_jackpot():
    jackpot_num = np.array([])
    while len(jackpot_num) < 5:
        # Generating a random number between 1 and 50
        regular_numbers =  np.random.randint(1, 51)
        # Adding the regular number if it's not already in the numbers of jackpot_num array
        jackpot_num =  np.unique(np.append(jackpot_num, regular_numbers))
    jackpot_num = np.sort(jackpot_num)

    euro_num = np.array([])
    while len(euro_num) < 2:
        # Generating a random number between 1 and 12
        euro_numbers =  np.random.randint(1, 13)
        # Adding the euro number if it's not already in the euro_num array
        euro_num =  np.unique(np.append(euro_num, euro_numbers))  
        
    jackpot_num =  np.append(jackpot_num, euro_num)  
    
    # Printing the output array of jackpot numbers during testing!
    print("jackpot numbers are:", jackpot_num)
    
    # return jackpot_num
euro_jackpot()

# Test the function
for i in range(5):
    euro_jackpot()


# Question 4.
# Plot the time series of daily stock closing prices (100 days).
# Highlight minimum (day 24, green circle) and maximum (day 59, red circle) prices.

# The closing prices for 100 days for a particular stock are given as follows:           

price = [77.0782, 70.7600, 73.3505, 68.6033, 68.6321, 65.5888, 
         63.9137, 63.9204, 59.1316, 57.3080, 56.8161, 54.2992, 
         55.9700, 53.9217, 48.6715, 45.7877, 46.2155, 41.9000, 
         38.4206, 39.5007, 37.2500, 35.7330, 33.5357, 28.1770, 
         32.4655, 35.2633, 35.8763, 76.7587, 35.1836, 37.2151, 
         35.0473, 35.6049, 41.5026, 44.3063, 45.1209, 49.9941, 
         47.8066, 44.1048, 48.4192, 50.6432, 50.9571, 52.6670, 
         63.7452, 55.3259, 56.0779, 54.5044, 57.6703, 62.1648, 
         61.9237, 61.0800, 60.9850, 66.1175, 88.5949, 72.3522, 
         72.4252, 72.2571, 72.3188, 73.2215, 77.7766, 74.5345, 
         76.2885, 71.1488, 69.7948, 73.3775, 71.2516, 69.5023, 
         71.8772, 67.6134, 68.0548, 65.8009, 95.3941, 65.5281, 
         67.0112, 65.6294, 64.7371, 63.6100, 63.2455, 60.4415, 
         61.9082, 63.3986, 58.5286, 63.2828, 62.6528, 81.0053, 
         57.9832, 56.0021, 57.5180, 59.9495, 57.3952, 54.5280, 
         56.8411, 51.3766, 73.6321, 55.2540, 49.0425, 52.8425, 
         50.0387, 49.4618, 51.5674, 52.3001]

time = list(range (1, 101))

x_values = np.array (time)
y_values = np.array (price)

max_price = np.amax(y_values)
min_price = np.amin(y_values)

index_of_max_price = price.index(max_price)
index_of_min_price = price.index(min_price)

plt.plot (x_values, y_values)
plt.scatter (x_values[index_of_min_price], np.amin(y_values), color = 'g')
plt.scatter (x_values[index_of_max_price], np.amax(y_values), color = 'r')

plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Daily Closing Prices")
plt.show()

