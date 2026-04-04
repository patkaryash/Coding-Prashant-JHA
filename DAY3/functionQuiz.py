#WAP for menu driven code
import sys 
def add():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    print("Addition: ", val1 + val2)

def subtract():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    print("Subtraction: ", val1 - val2)

def multiply():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    print("Multiplication: ", val1 * val2)

def divide():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    if val2 != 0:
        print("Division: ", val1 / val2)
    else:
        print("Cannot divide by zero!")

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice! Please try again.")
        
        
    
   