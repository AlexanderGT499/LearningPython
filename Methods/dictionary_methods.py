# Dictionary methods allow you to modify a dictionary.

dictionary = {

    "name": "alex",
    "last_name": "silva",
    "age": 34
}


# Example 1: Method keys()
# Returns all keys from the dictionary and can be used for iteration

keys = dictionary.keys()
print(keys)


# Example 2: Method get()
# Returns the value accessed by the key
# If the key does not exist, it returns None

value = dictionary.get("name")
print(value)


# Example 3: Method clear()
# Deletes all elements from the dictionary

# dictionary.clear()
# print(dictionary)


# Example 4: Method pop()
# Deletes one element from the dictionary using its key

dictionary.pop("last_name")
print(dictionary)


# Example 5: Method items()
# Returns dictionary elements as iterable key-value pairs

dictionary_iterable = dictionary.items()
print(dictionary_iterable)


# Example 6: Method update()
# Adds a new key-value pair or modifies an existing one

student = {
    "name": "Pedro",
    "age": 52
}

# Updating an existing value
student.update({"age": 21})
print("After updating\n", student)

# Adding a new key-value pair
student.update({"nationality": "Ecuadorian"})
print("Adding new key-value pair\n", student)

# Example 7: Method values()
# Returns all values from the dictionary

values = dictionary.values()
print(values)

# Example 8: Check if a key exists in the dictionary

if "name" in dictionary:
    print("Key exists")
    
# Example 9: Method popitem()
# Removes the last inserted key-value pair

student.popitem()
print(student)