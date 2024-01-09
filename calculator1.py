print("~~~~~~~~~~~~~~~CALCULATOR~~~~~~~~~~~~~~~~")

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")
choice =int(input("enter your choice from 1-4: "))
if (choice == 1):
    print("the Addition of given two number is",num1 + num2)
elif (choice == 2):
    print("the Substraction of given two number is",num1 - num2)
elif (choice == 3 ):
    print("the Multiplication of given two number is",num1 * num2)
elif (choice == 4):
    print("the Division of two number is",num1 / num2)
else:
    print("Invalid input")
   
