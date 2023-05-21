# Factorial of non-negative integer n, denoted by n! 
# is the product of all positive integers less than 
# or equal to n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter the number:"))
result = factorial(n)
print("factorial of",n,"is",result)