
def is_armstrong(num):
    
    original_num = num
    

    num_digits = len(str(num))
    

    sum_of_powers = 0
    

    while num > 0:
        digit = num % 10 
        sum_of_powers += digit ** num_digits  
        num //= 10 
    
    if sum_of_powers == original_num:
        return True
    else:
        return False


number = int(input("Enter a number: "))

