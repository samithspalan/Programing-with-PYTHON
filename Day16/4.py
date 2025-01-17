class Point:
    pass
blank=Point()
blank.x=3.0
blank.y=4.0
decdata=id(blank)
print('ID of Blank in decimal=',decdata)
print('Printing the object blank=',blank)
data=blank
datalist=str(data).split()
print(datalist)
hexdata=datalist[3].rstrip('>')
dec = int(hexdata, 16);
print(hexdata,"in Decimal =",str(dec));
if dec==decdata:
    print('ID in Decimal and Hexa are Same')