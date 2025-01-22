

# Question 1.
# Write a function, which takes the year as a four digit integer and returns True if the input year is a leap year, and False otherwise.

# The rules to determine a leap year:
#  - Any year that is divisible by 400 is a leap year.
#  - Of the remaining years, any year that is divisible by 100 is not a leap year.
#  - Of the remaining years, any year that is divisible by 4 is a leap year.
#  - All other years are not leap years.

def leap_year (year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

year = int (input("Please enter a year"))
print(leap_year(year))

# Test the function
not_leap_year_list = [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600, 2700, 2900, 3000]
print(list(map(leap_year, not_leap_year_list)))

leap_year_list = [1600, 2000, 2400, 2800, 1992, 2008]
print(list(map(leap_year, leap_year_list)))
    

# Question 2.
# Write a function that determines how many days there are in a given month of a given year. 

number_of_days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
number_of_days_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_a_month(month, year):
    def leap_year (year):
        if year%400 == 0:
            return True
        elif year%100 == 0:
            return False
        elif year%4 == 0:
            return True
        else:
            return False
     
    if leap_year(year) == True:
        return number_of_days_in_leap_year[month-1]
    else:
        return number_of_days_in_year[month-1]            
    
month = int (input("please enter the month as an integer between 1 to 12"))
if 0 < month < 13:
    year = int (input ("Please enter a year"))
    if 0 < year:
        print (days_in_a_month(month, year))
    else:
        print("the entered year is not valid!")
else:
    print("Month must be an integer between 1 and 12!")


# Test the function:
print(list(map(days_in_a_month, range(1,13), [2200] * 12)))
print(list(map(days_in_a_month, range(1,13), [2008] * 12)))


# Question 3.
# Write a function, which asks a month and the day within the month and returns the name of the corresponding season.
# that corresponds to the given input date.

# starting dates for each season:
# - Spring: March 20
# - Summer: June 21
# - Autumn: September 22
# - Winter: December 21

def find_the_season(month, day):
    month = month.lower()
   
    if month == "march":
        if day > 19:
            return "Spring"
        else:
            return "Winter"
    if month in ["april", "may"]:
        return "Spring"

    
    if month == "june":
        if day > 20:
            return "Summer"
        else:
            return "Spring"
    if month in ["july", "august"]:
        return "Summer"

    
    if month == "september":
        if day > 21:
            return "Autumn"
        else:
            return "Summer"
    if month in ["october", "november"]:
        return "Autumn"
   
    if month == "december":
        if day > 20:
            return "Winter"
        else:
            return "Autumn"
    if month == "january" or month == "february":
        return "Winter"
        
        
days_in_month = {
    "january": 31, "february": 29, "march": 31, "april": 30, "may": 31, "june": 30, 
    "july": 31,"august": 31, "september": 30, "october": 31, "november": 30, "december": 31
}

month = input("Please enter the name of month:")
day= int(input("Please enter the day:"))

month_lower = month.lower()

if month_lower in days_in_month and 1 <= day <= days_in_month [month_lower]:
    print(find_the_season(month, day))
else:
    print("The entered date is not valid!")

# Test the function
test_cases = [
    ("March", 19, "Winter"),
    ("March", 20, "Spring"),
    ("March", 21, "Spring"),
    ("June", 20, "Spring"),
    ("June", 21, "Summer"),
    ("June", 22, "Summer"),
    ("September", 21, "Summer"),
    ("September", 22, "Autumn"),
    ("September", 23, "Autumn"),
    ("December", 20, "Autumn"),
    ("December", 21, "Winter"),
    ("December", 22, "Winter"),

    ("January", 15, "Winter"),
    ("February", 28, "Winter"),
    ("April", 10, "Spring"),
    ("May", 25, "Spring"),
    ("July", 4, "Summer"),
    ("August", 17, "Summer"),
    ("October", 31, "Autumn"),
    ("November", 26, "Autumn"),

    ("February", 29, "Winter"),
    ("April", 30, "Spring"),
    ("June", 30, "Summer"),
    ("September", 30, "Autumn"),

    ("march", 20, "Spring"),
    ("JUNE", 20, "Spring"),
    ("SePtEmBeR", 22, "Autumn"),
    ("DECEMBER", 21, "Winter"),
    ("january", 1, "Winter"),
    ("AuGuSt", 15, "Summer"),
    ("oCtoBer", 31, "Autumn"),
    ("MaY", 15, "Spring"),
]

def test_find_the_season():
    for month, day, expected_season in test_cases:
        assert find_the_season(month, day) == expected_season, f"Failed test for {month} {day}"
    print("All tests passed!")

test_find_the_season()


# Question 4.
# Write a function which takes a string of Morse code and returns the corresponding text as a string, using the following dictionary.

morse_to_latin_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', \
                       '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', \
                       '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', \
                       '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', \
                       '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', \
                       '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', \
                       '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', \
                       '...--': '3', '....-': '4', '.....': '5', '-....': '6', \
                       '--...': '7', '---..': '8', '----.': '9', '-----': '0', \
                       '--..--': ',', '.-.-.-': '.', '..--..': '?', '-.-.-': ';', \
                       '---...': ':', '-..-.': '/', '-....-': '-', '.----.': "'", \
                       '-.--.-': '(', '..--.-': '_', '-.-.--': '!'}

# Note: The Morse character '-.--.-' represents '(', ')', '[', ']', '{' or '}'.

def morse_to_text(string_code):
    text = ""
    words = string_code.split("    ")
    for word in words:
        morse_codes = word.split()
        for code in morse_codes:
            text += morse_to_latin_dict[code]
        text += " "
    return text
    
string_code= input("Please enter a string of Morse codes:")    
print (morse_to_text(string_code))

# Test the function
print(morse_to_text('.... ..    - .... . .-. . -.-.--'))
print(morse_to_text('.-    ... . .-. .. . ...    --- ..-.    -.. --- - ...    .- -. -..    -.. .- ... .... . ...    .. ...    -- --- .-. ... .    -.-. --- -.. . .-.-.-'))


# Question 5.
# Write a function that takes one positive number and returns its square root, utilizing the Babylonian technique.

# The Babylonian technique:
#   It approximates the square root of a positive number, repeating a calculation using the following formula:
#        next_guess = (last_guess + (n / last_guess)) / 2
#   When next_guess and last_guess are almost identical, next_guess is the approximated square root.

def babylonian(number):
    last_guess= 1
    diff = 1.0  # Initializing with a value greater than 0.0001 to start the while loop!
    while diff > 0.0001:
        next_guess = (last_guess + (number / last_guess)) / 2
        diff = abs(next_guess - last_guess)
        last_guess = next_guess
    return next_guess
    
number = float (input("Please enter a positive number:"))
if number <= 0:
    print("Please enter a positive number!")
else:
    print (babylonian(number))

# Test the function
for n in range(4, 11):
    print(babylonian(n))
    
# The output looks like the following:
## 2.000000000000002
## 2.236067977499978
## 2.4494897427875517
## 2.6457513111113693
## 2.8284271250498643
## 3.000000001396984
## 3.162277660168379
