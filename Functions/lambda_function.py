# Lambda fuction is a anonymous function
# It is useful for short operations

# Creating a lambda function
multiply_by_two = lambda x: x * 2

# Using the lambda function
print(multiply_by_two(7))


# Function that checks if a number is even
def is_even_number(num):
    return num % 2 == 0


# Using filter with a normal function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = filter(is_even_number, numbers)
print(list(even_numbers))


# Creating the same using a lambda function
even_numbers_lambda = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers_lambda))