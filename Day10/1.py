txt='bu soft what lkight in  yonder window breaks '
words=txt.split()
t=list()
for word in words:
  t.append((len(word),word))#double bracket indicates tuple
  print(t)
t.sort(reverse=True)

res=list()
for lenght,word in t:
  res.append(word)

print(res)