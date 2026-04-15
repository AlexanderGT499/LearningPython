# Function with parameters

def create_sentence(name, last_name, adjective):
    return f"Hello {name} {last_name}, you are {adjective}"


# Calling the function (positional arguments)
result_sentence = create_sentence("Pedro", "Benalcazar", "cool")
print(result_sentence)


# Using keyword arguments (order does not matter)
result_sentence = create_sentence(
    adjective="great",
    name="Jeremy",
    last_name="Reinoso"
)

print(result_sentence)

# Using a default value when no argument is provided
def create_sentence(name, last_name, adjective="nice"):
    return f"Hello {name} {last_name}, you are {adjective}"