# For loops allow you to iterate over a sequence

# Iterate over a list

# Creating a list of animals
animals = ["cat", "dog", "turtle", "rabbit"]

# Iterating
for animal in animals:
    print(f"The animal is: {animal}")


# Multiply numbers from a list
numbers = [2, 4, 6, 8]

for number in numbers:
    result = number * 2
    print(f"{number} * 2 = {result}")


# Iterate over multiple lists at the same time
# Both lists must have the same number of elements
for number, animal in zip(numbers, animals):
    print(f"Number: {number}")
    print(f"Animal: {animal}")


# Using range()

# First way: one parameter
# Prints numbers from 0 to 4 (5 is not included)
for num in range(5):
    print(num)

# Second way: start and end
# Prints numbers from 5 to 9 (10 is not included)
for num in range(5, 10):
    print(num)


# Not recommended way to iterate a list
# This approach does not work with sets because they are unordered
print("Printing the list (not recommended)")
for i in range(len(numbers)):
    print(numbers[i])


# Better way using enumerate()
# enumerate() returns index and value
print("Better way to print a list")

for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")