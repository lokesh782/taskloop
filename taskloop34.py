
first_list = [1, "hello", 3.14, True, [1, 2, 3]]

second_list = []

for element in first_list:
    second_list.append(type(element))  
else:
    print("Done")

print("Types of elements:", second_list)