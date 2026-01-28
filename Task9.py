#Create a dictionary 
user_dict={
  "Alice": 85,
  "Kulbeer": 80,
  "Naveen": 90
}

user_name = input("Enter the student's name: ")

if user_name in user_dict:
 print(f"{user_name}'s marks: {user_dict[user_name]} ")
else:
 print("Student not found.")
