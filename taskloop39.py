
sum_multiples = 0


for num in range(3, 100):

    if num % 3 == 0 or num % 5 == 0:
        sum_multiples += num  

print("Sum of multiples of 3 or 5 below 100:", sum_multiples)
