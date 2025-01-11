#quadratic equation
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots are distinct and real: {r1} and {r2}")
elif d == 0:
    r = -b / (2*a)
    print(f"Roots are real and the same: {r}")
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-d) / (2*a)
    print(f"Roots are complex: {real_part} + {imag_part}i and {real_part} - {imag_part}i")