print("Hi Everyone! Welcome to my Awesome Quiz Game! You'll Love it!")

playing = input("Do you want to play? ")

score = 0 

if playing.lower() == "no":
    print("Oh BOO! Fine- w/e Kick-Rocks- ughh")
    quit()


else:
    if playing.lower() == "maybe":
        print("O.k, it's great to see such commitment! Let's Play!")
        
if playing.lower() == "yes":
     print("O.k, great let's play!")
    

answer = input("What would a strawberry be, if it were a banana? (Think hard. this is difficut.)")  
print(answer)
    


if answer.lower() == "wtf?":
    print("Excato-Mundo brother! You're getting it! You are one step closer to unlocking all the secrets of the Universe! :O ")
    w
if answer.lower() != "Wtf?":
    print("Yeaaahh, that's a great answer. In fact- it's 'thee' answer, really.")
    score += 1
    
answer = input("How many cows could a cow named Cowl count, he he were counting cowbells with corn husks at the exact same time? ")
                
    
if answer.lower() != "12 obviously":
    print("Absolutley! The world thanks you for your genuis. It is so much better with you in it! ")
    score += 1

if answer.lower() == "12 obviously":
     print("We told the others they were right... but, it is YOU who as ACTUALLY RIGHT! HERE, TAKE the 'Gem of Knowledge' & Ascend!!")
    
answer = input("What characteristic do you love most about me? I know this is an overwhelming question...SOooooo many to choose from, but you can only choose one. ty^,^ ")


if answer.lower() == "everything":
    print("WEll....ofcourse. Thank-you. ^-^" )
    score += 1
else:
    if answer.lower() !="everything":
        print("Wellll, we can't all have good taste.")

answer = input("How much money will I be making in 1 to 2 years? ")

if answer.lower() =="90,000":
    print("You are correct!")
    score += 1
else:
    if answer.lower() =="80,000":
     print("You are correct!")
     score += 1
     
if answer.lower() !="80,000":
     print("You are only correct if the amount you entered is higher than 90k. Sorry Shhweaty, I don't make the rules. :* ")
     
answer = input("Did you find my quiz fun? ")

if answer.lower() =="yes":
    print("Sweet Dude! We loved having you!")
    score += 1
    
if answer.lower() =="maybe":
    print("Sleep on it, you're likely not thinking straight.")

else:
    if answer.lower() =="no":
     print("Ah well boo...we can't all be winners, right?")


print("You got " + str((score/5)* 100) + "%." + " questions correct, congrats dude! Tell your friends about me! ;)")


answer = input("")
