# List methods allow you to modify a list.

# Example 1: Create a list
list1 = ["Hello", "Alexander", 20]
print(list1)


# Example 2: Function len()
# Returns the number of elements in the list

result = len(list1)
print(result)


# Example 3: Method append()
# Adds a new element to the end of the list

list1.append("Bye")
print(list1)


# Example 4: Method insert()
# Similar to append(), but allows selecting the position of the new element

list1.insert(2, "age")
print(list1)


# Example 5: Method extend()
# Adds more than one element to the list

list1.extend([True, 2026])
print(list1)


# Example 6: Method pop()
# Removes the element at the given index
# If the index is -1, it removes the last element

list1.pop(1)
print(list1)

list1.pop(-1)
print(list1)


# Example 7: Method remove()
# Removes an element by its value

list1.remove("age")
print(list1)


# Example 8: Method clear()
# Removes all elements from the list

# list1.clear()
# print(list1)


# Example 9: Method sort()
# Sorts the list in ascending order
# Works only with numbers and booleans
# True == 1 and False == 0

list2 = [1, 10, 5, 8, 12, 75, 23, True, False, 20, True]
list2.sort()
print(list2)


# Sort in descending order using reverse=True

list2.sort(reverse=True)
print(list2)


# Example 10: Method reverse()
# Reverses the list order without sorting

list3 = [1, 3, 7, 9, "Pedro", "Juan", True, 3, False]
list3.reverse()
print(list3)


# Example 11: Method index()
# Returns the position of the element
# If the element is not found, it raises an error

list4 = ["Hola", 50, 3, True, 1]
found_element = list4.index(3)
print(found_element)