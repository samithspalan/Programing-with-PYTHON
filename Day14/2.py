def picnic(item,leftWidth,rightWidth):
  print('PICNIC ITEMS'.center(leftWidth +rightWidth,'-'))
  for k,v in item.items():
    print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))
picnicItems={'sandwiches':4,'apples':12,'cups':14}
picnic(picnicItems,12,5)
picnic(picnicItems,20,5)