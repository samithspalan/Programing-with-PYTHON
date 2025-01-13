class Point:
  pass
blank=Point()
blank.x=3.0
x=blank.x
x=x+10
blankid=id(blank)
print(blankid)