import os 
basedir=os.getcwd()
filename=os.path.join(basedir, 'output.txt')
#Get first input like 25
userinput=input("Enter text to write to the file:")
  with open(filename, 'w') as f:
    content = "Hello python!"
    f.write(content + "\n")
    print(f"Data successfully written to output.txt")

#Get another input.
userinput1=input("Enter additional text to append:")
with open(filename, 'a') as f:
     content = userinput1
     f.write(content + "\n")
     print("Data successfully appended.")
#Read the content inside the file.     
with open(filename, 'r') as f:
    content = f.read()
    print(content, end='')
