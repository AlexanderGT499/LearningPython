# Basic way to sum a list

def sum_list(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

print(f"The total addition of the list is: {sum_list([1, 2, 3, 4, 5])}")


# Better way (more flexible)
# Using *args (variable number of arguments)

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_numbers(2, 4, 6, 8)
print(f"The total addition is: {result}")