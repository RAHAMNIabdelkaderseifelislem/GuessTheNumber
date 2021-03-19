import random
import sys


def menu():
    print("1. Play Game\n\n2. How to Play\n\n3. Exit\n\n")
    men = int(input("Enter number from one to three [1,2,3]"))
    while(men < 1 or men > 3):
        men = int(input("Please enter number from one to three [1,2,3]\n"))
    if men == 1:
        lev()
    elif men == 2:
        print("You have to choose level from the six levels")
        print("1st Rule: You have only 5 tries")
        print("Computer will Generate random number the hole game")
        print("Every Level has number of possibilities")
        print("Very Easy from 1 to 10")
        print("Easy from 1 to 100")
        print("Normal from 1 to 1000")
        print("Hard from 1 to 10000")
        print("Very Hard from 1 to 100000")
        print("Impossible from 1 to 1000000000(one Billion of possibilities)")
        s=input("Press any key than enter to return to top menu")
        menu()
    else:
        sys.exit()
        
def lev():
    print("Levels :\n1. Very Easy\n2. Easy\n3. Normal\n4. Hard\n5. Very Hard\n6. Impossible\n\n0. Exit")
    level = int(input("Which level you want to play?"))
    while(level < 0 and level > 6):
        level = int(input("Please enter number from range of zero to six [0,1,2,3,4,5,6,7]\n"))
    if level == 1:
        number = random.randint(1,10)
        game(number)
    elif level == 2 :
        number = random.randint(1,100)
        game(number)
    elif level == 3 :
        number = random.randint(1,1000)
        game(number)
    elif level == 4 :
        number = random.randint(1,10000)
        game(number)
    elif level == 5 :
        number = random.randint(1,100000)
        game(number)
    elif level == 6 :
        number = random.randint(1,1000000000)
        game(number)
    else:
        sys.exit()

def game(number):
    for i in range(5):
        user = int(input("Guess The Number"))
        if user == number:
            print("Wow!!!!")
            print("you guessed the number right it's ",number)
            break
        elif user <= number:
            print("It's higher than ",user)
            print("Remain ",(4-i+1))
        elif user >= number:
            print("It's lower than ",user)
            print("Remain ",(4-i))
    if user!= number:
        print("Your guess is incorrect the number is ",number)
    s=input("Press any key than enter to return to top menu")
    menu()

menu()