print(f"************************")
print(f"Sum")
def Sum(n):
    
    if n == 0: 
        return 1
    return n + Sum (n-1)

res = Sum (4)
print(res)


print(f"************************")
print(f"Factorial Recursion")
def factorial(n):
    
    if n == 0: 
        return 1
    return n * factorial(n-1)

res = factorial(4)
print(res)