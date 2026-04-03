# String methods allow you to modify and work with text data.
# To see all available string methods, we can use dir().

# test = "test"
# print(dir(test))


# Example 1: Convert the string to uppercase

string1 = "Hi I'm Alex"
result = string1.upper()
print(result)


# Example 2: Convert the string to lowercase

string2 = "Welcome"
result = string2.lower()
print(result)


# Example 3: Capitalize the first letter

string3 = "hello"
result = string3.capitalize()
print(result)


# Example 4: Find a letter.
# If it exists in the string, it returns the position.
# If not found, it returns -1.

result = string3.find("o")
print(result)  # Returns 4


# Example 5: Using index().

# It is similar to find(), but if the value is not found,
# it raises an exception.

# result = string3.index("v")
# print(result)


# Example 6: Count how many times a letter appears in a string

result = "morning"
count_letters = result.count("o")
print(count_letters)


# Example 7: Count how long the string is
# len() is not a method — it is a function

result_len = len(result)
print(result_len)


# Example 8: Replace part of a string with another string

old_string = "Hello boy"
print(old_string)  # Before using replace()

new_string = old_string.replace("boy", "guys")
print(new_string)  # After using replace()


# Example 9: Split a string (this returns a list)

separate_string = new_string.split(" ")
print(separate_string)
