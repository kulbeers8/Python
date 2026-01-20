#This program is used for file handling
import os
basedir=os.getcwd()
filename=os.path.join(basedir,"sample.txt")
if os.path.exists(filename):
   with open(filename,'r') as f:
     for content in f:
       print(content)
else:
   print(f"The file '{filename}' was not found.") 
      
