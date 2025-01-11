#GCD 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Update a to b, and b to the remainder of a divided by b
    return a
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"GCD of {a} and {b} is: {gcd(a, b)}")