from calendar import THURSDAY, WEDNESDAY
from pickle import FALSE
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
    print("it is a weekday")
if user_input == 'saturday'or'sunday':
    print('it the weekend')

# %%
#pay calulator w/overtime
User_Input = float(input('how hours worked in one week'))

if User_Input:
    Rate = 33.38 
    if User_Input <= 40:
        GrossPay = Rate*User_Input
        print("Gross Pay: $", GrossPay)
    else:
        RegularPay = Rate*40
        OverTime = User_Input-40
        OverTimeRate = Rate*1.5
        OverTimePay = OverTimeRate*OverTime
        GrossPay = RegularPay+OverTimePay
        print("Gross Pay: $", GrossPay)
        



# %%
#2 Loop Basics 
i = 5
while i <= 15:
    print(i)
    i += 1

# %%
i = 0
while <= 100:
    print(i)
    i += 2
#%% 
i = 100
while i >= -10:
    print(i)
    i -= 5

# %%
