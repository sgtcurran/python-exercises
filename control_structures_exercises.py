from calendar import THURSDAY, WEDNESDAY
from cmath import sqrt
from pickle import FALSE

#%%
#Conditional Statements 
#prompt the user for a day of the week, print out whether the day is Monday or not
user_input = input('What day of the week is it?').lower()

if user_input == 'monday': 
    print("It is monday")
else:
    print("It is not monday")


#%%
#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
user_input = input('What day of the week is it?').lower()

if user_input == 'monday'or'tuesday'or'wednesday'or'thursday'or'friday':
    print('it is a weekday')

if user_input == 'saturday'or'sunday':
    print('it the weekend')

# %%
#pay calulator w/overtime
user_input = float(input('how hours worked in one week'))

if user_input:
    rate = 33.38 
    if user_input <= 40:
        grosspay = rate*user_input
        print('Gross Pay: $', grosspay)
    else:
        regularpay = rate*40
        overtime = user_input-40
        overtimerate = rate*1.5
        overtimepay = overtimerate*overtime
        grosspay = regularpay+overtimepay
        print('Gross Pay: $', grosspay)
        

# %%
#2 Loop Basics 
i = 5
while i <= 15:
    print(i)
    i += 1

# %%
i = 0
while i <= 100:
    print(i)
    i += 2
#%% 
i = 100
while i >= -10:
    print(i)
    i -= 5

# %%
i = 2
while i <= 1000000:
    print(i)
    i = i**2
# %%
i = 100
while i >= 5:
    print(i)
    i -= 5
# %%
#For Loops
#i
User_Input = int(input('multiplication table up through 10'))
if int(User_Input) > 0:
    for i in range(1, 11):
        print(User_Input, '*', i, '=', (User_Input*i))
# %%
num = 9
for i in range (1, num+1):
    for j in range(1, i+1):
          print(i, end="")
    print()
    
# %%
# break and continue
while True:
    User_Input = input('enter odd number between 1 & 50')
    if User_Input.isdigit():
        if int(User_Input) % 2 == 1 and int(User_Input) <= 50:
            break
User_Input = int(User_Input)
for i in range(1, 50, 2):
    print(i)
    if i == User_Input:
        print('skip odd number:', i)
    else:
        print('here is an odd number')
#%%    
# user to enter a positive number and write 
# a loop that counts from 0 to that number
while True:
    user_input = input('enter positive number')
    if user_input.isdigit():
        if int(user_input) > 0:
            break
user_input = int(user_input)
for i in range(1000):
    print(i)
    if i == user_input:
        break
#%%
while True:
    user_input = input('enter positive integer')
    if user_input.isdigit():
        if int(user_input) > 0:
            break


user_input = int(user_input)
for i in range(user_input, 0, -1):
    print(i)
    
# %%

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
# %%
while True:
    user_input = input('enter an integer')
    if user_input.isdigit():
        if int(user_input) > 0:
            break
user_input_cont = input('do you want to continue & print table')
if user_input_cont.lower().startswith('y'):
    user_input = int(user_input)
    print()
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1, user_input + 1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: <6} | {i_squared: ^7} | {i_cubed: 5}')
    
    
# %%
