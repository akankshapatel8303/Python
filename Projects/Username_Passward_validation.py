username = input("Enter your username: ")
passward = input("Enter your passward: ")

def isValidPassward(passward):
    if(len(passward)<6 and len(passward)>12):
        lowerCase = False
        upperCase = False
        number = False
        special = False

        for char in passward:
            if(char.isdigit()):
                number = True
            if(char.isupper()):
                upperCase = True
            if(char.islower()):
                lowerCase = True
            if(not char.isalnum()):
                special = True
        return lowerCase and upperCase and number and special
    else:
        return False
    
print(isValidPassward(passward))