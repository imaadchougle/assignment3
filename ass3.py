#task1
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  
    return result  
num = int(input("Enter a number: "))

fact = factorial(num)
print(f"Factorial of {num} is: {fact}")

#task2
import math  
num = float(input("Enter a number: "))

square_root = math.sqrt(num)      
log_value = math.log(num)           
sine_value = math.sin(num)    

print(f"Square root: {square_root}")
print(f"Logarithm: {log_value}")
print(f"Sine: {sine_value}")
