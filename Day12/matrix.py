rows=int(input("Enter the number of rows: "))
colums=int(input("Enter the number of columns: "))
matrix=[]
for i in range(rows):
  row=[]
  for j in range(colums):
    x=int(input("Enter the element: "))
    row.append(x)
  matrix.append(row)
    
print(matrix) 