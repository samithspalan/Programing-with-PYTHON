catnames=[]
while True:
  print('Enter the names of the cat'+str(len(catnames)+1)+'(or enter nothing to stop)')
  name=input()
  if name=='':
    break
  # catnames=catnames + [name]
  catnames.append(name)

print('The cat names are:')
for name in catnames:
  print(name)