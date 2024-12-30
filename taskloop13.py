 
a=[1,2,3,"d",4,5,"a"]
typed = {}
for i in a:
    item_type = type(i)
    if item_type not in typed:
        typed[item_type] = []
    typed[item_type] += [i]
for item_type, items in typed.items():
    print(f"{item_type}: {items}")