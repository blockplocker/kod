""""
#procent räknare
val = int(str(input("1 för %procent 2 för *gånger: ")))

if val == 1:
    tal = int(float(input("Ange ett tal: ")))
    procent = int(float(input("Hur många procent av talet: ")))
    procent = procent/100
    print(procent*100,"% av", tal,"=", tal*procent)

elif val == 2:
    x = int(float(input("Ange ett tal: ")))
    y = int(float(input("Andra talet: ")))
    print("svar=", x*y)

else:
    print ("Du ska välja % eller *")
"""


radie = float(input("Ange en radie: "))
volym = (4*3.14*radie**3)/3
area = 4*3.14*radie**2
print("volym = ", volym)
print("area = ", area)
