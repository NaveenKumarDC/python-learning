# Writing to a text file using 'with' ensures the file is properly closed
# with open('example.txt', 'w') as file:
#     file.write("Hello, this is a test file.\nAnother line.")

#Reading from a file:
# Reading the content back from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:\n", content)
