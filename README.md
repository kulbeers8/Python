# Python

Assignment : 1

Python Task submission 

Task1: Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.


Solution: 

  1) We have to take two variable which store user input value and convert it into integer. Because by default eveery input is in the form of string.
  2) We implement airthmatic operation on it.


 Task2: 

   Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.

Solution: 
  
  1) We take first name from user using input funtion and store in a variable.
  2) We take last name from user using input funtion and store in a variable.
  3) Concatenates first name and last name with addition operator and save it into another variable.
  4) print the message
     
 

Assignment : 2 


Task 1: Check if a Number is Even or Odd
   Problem Statement:  Write a Python program that:
   1. 	Takes an integer input from the user.
   2. 	Checks whether the number is even or odd using an if-else statement.
   3. 	Displays the result accordingly.
   
   Solution:
   
   1. We take input from users.
   2. If number is divide by 2 then number is even. If not then number is odd. 
   

Task 2: Sum of Integers from 1 to 50 Using a Loop
 
     Problem Statement: Write a Python program that:
     1.   Uses a for loop to iterate over numbers from 1 to 50.
     2.   Calculates the sum of all integers in this range.
     3.   Displays the final sum.
     
     Solution:
     
     1. In this task we have already defined range 1 to 50
     2. total_sum variable by default 0 . When it enter into the for loop then its value change until we reched our final range value.





Assignment 4 

Task 1: Read a File and Handle Errors 

    Problem Statement:  Write a Python program that:
    
    1.   Opens and reads a text file named sample.txt.
    2.   Prints its content line by line.
    3.   Handles errors gracefully if the file does not exist.

Solution: 

  1. We use os module for check file exist or not using if condition
  2. Open the file using with so that we not need to close file method It automatically close the file.
  

Task 2: Write and Append Data to a File
 
  Problem Statement: Write a Python program that:
   1.   Takes user input and writes it to a file named output.txt.
   2.   Appends additional data to the same file.
   3.   Reads and displays the final content of the file.

  Solution: 

   1. In this program first we take the input and write it into the file.
   2. After write the file we again take input from the user.
   3. Second input we append in this file.
   4. After append we display the content inside the file.
