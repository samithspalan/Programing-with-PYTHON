import traceback
try:
  raise Exception("this is the error message")
except:
   errorFile=open('errorInfo.txt','w')
   errorFile.write(traceback.format_exc())
   errorFile.close()
   print("the trceback info was written to errorInfo.txt")