name=input("enter a name")
print("good afternoon-",name)

template='''
          Dear,<name>
          You are selected'''
          
print(template.replace('<name>',name))
