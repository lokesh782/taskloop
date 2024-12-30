
start = 1
end = 10

even_sum = 0

for num in range(start, end + 1):
    if num % 2 == 0:  
        even_sum += num  
print(f"The sum of all even numbers from {start} to {end} is {even_sum}")
