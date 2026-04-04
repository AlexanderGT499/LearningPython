# Creating sets

set1 = set(["Data1", "Data2"])
print(set1)


# Creating sets inside other sets
# The frozenset() function creates an immutable set,
# which can be included inside another set

set2 = frozenset(["data1", "data2"])
set3 = {set2, "data3"}

print(set3)


# Set theory operations
set1 = {1, 3, 5, 7}
set2 = {1, 3, 7}

# Verify if it is a subset
result = set2.issubset(set1)
print(result)

# Other way to verify
result = set2 <= set1
print(result)


# Verify if it is a superset
result = set1.issuperset(set2)
print(result)

# Other way to verify
result = set1 >= set2
print(result)


# Verify if the sets have no elements in common
# Returns True if they are completely different

result = set2.isdisjoint(set1)
print(result)