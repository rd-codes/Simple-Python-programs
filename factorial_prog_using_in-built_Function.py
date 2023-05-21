# Factorial of non-negative integer n, denoted by n! 
# is the product of all positive integers less than 
# or equal to n.

import math 

n = int (input("Enter the number:"))
result = math.factorial(n)
print("factorial of", n, "is", result)