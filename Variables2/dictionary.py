# Creating dictionary

dictionary = dict(name="Mesias",lastname = "Simbania")

print(dictionary)

# A tuple can be a key because they are unmutable

dictionary = {("hello","friend"): "Bye"}

print(dictionary)

# Creating dictionary with the fuction fronkeys() 
dictionary = dict.fromkeys(["name","lastname","age"])

print(dictionary)

# As well this fuction if we send a string 
# we can create a dictionary with every character 
# from that string

dictionary = dict.fromkeys("name")
print(dictionary)