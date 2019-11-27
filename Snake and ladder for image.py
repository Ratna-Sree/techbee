#3) write a backend of the snake and ladder game
#and write how many attempts you took to complete the game.

title="Welcome to Ratna's Snake and Ladder"
print (70*'*')
print (title.center(70,' '))
print (70*'*')

start=input("\nPlease enter 'Y' to start the snake and ladder game :")
import random
pos=0
count=0

if start=='y' or start=='Y':
    while pos < 100:
        
        dice=random.randrange(1,7)                      #This is the dice roll using random module
        print("\nDice rolled to: ",dice,"|",end=" ")
        
        count += 1                                      # count of the loop
        pos += dice                                     # position will be incremented with dice value
            
        if pos > 100:                                   # Position greater than hundred is not allowed
            pos -= dice
            if dice==6:                                 # Extra dice for 6 is not allowed after 94
                continue;
        elif pos==100:                                  # Final step reached, break the loop and print the final statement
            break;

        elif dice==6:                                   # extra dice chance is given for 6
            print("Pawn position at: ",pos)
            print("Its a six, one more chance")
            dice=random.randrange(1,7)
            pos += dice
            if pos > 100:
                pos -= dice
            print("Dice rolled to: ",dice,"|",end=" ")

# Actual ladder and snakes check / and print the pawn position
        if pos==1:
            pos=38
            print("Hurrey its a ladder, going to position :",pos)
        elif pos==4:
            pos=14
            print("Its a ladder, going to position :",pos)
        elif pos==9:
            pos=31
            print("Its a ladder, going to position :",pos)
        elif pos==17:
            pos=7
            print("Ohh its a snake, going to position :",pos)
        elif pos==21:
            pos=42
            print("Its a ladder, going to position :",pos)
        elif pos==28:
            pos=84
            print("Its a longest ladder, going to position :",pos)
        elif pos==51:
            pos=67
            print("Its a ladder, going to position :",pos)
        elif pos==54:
            pos=34
            print("Ohh its a snake, going to position :",pos)
        elif pos==62:
            pos=19
            print("Ohh its a snake, going to position :",pos)
        elif pos==64:
            pos=60
            print("Ohh its a snake, going to position :",pos)
        elif pos==72:
            pos=91
            print("Its a ladder, going to position :",pos)
        elif pos==80:
            pos=99
            print("Its a ladder, going to position :",pos)
        elif pos==87:
            pos=36
            print("Ohh its a snake, going to position :",pos)
        elif pos==92:
            pos=73
            print("Ohh its a snake, going to position :",pos)
        elif pos==95:
            pos=75
            print("Ohh its a snake, going to position :",pos)
        elif pos==98:
            pos=79
            print("Ohh its a snake, going to position :",pos)
        else:
            print("Pawn position at: ",pos)

print("\nCongratulations, you completed game in '{}' attempts".format(count))

