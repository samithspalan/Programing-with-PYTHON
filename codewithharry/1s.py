mydict={
  "name":"Mike",
  "grade":8,
  "school":"DPS",
  "phno":[9,394,59,6,96,9]
}
print(mydict.keys())
print(mydict.values())
print(mydict.items())

updatedict={
  "name":"John",
  "grade":7,
  "school":"DPS"
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("harry"))
# print(mydict.["harry"]) throws error