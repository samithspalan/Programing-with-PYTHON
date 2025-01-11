mypet=['zophie','pooka','foot']
print("enter a name")
name=input()
if name not in mypet:
  print("I do not have a pet named "+name)
else:
  print(f"{name} is my pet name")