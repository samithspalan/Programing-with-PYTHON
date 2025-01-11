#Sum of the Series 1/1!+1/2!+1/3!+…1/N!
import math 
n = int(input("Enter N: "))
s = sum(1 / math.factorial(i) for i in range(1, n + 1))

print(f"Sum of the series: {s}")