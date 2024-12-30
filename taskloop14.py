
given_list = [1, 2, 3, 4, "a", "b"]
int_list = []
str_list = []

for item in given_list:
    
    if type(item) == int:
        int_list.append(item)
    elif type(item) == str:
        str_list.append(item)
print("Integers List:", int_list)
print("Strings List:", str_list)
