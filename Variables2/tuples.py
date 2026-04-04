# Creating tuples using the tuple() function

tuple1 = tuple(["data1", "data2"])
print("Tuple created with tuple():", tuple1)

# Creating tuples without parentheses

tuple2 = "data1", "data2"
print("Tuple without parentheses:", tuple2)

# Creating tuples with parentheses

tuple3 = ("data1", "data2")
print("Tuple with parentheses:", tuple3)

# Accessing elements

print("First element:", tuple3[0])

# Tuple unpacking

data = ("Ethan", "Winters", 57)

name, lastname, age = data

print("Name:", name)
print("Last name:", lastname)
print("Age:", age)

# Tuples are immutable (this will cause an error)
# tuple3[0] = "new data"  # Uncommenting this line will raise a TypeError