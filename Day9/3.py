year=int(input())
if(year%400==0):
    print("Its a leap year")
elif(year%100==0):
  print("Its not a leap year")
elif(year%4==0):
  print("Its a leap year")
else:
  print("Its not a leap year")