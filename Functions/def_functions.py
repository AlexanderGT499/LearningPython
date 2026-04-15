# How to create our own functions

# Creating a function without parameters
# This function greets the user
def greet():
    print("Hello my friend Alejandro, how are you?")

# Using the function
greet()


# Function with parameters
def greet_with_data(name, age):
    
    if age < 18:
        message = "You are too young"
    else:
        message = "You are an adult"
        
    print(f"Hello my friend {name}. {message}")

greet_with_data("Alexander", 17)


# Function with a return value
def reverse_number(num):
    num = str(num)
    reversed_num = ""
    
    for digit in num:
        reversed_num = digit + reversed_num  # builds the number in reverse
        
    return reversed_num


# Asking the user for input
number = int(input("Enter a number to reverse: "))

reversed_number = reverse_number(number)

print(f"The reversed number of {number} is: {reversed_number}")

# Function that returns sum and product
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

# Unpacking results
sum_value, product_value = calculate(5, 3)

print(f"Sum: {sum_value}")
print(f"Product: {product_value}")