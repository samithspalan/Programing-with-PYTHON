num=int(input('enter a no'))
prime=False 
for i in range(2,num):
    if num%i==0:
        prime=True
        break
if prime:
    print ("this number is prime")
    
else:
    print("not a prime no")