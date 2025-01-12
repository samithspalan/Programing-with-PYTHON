while True:
  print('select a password(letter and num)')
  password=input()
  if password.isalnum():
    break
  print('password can only have letters and numbers')