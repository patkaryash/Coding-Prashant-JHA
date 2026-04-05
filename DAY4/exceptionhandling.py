# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# try:
#     print("The division is: ", n1/n2)
# except:
#     print("can't divide by zero")


# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print("The division is: ", n1/n2)
# except ZeroDivisionError:  #This will handle the exception when we try to divide by zero
#     print("can't divide by zero")
# except ValueError:         #This will handle the exception when we enter a non-integer value
#     print("Please enter valid integers")


#Handling multiple exceptions in a single except block
# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print("The division is: ", n1/n2)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)


#The concept of default except block
# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print("The division is: ", n1/n2)
# except (ZeroDivisionError, ValueError) as message:
#     print("Enter correct numbers: ", message)
# except:
#     print("This is default part of except block") #This will execute if any other exception occurs which is not handled by the above except blocks
    
#We can use else block if no error will occur in the try block
# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print("The division is: ", n1/n2)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# else:
#     print("Division performed successfully")
        


#Finally block will execute in any case whether an exception occurs or not
# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print("The division is: ", n1/n2)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# finally:
#     print("This will execute in any case whether an exception occurs or not")


#nested try except block
# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     try:
#         print(n1/n2)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)

#        
# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print(n1/n2)
# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)
# else:
#     print("Division performed successfully")
# finally:
#     print("This will execute in any case whether an exception occurs or not")

        
 

