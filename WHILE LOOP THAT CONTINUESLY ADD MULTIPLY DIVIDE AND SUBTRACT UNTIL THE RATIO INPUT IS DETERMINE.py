import random

user = int(input("how many sequence do you want to do?: "))
def operations():
    print("MULTIPLICATION (*)")
    print("DIVISION (/)")
    print("SUBTRACTION (-)")
    print("ADDTION (+)")
    
operations()
list = ["*","/","-","+"]
operation = input("chooise what operation to use: ").lower()

if operation in list:
    if operation == "/":
        div = int(input("enter a ratio: "))
        while type(div) != int:
            print("Invalid input")
            div = int(input("enter a ratio: "))
    elif operation == "-":
        sub = int(input("enter a ratio: "))
        while type(sub) != int:
            print("Invalid input")
            sub = int(input("enter a ratio: "))
    elif operation == "*":
        multi = int(input("enter a ratio: "))
        while type(multi) != int:
            print("Invalid input")
            multi = int(input("enter a ratio: "))
    elif operation == "+":
        add = int(input("enter a ratio: "))
        while type(add) != int:
            print("Invalid input")
            add = int(input("enter a ratio: "))
elif operation not in list:
    print("Please enter a valid input")
    operation = input("chooise what operation to use: ").lower()
    
def calculating():
    
    list= []
    starter = int(input("Enter a number you want to start: "))
    num = (starter)
    
    if operation == "/":
        while len(list)<user:
            list.append(num)
            num /= div
    if operation == "+":
        while len(list)<user:
            list.append(num)
            num += add
    if operation == "-":
        while len(list)<user:
            list.append(num)
            num -= sub
    if operation == "*":
        while len(list)<user:
            list.append(num)
            num *= multi
    return list

print(calculating())
    
    



