# Data types in Python

# Strings: text is written with single, double, or triple quotes
"string"
'string'
"""String
for multiple
lines"""
'''Another way
for multiple
lines'''


# Simple data types

# 40        -> Integer (int)
# 40.2      -> Float
# True/False -> Boolean


# Variables

# Example with numbers
a = 2        # 'a' is an integer
b = 10       # 'b' is an integer
c = a + b    # 'c' is the sum of a and b

# Example with strings
name = "Alexander"   # Declare and assign a string variable
name = "Alex"        # Redefine the variable
print(name)          # Print the value of 'name'

# Working with numbers
number = 10
number += 5           # Increment 'number' by 5
print(number)

# Concatenation with +
name = "Mario"
greeting = "Hello " + name + ", how are you?"
print(greeting)

# Concatenation with f-strings
num = 5

# This won't work as expected:
greeting2 = "Hello {num}, how are you?"  # The number will not be printed
print(greeting2)

# Correct way using f-strings
greeting2 = f"Hello {num}, how are you?"  # Add 'f' before the string
print(greeting2)

# The 'del' keyword is used to delete data from memory

# in / not in return a boolean
print("Hello" in greeting2)   # Returns True
print("Pedro" in greeting2)   # Returns False
print("Pedro" not in greeting2)  # Returns True

# Define a variable with camelCase
fullName = "Alexander Guerrero"

# Define a variable with snake_case
full_name = "Alexander Guerrero"


# Complex data

"""
In Python, we can create a list that contains different types of data,
such as strings, integers, floats, and booleans.
"""

data_list = ["Alexander Guerrero", "I am Alex", True, 1.73]

# Accessing elements
"""
In a list, we access elements by their position (index).
In Python, indexing starts at 0.
"""
print(data_list[0])  # First element
print(data_list[2])  # Third element

# Modify list
data_list[1] = "Alex"
print(data_list[1])


# Tuple: similar to a list but immutable (cannot be modified)
data_tuple = ("Alexander Guerrero", "I am Alex", True, 1.73)

print(data_tuple[3])

# This is incorrect:
# data_tuple[3] = 1.16  X


# Set: unordered collection, no duplicates, no indexing
data_set = {"Alexander Guerrero", "I am Alex", True, 1.73}

data_set.add("new value")  # Allowed
# print(data_set[3])  #  Not allowed


# Dictionary: key-value pairs (similar to Java HashMap)
data_dict = {
    'name': "Alexander Guerrero",
    'is_happy': True,
    'height': 1.73
}

# Access value using key
print("Is Alexander happy?", data_dict['is_happy'])