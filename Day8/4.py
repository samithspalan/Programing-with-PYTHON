import copy
spam2=[1,[2,1],3]
cheese2=copy.copy(spam2)#is a shallow copy
cheese2[1][0]=5
print(spam2)

spam3=[1,[2,1],3]
cheese3=copy.deepcopy(spam2)
cheese3[1][0]=5
print(spam3)