#armstrong
def arm(n):
    p = len(str(n))
    return n == sum(int(d)**p for d in str(n))

n = int(input("Enter a number: "))

if arm(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")