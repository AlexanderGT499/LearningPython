# To write to a file, we use the mode 'w'
with open('Files\\test_text.txt', 'w', encoding='UTF-8') as file:
    
    # file.write('Editing file')  # This will overwrite the file
    
    # Writing multiple lines using a list
    file.writelines(["What's up\n", "Juan\n"])
    
    # Adding more lines
    file.writelines(["Bye\n", "Juan"])

'''
This example shows how to work with text files in Python.

We use the open() function with different modes:
- 'r' to read
- 'w' to write (overwrites the file)
- 'a' to append

The 'with' statement is recommended because it automatically closes the file.
'''
