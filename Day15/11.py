def boxprint(symbol,width,height):
  if len(symbol)!=1:
    raise Exception("symbol must be a single character")
  if width<=2:
    raise Exception("width must be greater than 2")
  if height<=2:
    raise Exception("height must be greater then 2")
  print(symbol*width)
  for i in range(height-2):
    print(symbol+(''*(width-2))+symbol)
  print(symbol*width)

for sym, w,h in ('a',4,4):
  try:
    boxprint(sym,w,h)
  except Exception as err:
    print("AN exception happpened"+str(err))