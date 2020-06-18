import random , string#import module
#welcome the user and list the menu (inspired by text based games)
print ("Welcome to my password generator!") 
print ("Here's the menu:")
print("1: set character amount")
print("2: set amount of different types of characters")
print("3: generate password")
print("4: call menu")
print("5: end usage")
#initialze and declare variables
symbols = 0
low_letters = 0
high_letters= 0
digits = 0
amount = 12

while True: #endless loop
    choice = int(input('What would you like to do? (Press 4 for the menu)')) #get input from user
    if choice ==1: 
        amount = int(input('Enter the amount of characters you want in your password: '))
        
        if amount < 4:#program will break because there's 4 types of characters
            print("Please state what type of characters you want in your password:") #program will break because there's 4 types of characters
            symbols = int(input('Enter the amount of symbols you want in your password: ')) #get input from user
            low_letters = int(input('Enter the amount of lowercase letters you want in your password: ')) #get input from user
            high_letters = int(input('Enter the amount of uppercase letters you want in your password: ')) #get input from user
            digits = int(input('Enter the amount of numbers you want in your password: ')) #get input from user
    
    elif choice == 2: 
        symbols = int(input('Enter the amount of symbols you want in your password: ')) #get input from user
        low_letters = int(input('Enter the amount of lowercase letters you want in your password: ')) #get input from user
        high_letters = int(input('Enter the amount of uppercase letters you want in your password: ')) #get input from user
        digits = int(input('Enter the amount of numbers you want in your password: ')) #get input from user
    
    elif choice == 3:   
        if symbols == 0 and low_letters == 0 and high_letters == 0 and digits == 0:
            while low_letters <1 or high_letters <1 or digits <1 or symbols <1 or low_letters+high_letters+digits+symbols > amount: #must contain at least one of each
                symbols = random.randint(0,(amount - 3)) #has to leave 3 for the other types
                low_letters = random.randint(0,((amount - symbols)+1)) #random amount of what's left
                high_letters= random.randint(0,((amount - (low_letters + symbols)+1))) #random amount of what's left
                digits = amount - (low_letters + high_letters + symbols) #the rest has to be symbols
                
        elif low_letters+high_letters+digits+symbols != amount:
            print("The amount of characters you want cannot be achieved with ")
            print("the comination of characters you want. I will be generating ")
            print("your password based on your character combination.")
            
        charStr = ''.join((random.choice(string.digits) for i in range(digits))) #make a string of random numbers
        charStr += ''.join((random.choice(string.ascii_lowercase) for i in range(low_letters))) #make a string of random lowercase letters
        charStr += ''.join((random.choice(string.ascii_uppercase) for i in range(high_letters))) #add to the string random uppercase letters
        charStr += ''.join((random.choice(string.punctuation) for i in range(symbols))) #add to the string random symbols
        
        charList = list(charStr) #make a list out of the string
        random.shuffle(charList) #mix the content of the list up
        password = ''.join(charList) #turn the list into a string again
        
        print("Password: ", password) #print out the password
    elif choice == 4:
        #just print the menu again
        print ("Here's the menu:")
        print("1: set character amount")
        print("2: set amount of different types of characters")
        print("3: generate password")
        print("4: call menu")
        print("5: end usage")
    elif choice == 5:
        break #break out of the while loop
    else: # if they enter an invalid input
        print ("Please choose one of the 5 (1, 2, 3, 4, 5) options") #Tell them what they need to do
        
#Fun fact:59% of people use the same password everywhere 