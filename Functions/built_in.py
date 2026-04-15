# Built-in functions

numbers = [2, 6, 9, 34, 76]

# max(): returns the largest number in the list
# The list must contain only numbers
print(max(numbers))

# min(): returns the smallest number in the list
print(min(numbers))


# Rounding numbers

# round(): returns an integer
number = round(123.5465)
print(number)

# round(): returns a float when specifying decimal places
number = round(435.32344, 2)
print(number)


# bool(): converts a value to True or False
# Returns False for 0, None, or empty values
# Returns True for most other values

boolean_result = bool(0)
print(boolean_result)

boolean_result = bool("Pig")
print(boolean_result)


# all(): returns True if all elements are True
# Works with lists, tuples, and sets

# Returns True
result_all = all((4, True, 20, "hello"))
print(result_all)

# Returns False because some elements are False
result_all = all([False, 0, 50, True])
print(result_all)

# any(): returns True if at least one element is True
print(any([0, False, 5]))  # True