# For loop examples

# Using for/else
numbers = [2, 4, 6, 8, 10, 12, 14]

for num in numbers:
    print(f"Loop iteration: {num}")
else:
    print("Loop finished")  # Runs only if the loop is not interrupted

# Using continue
# The `continue` keyword allows you to skip to the next iteration
fruits = ["apple", "pear", "cherry", "orange", "pineapple"]

print("\nUsing continue")
for fruit in fruits:
    if fruit == "cherry":
        print(f"Skipping the iteration for {fruit}")
        continue
    print(f"I eat: {fruit}")


# Using break
# The `break` keyword stops the loop immediately
print("\nUsing break")

for fruit in fruits:
    print(f"I eat: {fruit}")
    if fruit == "orange":
        break
else:
    print("Loop ends")  # If break is used, this block does not run


# Iterating over a string
text = "Good night"

for letter in text:
    print(letter)


# Duplicate values from a list

# First way (more verbose)
numbers = [2, 4, 6, 8]
numbers_duplicate = []

for num in numbers:
    numbers_duplicate.append(num * 2)

print(numbers_duplicate)


# Second way (more concise)
numbers_duplicate = [num * 2 for num in numbers]
print(numbers_duplicate)