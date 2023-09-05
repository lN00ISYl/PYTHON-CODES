#for examples

for BACON in range (1,10 ):
    print(BACON)
  
  
  #while examples
  #EXAMPLE 1
#Name = input("ENTER YOUR NAME:")

#while Name == "":
 #   print("YOU DIDNT TYOE ANYTHING")
 #   Name = input("ENTER YOUR NAME:")  

#print(f"Hello {Name}")
        
#FREINDS = input("Enter your friends name: ")

#while not FREINDS == "NONE":
 # print(f"Your friends with {FREINDS}")
  #FREINDS = input("Enter your friends name")

#print("DONE")

number1= int(input("Enter a number: "))
for number in range(number1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
        continue
    elif number % 3  == 0 :
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    else:
        print(number)