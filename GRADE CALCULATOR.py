G1 =int(input("ENTER FIRST GRADING GRADE:"))
G2 =int(input("ENTER SECOND GRADING GRADE:"))
G3 =int(input("ENTER THIRD GRADING GRADE:"))
G4 =int(input("ENTER FOURTH GRADING GRADE:"))
overall=(G1 + G2 + G3 + G4)/4

if overall >= 70 and overall <= 89:
    print(f"{overall} CONGRATS YOU HAVE PASS")
elif overall >= 90 and overall <= 94:
    print (f"{overall} WITH HONORS")
elif overall >= 95 and overall <= 97:
    print (f"{overall} WITH HIGH HONORS")
elif overall >= 98 and overall <= 100:
    print (f"{overall} WITH HIGHEST HONORS")
else: 
    print("YOU FAILED GO BACK TO STUDYING")