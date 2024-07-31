num = int(input("Enter the value of number: "))

def fact(num):
    if num == 0:
        return 1
    
    if num == 1:
        return 1
    
    return num * fact(num-1)

result = fact(num)
print(result)