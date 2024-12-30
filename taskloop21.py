start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum_odd = 0
for num in range(start, end + 1):
    if num % 2 != 0: 
        sum_odd += num
print("The sum of all odd numbers in the range is:", sum_odd)