# This example shows how to unpack a tuple into variables.
# The tuple data contains three values. When we assign 
# it to name, lastname, and age, each variable receives one value from the tuple in order.
# The number of variables must match the number of values in the tuple.

# Creating data
data = ("Ethan", "Winters", 57)
data_list = ["Ronal", "Parker", 34]

# Unpacking
name, lastname, age = data
name2, lastname2, age2 = data_list

# Show results
print(name)
print(name2)