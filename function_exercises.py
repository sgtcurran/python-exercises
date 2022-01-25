#%%
#1
from curses.ascii import isdigit
from doctest import OutputChecker
from email import charset

from numpy import cumproduct, index_exp


def is_two(x):
    if x == 2 or x =='two': # if conditon x is == 2 or str 'two' 
        return True #returns true
    else:
        return False
x = 2
x1 = 'two'
x2 = 5

print(is_two(x))
print(is_two(x1))
print(is_two(x2))
# %%
#2
def is_vowel(char): # char = characters 
    result = char.lower() in 'aeiou' #results = character.lower() in 'aeiou'
    return result
     

x = 'dfhdfh'
x1 = 'aeiou'
x2 = 'a'
print(is_vowel(x))
print(is_vowel(x1))
print(is_vowel(x2))
# %%
#3
def is_consonant(char): #variable is any character
    return char.lower() in 'zbtgh' # if character is lower return true if 
x = 'zbtgh' #x is a string 
x1 = 'hi'
print(is_consonant(x))
print(is_consonant(x1))

# %%
#4
# 
def upper_con(string):
    if type(string) != str: # if type of string is not equal to string return false
        return False
    first_letter = string[0] # variable is first letter & placement 0
    if is_consonant(first_letter): # calls is_consonant function applies variable first_letter
        string = string.capitalize() # string = string.capitalize() makes first letter capitalize
        return string #return if a consonant and makes the first letter capitalize
            
str1 = 'zebra'
str2 = 'apple'
str3 = 'boat'
print(upper_con(str1))
print(upper_con(str2))
print(upper_con(str3))
# %%
#5 user based input of bill plus 20% tip
#Tip is the fixed variable of 0.20 & user_input must be a float or an error
#mesage will occur. 
user_input=float(input('enter total bill to get tip'))
def calculate_tip(tip):
    tip = 0.20
    
    return float(tip*user_input)+user_input
#return function is 0.20 * input + user_input to get correct output
print('bill plus 20% tip =', calculate_tip(user_input))
#%%
#6
def apply_discount(discount_total):
    discount_total = (price * discount)
    total = (price - discount_total)
    return total
discount = .20
price = 10
print('price = $10 Discount - 20% = ', apply_discount(discount))

# %%
#7 accept a string that is a number that contains 
# commas in it as input, and return a number as output
def handle_commas(string):
    s = string.replace(',','')
    return s

string = ('one, two, three, four, five')

print('remove comas from string:', handle_commas(string))
# %%
#8 accept a string that is a number that contains 
# commas in it as input, and return a number as output

def get_letter_grade(grade):
    if grade >= 90:
        return "A" 
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
        
grade1 = 65 # variable

print('Grade:', get_letter_grade(grade1)) # print function of get_letter_grand and independant varible 
    
# %%
#9 accepts a string and returns a string with all 
# the vowels removed.
import re
#import re (regular expression) & use re.sub to remove str elements
def remove_vowels(vowels):
    return (re.sub("[aeiouAEIOU]","", vowels))
vowels1 = 'I came, I saw, I got blown up'

print('I came, I saw, I got blown up','=', remove_vowels(vowels1))
# %%
#10 
# user inputs string 
string = input('Enter your first name').lower() #converts string input to lower case
def normalize_name(string):
    output = '' #output 
    for character in string: # for characters in string 
        if character.isidentifier() or character == ' ':#isidentifier() returns true if valid identifier or character == ' '
            output += character
    output = output.strip() #.strip removes whitespace
    output = output.replace(' ', '_') #.replace whitespace between strings & adds _

    return output
print(normalize_name(string))
    
# %%
#11
import numpy as np 
# import numpy as np to use tool cumsum
def cumulative_sum(list):# variable is any list
    return np.cumsum(list) # return numpy cumsum of any list

print(cumulative_sum([1, 1, 1]))
print(cumulative_sum([1, 2, 3, 4]))
# %%

