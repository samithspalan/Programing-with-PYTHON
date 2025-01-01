# m1=int(input(""))
# m2=int(input(""))
# m3=int(input(""))
# mylist=[m1,m2,m3]
# print(mylist)
# mylist.sort()
# print(mylist)
try:
    m1 = int(input("Enter the first number: "))
    m2 = int(input("Enter the second number: "))
    m3 = int(input("Enter the third number: "))
    mylist = [m1, m2, m3]
    mylist.sort()
    print("Sorted list:", mylist)
except ValueError:
    print("Invalid input. Please enter integers only.")

