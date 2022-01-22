#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~                            Python Functions                            ~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Topics Covered:
# - Using Functions
# - Defining Functions
# - Function Scope
# - Lambda Function Expressions

############################### Using Functions ###############################

# Function Vocabulary
#
# - run / invoke / call
# - argument
# - return value
#%%
# We've already used some built-in functions

from ast import Lambda


type('abc')
print('Hey there!')

# TODO: take a look at the code snippet below:
max([1, 2, 3])

# What is the function name? 
# Max value (int)
# Where is the function invocation? max([1, 2, 3])
# What is the return value? 3 
# Is the highest value in list

# TODO: What will the output of the following code be? Why? Explain step-by-step
type(max([1, 2, 3]))

# TODO: What will the output of the following code be? Why?
type(max)
#%% 
# What other built-in functions do you know?

############################## Defining Functions ##############################

# Function Vocabulary
#
# - Function Definition
# - Function Name
# - Parameter
# - Function Body

def increment(n):
    return n + 1

# TODO: What is the difference between the increment function above and the one below?
def increment(n):
    print(n + 1)

# TODO: define a function named is_weekend. This function should accept a string and return true if the string is either saturday or sunday, false otherwise.
# TODO: test out your is_weekend function with various values.
# TODO: Use your is_weekend function in combination with input() and an if statement to prompt the user for a day of the week and tell them whether or not it is a weekend.

# TODO: Create a function named nonzero. It should accept a number and return true if the number is anythong other than zero, false otherwise.
# TODO: Use your nonzero function in combination with the built-in input function and an if statement to prompt the user for a number and print a message displaying whether or not the number is zero.
# TODO: Transfer the work you have done into a function named explain_nonzero. Calling this function should prompt the user and display the message as before.
#%%
def is_weekend(bool):
    if bool.str(saturday' or 'sunday'):

        return 
    else:
        return 
is_weekend('saturday')

#%%
## Default Parameter Values and Keyword Arguments ##

# - Positional Argument
# - Keyword Argument
#%%
def sayhello(name="Innis"):
    return f"Hello, {name}!"
print("",sayhello)


# TODO: call the say hello function and don't pass any arguments
# TODO: call the say hello function and pass your name as a string argument both positionally and as a keyword argument.
#%%
## Docstrings ##
def sayhello(name="Innis"):
    "Provides a friendly greeting."
    return f"Hello, {name}!"
sayhello()
# Aside: built-in help with help() (or ? in ipython)
#%%
################################ Function Scope ################################
#
# - scope refers to defining variables inside/outside of functions
# - scope defines where a variable can be referenced
# - global and local scope

# TODO: look at the example below. What do expect will happen when you run it? f is function is not defined 
def f(x):
    x = 123
f()
print(x)
#%%
# TODO: look at the example below. What do expect will happen when you run it? print function will print x = 123 
x = 123
def f():
    print(x)
f()
#%%
# TODO: look at the example below. What do expect will happen when you run it? print f function plus 1 to 12 = 13 
x = 123
def f(x):
    return x + 1
print(f(12))

# TODO: What is the difference between local and global scope? Which is preferred?
# local is locked into the function. Global the function pulls from. I like global it is easier for me to keep track
# of the data. 
#%%
# TODO: Take a look at the code below. Before running it, think about what you would expect to happen. Explain step by step how the python code is executing.
def changeit(x):
    return x + 1

x = 42
print(x)
x = changeit(x)
print(x)
#%%
## Function Scope Example ##
def fill_nulls(df):
    return df.fillna(0)
#%%
def drop_outliers(df):
    outlier_cutoff = 3
    return df[df.zscore().abs() < outlier_cutoff]
#%%
def prep_dataframe(df):
    df = fill_nulls(df)
    df = drop_outliers(df)
    return
#%%
# Data Prep example: https://github.com/CodeupClassroom/darden-nlp-exercises/blob/main/nlp_prepare.py
# The specifics here aren't important right now, just pay attention to the overall shape of functions and how local scope is used.

############################### Lambda Functions ###############################
#
# - A function as an expression
# - used for "throw away", or one-off, functions

def increment(n):
    return n + 1
# same as
increment = lambda n: n + 1

# Use case: sorting (min, max)
#%%
# Python doesn't know how to compare dictionaries, but it does know how to compare strings or numbers

students = [
    {"name": "Ada Lovelace", "grade": 87},
    {"name": "Thomas Bayes", "grade": 89},
    {"name": "Christine Darden", "grade": 99},
    {"name": "Annie Easley", "grade": 94},
    {"name": "Marie Curie", "grade": 97},
]
sorted(students, key=lambda s: s['grade'])
# sort by name
sorted(students, key=lambda s: s["name"])

# TODO: write the code necessary to sort by grade
sorted(students, key=lambda s: s["grade"])
#%%
# TODO: Write the code necessary to sort the list of student dictionaries by student <em>last</em> name.
students = [
    {"name": "Ada Lovelace", "grade": 87},
    {"name": "Thomas Bayes", "grade": 89},
    {"name": "Christine Darden", "grade": 99},
    {"name": "Annie Easley", "grade": 94},
    {"name": "Marie Curie", "grade": 97},
]
def last_name(students):
    Return 
sorted(students, key=lambda s: s["name"].split()[0])




# Hint: You will need to write a function that takes in a student dictionary and returns just the last name.
# Hint: You can use the <code>.split</code> string method to seperate the first name and the last name.
#%%


# If we wanted to sort the students by last name, we would want to break up the name string into first and last name.
#  We would want to do this using the .split() string method, which will allow us to reference a list of two strings for each name, firstname and lastname.  [firstname, lastname] as a list can be 
# indexed by [0] for firstname and [1] for lastname just as we would index any other list.  
# So adding nuance to our initial name sort, we would want to look at the first index (as opposed to the 0th) of the split version of our value associated with the key 'name' for each value in our iterable list of dictionaries

# %%
