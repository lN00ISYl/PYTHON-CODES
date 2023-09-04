#KARLOS SON P. RIVO
#UP-FA1-BSIT01
Money=int("1000")
Interest=float(".03")
Year=int("5")
Investment= Money*(1+Interest)**Year
rounded = round(Investment, 2)
print("The Future value of the investment:",rounded ,"USD")