myDict={
    "fast":"speed",
    "won":"out"
}
updatedict={
    "fast":"slow"
}
myDict.update(updatedict)
print(myDict)

print(myDict.get("sam"))#prints none
print(myDict.get["sam"])#throws error
