num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Press 1 for Addition\n Press 2 for Substraction\n Press 3 for Multiplication\n Press 4 for Division")
choice = int(input("Enter your choice from 1-4: "))

if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num1)
else:
    print("Invalid input")