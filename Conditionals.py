# Conditionals are blocks of code that execute different actions depending on whether a condition is true or false.

# Example 1: equal comparison (If)

age = 10

if age == 10:
    #This code will be run
    print("Equals")

# Example 2: not equal comparison with else (if, else)

age=12

if age != 12:
    #This code will not be run
    print("Not equals")
else:
    #This code will be run
    print("Equals")
    
# Example 3: Using If, elif and else
# Only one block of code will run depending on the value of cash

cash = 1000

if cash == 100:
    print("You are poor")
elif cash == 1000:
    print("Not rich, but doing well")
else:
    print("You are rich")

# Example 4: Using a nested if statement

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")