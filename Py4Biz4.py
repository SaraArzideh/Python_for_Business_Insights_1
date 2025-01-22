## Functions
 
# Write a function, even_number(), which returns the number of even numbers in the given integers list. 

def even_number (integers_list):
    count = 0
    for num in integers_list:
        if num % 2 == 0:
            count +=1
    return count

# Test the function:
even_number(list(range(1, 101)))  
 
# Write a function, which checks whether the given list has any odd number in it, returning True, otherwise False.

def any_odd_number(num_list):
    for num in num_list:
        if num % 2 ==1:
            return 'True'
    return 'False'

# Test the function:
print(any_odd_number([2,4,3,8,10]))  ## True
print(any_odd_number([2,4,6,8,10]))  ## False


# Write a function, which checks whether the input number is prime (divisible only by 1 and itself), returning True, otherwise False.

def is_prime(argument):
    for num in range(2, argument):
        if argument % num == 0:
            return 'False'
    return 'True'

# Test the function:
for number in range(2, 21):
    print("Is", number, "prime?", is_prime(number))


# Write a function, which prints out all twin primes less than the given positive number. 
# Twin primes are a pair of prime numbers that differ by 2. For example, 3 and 5, 5 and 7, and 11 and 13 are twin primes. 

def twin_primes(positive_integer):
    for num in range (2, positive_integer):
       if is_prime(num) == 'True':
           if is_prime(num+2) == 'True':
               print(num, 'and', num+2)

# Test the function:
twin_primes(1000)  ## The output should contain 35 pairs of prime numbers.


# Write a function, which can translate a text to Morse code, using the given dictionary

latin_to_morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', \
                       'E':'.', 'F':'..-.', 'G':'--.','H':'....', \
                       'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', \
                       'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', \
                       'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', \
                       'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', \
                       'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', \
                       '3':'...--', '4':'....-', '5':'.....', '6':'-....', \
                       '7':'--...', '8':'---..', '9':'----.', '0':'-----', \
                       ',':'--..--', '.':'.-.-.-', '?':'..--..', ';':'-.-.-', \
                       ':':'---...', '/':'-..-.', '-':'-....-', '\'':'.----.', \
                       '(':'-.--.-', ')':'-.--.-', '[':'-.--.-', ']':'-.--.-', \
                       '{':'-.--.-', '}':'-.--.-', '_':'..--.-', '!':'-.-.--'}

## Note: '(', ')', '[', ']', '{' and '}' have the identical Morse character '-.--.-'

def text_to_morse(string):
    morse_code = ''
    for character in string:
        if character == ' ':
            morse_code += '    '
        else:
            character = character.upper()
            morse_code += latin_to_morse_dict[character]
            morse_code += ' '
    return morse_code


# Test the function with the following texts:
text_to_morse('Hi there!')

## '.... ..    - .... . .-. . -.-.--'

text_to_morse('Programming for Analytics')

## '.--. .-. --- --. .-. .- -- -- .. -. --.    ..-. --- .-.    .- -. .- .-.. -.-- - .. -.-. ...'


# Write a function, which determines whether or not a password is good. 
# A good password has at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one number. 
# 
# Hint: The way the computer knows that characters like uppercase and lowercase letters are different, is that 
# each character is assigned a unique integer value, which is called the **Ordinal Value**. 
# For example, “A” is 65, “B” is 66, “a” is 97, “b” is 98, and “1” is 49.

# Check the ordinal values for some charaters:
alphabet = ['A','B','C','D','E','a','b','c','d','e','1','2','3','4','5']

for letter in alphabet:
    print('The ordinal value of', letter, 'is', ord(letter))

print('\n')
print('A' < 'B')
print('A' < 'a')
print('1' < '2')


# Solution

def good_password(argument):

        
    length_checker = False
    upper_checker = False
    lower_checker = False
    digit_checker = False
            
    if len(argument) >= 8:
        length_checker = True
        
    for letter in argument:
        if 'A'<= letter <= 'Z':
            upper_checker = True
        
        elif 'a'<= letter <= 'z':
            lower_checker = True
            
        elif '0' <= letter <= '9':
            digit_checker = True
            
        if  length_checker and upper_checker and lower_checker and digit_checker:
            return 'True'
            
    return 'False'


# Test the solution:
print(good_password('Rtyy8yyrtht65'))  ## True
print(good_password('Rtyy8yyrtht_!'))  ## True
print(good_password('Rtyy8'))          ## False
print(good_password('Rtyyyyyyy'))      ## False
print(good_password('rtyy88888'))      ## False
print(good_password('R88888888'))      ## False 
print(good_password('Rt-----_!'))      ## False
