import sys

# Program make a simple calculator
# This function adds two numbers 
def add(x, y):
    return x + y
# This function subtracts two numbers 
def subtract(x, y):
    return x - y
# This function multiplies two numbers
def multiply(x, y):
    return x * y
# This function divides two numbers
def divide(x, y):
    return x / y



if len(sys.argv) == 4:    

    num1 = sys.argv[1]
    num2 = sys.argv[2]
    choice = sys.argv[3]
    
    if choice == '1':
       add(num1,num2)
    elif choice == '2':
       subtract(num1,num2)
    elif choice == '3':
       multiply(num1,num2)
    elif choice == '4':
       divide(num1,num2)
    else:
       return ("Invalid input")
else:
    return "Invalid Passing Arguments."
