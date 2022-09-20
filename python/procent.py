
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

