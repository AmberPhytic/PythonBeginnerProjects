name = input("Hi, what's your name?: ")
print("Welcome", name, "are you ready for a wild adventure?!")

answer = input(" You've come to a fork in the road. Wich direction do you want to turn, left or right? " ).lower()


if answer == "left":
    answer = input (" Woah! What is that over there?! Do you see that?! It's a pirate ship! Are we wanting to take it? yes or No? " ).lower()

    if answer == "yes":
        Q2_answer = input ("Sweet! These guys look kinda shady. Ask to join them anyway? Type, 'yes' for yes & 'no' for no. " ).lower()

        if Q2_answer == "yes":
            Q2_answer = input ("Damn, the party ended so early. You shared many laughs with these guys. Had deep conversations over drinks...you should of trusted your gut though. :C They traded you for a bag of potatos. :, C ")

        elif Q2_answer =="no":
            Q2_answer = input ("You made a fantastic choice. Ounce you contiued your path, you ran into a friendly trutle carrying a golden box. He gave it to you. How exciting! I hope you can find the key! ")

        else:
            print("Wah, wah, wah...you fell into a pool of lava. R.I.P ")
                
    elif answer == "no":
        print("You couldn't have made a better choice. You walked many miles but eventually you ended running into a gorgeous cottage with an even more beautful maiden living alone within it's walls. She fell in love with you & you with her. You all lived together happy as can be, well into your old age. <3 " )

    else:
        print("Sorry, that's not a valid optioin. A commet came barreling down form the sky and killed you. ")

            

elif answer == "right":
    Q3_answer = input("I've never seen such a gorgeous field of flowers. Do you want to explore it? Type, 'yes' for yes & 'no' for no. ").lower()

    if Q3_answer =="yes":
        print("Oh wow! You've founded a golden key! I wonder what it opens??" )

    elif Q3_answer =="no":
        print("Ughh, how lame. You followed the path all the way to a cliff. Atleast you have an abundant amount of rations & water. ")
                
else:
    print("Oh no, you ran into a hacksaw. R.I.P" )



