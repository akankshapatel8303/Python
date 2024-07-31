x = int(input("First variable: "))
y = int(input("Second variable: "))

def swap(x, y):
    temp = x
    x = y
    y = temp
    print(f"x = {x} and y = {y}")

swap(x,y)