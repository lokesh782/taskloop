a = [1, 2, 3, 4]
new = []
for i in range(len(a)):
    if i == 2:  
        new.append("a")  
    else:
        new.append(a[i])  
print(new)