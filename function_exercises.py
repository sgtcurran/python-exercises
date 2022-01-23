#%%
#1
from curses.ascii import isdigit
from email import charset


def is_two(x):
    if x == 2 or x =='two':
        return True
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
def is_vowel(char):
    result = char.lower() in 'aeiou'
    return result
     

x = 'dfhdfh'
x1 = 'aeiou'
x2 = 'a'
print(is_vowel(x))
print(is_vowel(x1))
print(is_vowel(x2))
# %%
#3
def is_consonant(char):
    return char.lower() in 'zbtgh'
x = 'zbtgh'
x1 = 'hi'
print(is_consonant(x))
print(is_consonant(x1))

# %%
#4

def upper_con(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
        return string 
     
#if x =='z'or'b'or't'or'g'or'h'or'Z'or'B'or'T'or'G'or'H':    
#char.upper()
        
str1 = 'zebra'
str2 = 'apple'
str3 = 'boat'
print(upper_con(str1))
print(upper_con(str2))
print(upper_con(str3))
# %%
#5
user_input=float(input('enter total bill to get tip'))
def calculate_tip(tip):
    tip = 0.20
    
    return float(tip * user_input) + (user_input)

print('bill plus tip =', calculate_tip(user_input))



#%%
#6
def apply_discount(price, discount):
    discount = price * discount
    return discount 
dis = .20

print(10, .5, apply_discount)
# %%
