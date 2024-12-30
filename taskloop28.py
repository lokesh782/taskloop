#Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] 
# Given list
a = ["ram", "shyam", 1, 2]
for name in a:
    if isinstance(name, str):  
        print(f"Hello!{name}")