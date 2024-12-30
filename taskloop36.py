
bad_chars = [';', ':', '!', "*"]

string = "py;th* o:n ! ;py * t*h:o !n"

cleaned_string = ""

for char in string:
    if char not in bad_chars:  
        cleaned_string += char 

print(cleaned_string)
