num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
num3 = int(input("Number3: "))

if(num1>num2 and num1>num3):
    print(f"{num1} is largest")

elif(num2>num1 and num2>num2):
    print(f"{num2} is largest")

else:
    print(f"{num3} is largest")