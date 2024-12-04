s={20,2,123}#set is unordered
print(type(s))
s2={34,56,123,6}
#tot=s + s2 #cannot be added
print(s  | s2)#union
print(s&s2)#intersection
s.add(4)
s.delete(4)
s.discard(4)#wont show error even if the element is not there in th list
s.pop()#it itself removes the element randomly

