# Iterating over dictionaries

dictionary = {
    "name": "Alex",
    "last_name": "Guerrero"
}

# The items() method returns key-value pairs as tuples
for item in dictionary.items():
    print(item)

# Better way to access keys and values using the items() method
for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")

# Iterating only keys
for key in dictionary.keys():
    print(key)

# Iterating only values
for value in dictionary.values():
    print(value)