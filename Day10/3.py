import pprint
message='It is a good book'
count={}
for character in message:
  count.setdefault(character,0)
  count[character]=count[character ]+1
pprint.pprint(count)