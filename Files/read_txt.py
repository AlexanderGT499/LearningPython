# First, to open a file we use the reserved word 'open'
# and then write the path of the file.

file_without_read = open('Files\\test_text.txt')

# Then we read the file using the method read()
# This shows the content of the file, but special characters
# may not display correctly.

'''
file_read = file_without_read.read()
print(file_read)
'''

# To fix encoding issues, we use UTF-8 (a standard format)
'''
file_without_read = open('Files\\test_text.txt', encoding='UTF-8')
file_read = file_without_read.read()
print(file_read)
'''

# If we want to read line by line
# Not recommended for large files
'''
lines = file_without_read.readlines()  # Returns a list
print(lines)
'''

# When we finish working with the file, we must close it
file_without_read.close()