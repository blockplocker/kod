from multiprocessing.resource_sharer import stop
from random import *

print("_________________________________________________")
namn = input("Araz; Hello my name is araz what is your name? ")

hp = 100
araz_hp = 100
atk_multiplier = 1

# pedo araz
if namn == "barn" or namn == "kid":
    print("Araz; hi i love kids")
    print("Araz; i will not fight you i will rape you ahahahah")
    print("defeat araz raped you")
    exit()

# 200hp
elif namn == ("max"):
    hp = 200

# dubble damage
elif namn == ("araz"):
    atk_multiplier = 2


print("Araz; hi ", namn, " have you come to fight with me? yes or no ")
val = input()
if val == "yes":

    print("Araz; come and fight me i'm ready ")
    print("")
    print("kick deals 25 damage and has 50% chance to hit. punch deals 10 damage and has 80% chance to hit ")
    if namn == ("kassim") or namn == ("Top G"):
        print("Becuse u are a Top G u have a special attack sparkling water toss that deals 50 hp and has a 30% chance to hit ")

    while True:
        if araz_hp <= 0:
            print("Mission sucsess Araz was slain ")
            print("")
            break

        elif hp <= 0:
            print("Defeat \n araz killed you")
            print("")
            break

        print("you have ", hp, " hp left and araz has ", araz_hp, " hp left")
        print("_________________________________________________")
        print("____________________ new round __________________")
        print("_________________________________________________")

#------------------------------- special attack ---------------------------------------
        if namn == ("kassim") or namn == ("Top G"):
            print("s for sparkling water toss")
        val2 = input("k for kick and p for punch ")
        print("")

# ---------------------------  sparkling water toss ------------------------------------
        if val2 == "s" and namn == ("kassim") or namn == ("Top G"):
            k = randrange(1, 101)
            if k < 31:
                araz_hp = araz_hp - 50
                b = randrange(1, 3)
                if b == 1:
                    print("araz got sparkling water in his eyes and it dealt 50 hp")
                else:
                    print(
                        "araz eyes are burning the sparkling water took 50 hp from him")
                print("")
            else:
                print("miss araz opend his mouth and drank the water")
                print("")

        # --------------------------- kick ---------------------------------
        elif val2 == "k":
            k = randrange(1, 101)
            if k < 51:
                araz_hp = araz_hp - 25 * atk_multiplier
                print("sucsess araz took 25 hp")
                print("")
            else:
                print("miss araz dodged")
                print("")

        #----------------------------- punch ---------------------------------
        elif val2 == "p":
            k = randrange(1, 101)
            if k < 81:
                araz_hp = araz_hp - 10 * atk_multiplier
                print("sucsess araz took 10 hp")
                print("")
            else:
                print("miss araz dodged")
                print("")

        print("you have ", hp, " hp left and araz has ", araz_hp, " hp left")
        print("_________________________________________________")

        araz_val = randrange(1, 4)

        # --------------------------------- araz kick ---------------------------
        if araz_val == 1:
            print("araz chose to kick")
            k = randrange(1, 101)
            if k < 51:
                hp = hp - 25
                print("araz dealt 25 hp to you")
                print("")
            else:
                print("araz missed you dodged")
                print("")

        #--------------------------------- araz punch ---------------------------------
        elif araz_val == 2:
            print("araz chose to punch")
            k = randrange(1, 101)
            if k < 81:
                hp = hp - 10
                print("araz dealt 10 hp to you")
                print("")
            else:
                print("araz missed you dodged")
                print("")

        #--------------------------------- araz fart attack ---------------------------------
        elif araz_val == 3:
            k = randrange(1, 101)
            if k < 51:
                hp = hp - 30
                print("araz farted on you and dealt 30 hp")
            else:
                print("araz tried to fart on you but only poop came out")

else:
    print("yes or no")
    exit()
exit()
