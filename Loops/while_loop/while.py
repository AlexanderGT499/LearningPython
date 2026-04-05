# While loop

# Creating a counter for the while example
counter = 0

# The loop runs while the condition is true
while counter <= 5:
    print(f"Counter value: {counter}")
    counter += 1

print("Counter ends")

# Be careful: if the condition never becomes false,
# the loop will run forever (infinite loop)
# With while we can use break as well.