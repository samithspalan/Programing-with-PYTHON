def spam(n):
  try:
     return 42//n
  except ZeroDivisionError:
      print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))#not skipped