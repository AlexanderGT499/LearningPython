# Using the 'with' statement
with open('Files\\test_text.txt', encoding='UTF-8') as file:
    
    # Reading the file
    content = file.read()
    
    # Show file content
    print(content)

# It is not necessary to close the file (it is done automatically)