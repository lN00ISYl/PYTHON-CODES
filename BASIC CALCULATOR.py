NUMBER = float(input("ENTER A NUMBER:"))
NUMBER2= float(input("ENTER A NUMBER:"))
operator = input("CHOSE AN OPERATIOR (+,/,-,*):")

if operator =="+":
    result= NUMBER + NUMBER2
    print(result)
if operator =="-":
    result= NUMBER - NUMBER2
    print(result)
if operator =="*":
    result= NUMBER * NUMBER2
    print(result)
if operator =="/":
    result= NUMBER / NUMBER2
    print(result)
else:
    print("INVALID OPERATOR")