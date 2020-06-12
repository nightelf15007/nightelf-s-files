#dice roll game
def roll_dice(): 
    import random #import module
    #welcome the players and list the game menu (inspired by text based games)
    print ("Welcome to my dice game!") 
    print ("Here's the game menu:")
    print("1: set limits")
    print("2: set amount of dice")
    print("3: roll dice")
    print("4: call menu")
    print("5: end game")
    #initialze and declare variables
    choice = 0 
    min_value = 1 # a normal dice has 1 as minimum
    max_value = 6 # a normal dice has 6 as maximum
    amount = 1 # amount of dice
    usage = amount # usage placeholder for choice 3
    while True: #endless loop
        choice = int(input('What would you like to do? (Press "4" for the game menu)')) #get input from user
        if choice ==1: 
            try: #try to get values from user
                min_value = 0
                max_value = 0
                while min_value >= max_value:
                    min_value = int(input("Enter the minimum value of the die: "))
                    max_value = int(input("Enter the maximum value of the die: "))
            except: #if the user enters anything that's not numbers, I will just go back to 1 and 6
                print("I will just use 1-6") #tell the user that this is what I be doing
                min_value = 1 # a normal dice has 1 as minimum
                max_value = 6 # a normal dice has 6 as maximum
                
        elif choice == 2: 
            amount = int(input('Enter the amount of the dice you want: ')) #get the amount of dice they want
        elif choice == 3:
            usage = amount #I did this to be able to keep the amount
            while usage > 0: # just to get the amount of die they want
                print(random.randint(min_value, max_value)) # print a value
                usage -= 1 #reduce the amount left to print
        elif choice == 4:
            #just print the menu again
            print ("Here's the game menu:")
            print("1: set limits")
            print("2: set amount of dice")
            print("3: roll dice")
            print("4: call menu")
            print("5: end game")
        elif choice == 5:
            break #break out of the while loop
        else: # if they enter an invalid input
            print ('Please choose one of the 5 (1, 2, 3, 4, 5) options. Press "4" for the game menu') #Tell then what they need to do
roll_dice()


#fun fact about dice: did you know that a normal six sided dice's opposite sides always add up to 7?
