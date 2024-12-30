
string = "Hello World! This is a test string."

space_count = 0
for char in string:
    if char == ' ':  
        space_count += 1  
print(f"The number of spaces in the string is: {space_count}")
