#%%
#1
from itertools import accumulate
from function_exercises import is_vowel

# %%
#1b
from function_exercises import calculate_tip
user_input = 100.25
print(calculate_tip(user_input))
# %%
#2a 
import itertools 


list1 = ['abc']
list2 = ['123']
list3 = [['abc123']]
print(list(map(''.join, itertools.product(list1, list2))))
print(list(itertools.chain.from_iterable(list3)))
# %%
#2 12 permutations 
import itertools 

list1 = 'abc'
list2 = '123'
list3 = list('abcd')
#


print(list(itertools.permutations(list3, 2)))
# %%
# 6 combinations
import itertools

list3 = 'abcd'
print(list(itertools.combinations(list3, 2)))
# %%
