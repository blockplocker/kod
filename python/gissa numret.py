import numbers
from random import *




print("")
print("")
print("")
while True:
    

    x = randrange(1,601)
    y = randrange(700,2001)
    number = randrange(x,y)
    low = x
    high = y
    # number = randrange(1, 1001)
    score = 150
    # low = 1
    # high = 1000

    print("___________________________________________")
    choice = input("yes to play  ")
    print("___________________________________________")


    if choice == "yes" or choice == "Yes":

        while True:
            print("the number is between ", low, " and ", high)
            guess = input("guess the number: ")
            guess = int(guess)

            if number == guess:
                print("you guessed the number your score is ", score)
                break

            elif score == 0:
                print("defeat")
                break

            elif number < guess:
                # print("too high")
                print("score: ",score)
                score = score - 10
                if guess < high:
                    high = guess

            elif number > guess:
                # print("too low")
                print("score: ",score)
                score = score - 10
                if guess > low:
                    low = guess


            print("___________________________________________")
    else:
        print("ok bye")
        break

