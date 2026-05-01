# Now we can use the fuctions created in Modules1

# First need to import the moduel

import math_operations 

# Second we call function from the module
addition = math_operations.add(5,8)
multiply = math_operations.multiply(10,5)

print(f'addition {addition} and multiply {multiply}')

# We can import with an alias

import math_operations as op

print(f'Addition = {op.add(3,5)}')