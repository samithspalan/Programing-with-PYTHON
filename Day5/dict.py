meanings = { #dictionary
     "bat":"used to hit",
      "ball": "to be hit"
 }
print(meanings)
print(type(meanings))
print(meanings["bat"])
print(meanings.get("ball","not found"))#safe access not to crash
print(meanings.get("sudeep","not found"))#safe access not to crash

meanings["samith"] = 'my name'#to add dictionery #can be also used for updating
print(meanings)
meanings.pop("samith")
print(meanings)
print(meanings.keys())
print(meanings.values())

