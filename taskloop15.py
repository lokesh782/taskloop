
input_string = input("Enter a string: ")
digits = 0
letters = 0
spaces = 0
for char in input_string:
    if char.isdigit():  
        digits += 1
    elif char.isalpha():  
        letters += 1
    elif char == " ":
        spaces += 1
print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")
print(f"Number of spaces: {spaces}")