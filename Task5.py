#Program to get factorial
number = int(input("Enter a number: "))

def factorial(number): 
  current_numer=1
  while number > 0:
      current_numer = current_numer*number
      number -= 1 
  return current_numer 

#Create object of the function    
obj=factorial(number)
print(f"Factorial of {number} is: {obj}")
