
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10  
        reversed_num = reversed_num * 10 + digit 
        num //= 10  
    
    if original_num == reversed_num:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
