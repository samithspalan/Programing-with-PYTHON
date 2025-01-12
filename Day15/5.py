import os
for foldername,subfolders,filenames in os.walk('c:\\delicious)'):
  print('the current folder is'+foldername)
  for subfolder in subfolders:
    print('subfolder of'+foldername+':'+subfolder)
  for filename in filenames :
    print("file inside "+foldername+':'+filename)