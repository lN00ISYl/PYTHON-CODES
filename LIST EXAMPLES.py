#LIST EXAMPLES
#NAME = ["BACON","TRISH", "KIRSTER"]
#NAME.append("RIN")
#NAME.remove("BACON")
#print(NAME)


#STRINGS
FIRST = "KARLOS"
SECOND = "SON"

print(FIRST[2])

#check if the number you put in is in the list
name = []
name1 =int(input("Enter first number"))
name2 =int(input("Enter second number"))
name3 =int(input("Enter third number"))
name4 =int(input("Enter fourth number"))
name5 =int(input("Enter fifth number"))

name.append(name1)
name.append(name2)
name.append(name3)
name.append(name4)
name.append(name5)
print(name)
cont = input("Enter s to continue:")
if cont == "s":
    num= int(input("enter a number"))
    if num in name:
        print("the number is in the list")    
else:
    print("nice")
    

#sort it form highest to lowest
name = []
name1 =int(input("Enter first number"))
name2 =int(input("Enter second number"))
name3 =int(input("Enter third number"))
name4 =int(input("Enter fourth number"))
name5 =int(input("Enter fifth number"))

name.append(name1)
name.append(name2)
name.append(name3)
name.append(name4)
name.append(name5)


name.sort(reverse=True)
print(name)



