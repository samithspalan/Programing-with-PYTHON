birthdays={
    'Alice':'apr 1',
    'Bob':'dec 12',
    'Carol':'mar24'
}
while True:
  print("enter a name :(done to quit)")
  name=input()
  if name=='done':
    break
  if name in birthdays:
    print(birthdays[name]+' is the birhtday of '+name)
  else:
    print('i do not have birthday information for'+name)
    print('What is their birthday?')
    bday=input()
    birthdays[name]=bday
    print('Birthday database updated')