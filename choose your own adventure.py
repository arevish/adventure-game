name = input("Type your name: ")
print("Welcome ",name, "to this adventure!")
choice1 =input("You are on a dirt road, it has come to an end you can go lEFT and RIGHT, which way you like to go?\n ").lower()
if choice1 == "left":
    choice2 = input(f"\nYou Turn {choice1}, And Now you came to a river, you can walk around it or swim accross it, \n\n Type WALK to Walk around and SWIM to swim accross:\n ").lower()
    if choice2 == "walk":
        choice3 =input(f"\nYou choose to {choice2}, You walk around the river and reached the green land jungle, there are lions sitting behind the bushes, you can run through the bushes or walk very slowly without disturbing them.\n\n Type RUN to run through bushes or WALK to walk slowly :\n ").lower()
        if choice3 == "run":
            print("\nLions saw you running. You got eaten by lions, You loose !")
        elif choice3 =="walk":
            choice4 = input("\nYou passed the lions safely and reached the mountain area.You have to reach other side of mountains. you can climb it or you can walk through the jungle.\n\n Type CLIMB to climb the mountain or WALK to go though jungle\n ").lower()
            if choice4 == "climb":
                print("\nCONGRATULATIONS! you reach other side of the mountain.\nYOU WIN!!")
            elif choice4== "walk":
                print("\nYou got bitten by the snake in dense jungle. You died")
    elif choice2== "swim":
        print(f"\nYou choose to {choice2}, You tried to swim but get drowned in it due to fast current, YOUO LOOSE!")
elif choice1 == "right":
    choice12= input(f"\nYou Turn {choice1}, You reached big trees area you can eat fruits from it or walk pass by it. \n\n Type EAT to climb the tree and eat fruits or PASS to walk pass by it\n ").lower()
    if choice12 == "eat":
        print("\nYou ate the fruits all the way and reached the muddy area and got stuck in a swamp and got eaten by aligators. You loose!")
    elif choice12 == "pass":
        print("\nYou walked for few days and die because of hunger !, YOU LOOSE!")    
else:
    print("Not a valid option. You loose.")

print("\nThank you for trying", name)