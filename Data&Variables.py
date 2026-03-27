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


#Variables

# Example with numbers
a = 2        # 'a' is an integer
b = 10       # 'b' is an integer
c = a + b    # 'c' is the sum of a and b

# Example with strings
nombre = "Alexander"   # Declare and assign a string variable
nombre = "Alejandro"   # Redefine the variable
print(nombre)          # Print the value of 'nombre'

# Working with numbers
numero = 10
numero += 5           # Increment 'numero' by 5 (accumulator)
print(numero)

# Concatenation with +
name = "Mario"
bienvenida = "Hola " + name + " ¿Cómo estás?"
print(bienvenida)

# Concatenation with f-strings
num = 5
# This won't work as expected:
bienvenida2 = "Hola {num} ¿Cómo estás?"  # The number will not be printed
print(bienvenida2)

# Correct way using f-strings
bienvenida2 = f"Hola {num} ¿Cómo estás?"  # Add 'f' before the string to insert variables
print(bienvenida2)

# del word is used to delet data in memory

# in/not in return a boolean
print("Hola " in bienvenida2) #It will return true
print("pedro" in bienvenida2) # It will return False
print("pedro" not in bienvenida2) # True because it is not pedro in bienvenida2

# Define a variable with camelCase
fullName = "Alexander Guerrero"
# define a variable with snake_case
full_name = "Alexander Guerrero"



# Complex data

"""
In Python, we can create a list that contains different types of data,
such as strings, integers, floats, and booleans."""

lista = ["Alexander Guerrero", "Soy Alex",True, 1.73]
# Accessing the first element of the list
"""
In a list, we access elements by their position (index).
In Python, indexing starts at 0, so the first element is at position 0."""
print(lista[0]) # It will print the name element 1
print(lista[2]) # It will print the boolean element 3

# Modify list

lista[1] = "Alex"
print(lista[1])

# Tuple: similar to list but its elements cannot be modified (it is immutable)


tuple = ("Alexander Guerrero", "Soy Alex",True, 1.73)

print(tuple[3])

#It is wrong tuple[3] = 1.16 X

# Set: similar to a list, but its elements cannot be modified (mutable structure, but no indexing),
# elements are unordered, and duplicate values are not allowed.

conjunto = {"Alexander Guerrero", "Soy Alex", True, 1.73}
conjunto.add("new value") # Allowed
# print(conjunto[3]) # Not allowed

# Dictionary: similar to a Java HashMap
# A dictionary stores data as key-value pairs.
# You use the key to access its value.

dictionary = {
    'name': "Alexander Guerrero",
    'happy': True,
    'height': 1.73
}

# Example: access a value using its key
print("Alexander is happy? ", dictionary['happy'])  # Output: True