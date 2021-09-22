from addition import *
from subtraction import *
from multiplication import *
from division import *

print("Welcome to the simple calculator. Please make a selection from the following options.")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")


user_selection = int(input("Make your selection: "))
if user_selection == 1:
    print("you chose addition")
    x = int(input("Enter a number "))
    y = int(input("Enter another number "))
    print(x, "+", y, "=", addition(x,y))
    
elif user_selection == 2:
    print("you chose subtraction")
    x = int(input("Enter a number "))
    y = int(input("Enter another number "))
    print(x, "-", y, "=", subtract(x,y))
elif user_selection == 3:
    print("you chose multiplication")
    x = int(input("Enter a number "))
    y = int(input("Enter another number "))
    print(x, "*", y, "=", multiply(x,y))
elif user_selection == 4:
    print("you chose division")
    x = int(input("Enter a number "))
    y = int(input("Enter another number "))
    print(x, "/", y, "=", divide(x,y))
else:
    print("Sorry that option does not exist. Please choose a valid option.")

