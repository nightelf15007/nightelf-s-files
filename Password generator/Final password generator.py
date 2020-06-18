#import the modules
import random , string
#create the password class
class password:
    def __init__(self, symbols, low_letters, high_letters, digits, length):
        self.symbols = symbols
        self.low_letters = low_letters
        self.high_letters= high_letters
        self.digits = digits
        self.length = length
#create an instance of password        
pw = password(0,0,0,0,12)

#define the menu function
def menu():
    print ("Here's the menu:")
    print("1: set character amount")
    print("2: set amount of different types of characters")
    print("3: generate password")
    print("4: call menu")
    print("5: end usage")
    
#define the character combination function
def character_combination(password):
    pw.symbols = int(input("Enter the amount of symbols you want in your password: ")) #user input 
    pw.low_letters = int(input("Enter the amount of lowercase letters you want in your password: ")) #user input
    pw.high_letters = int(input("Enter the amount of uppercase letters you want in your password: ")) #user input
    pw.digits = int(input("Enter the amount of numbers you want in your password: ")) #user input

#apparently we have to work in the main method so...
#endless loop
while True:
    choice = int(input("What would you like to do? (Press 4 for the menu)")) #user input
    if choice ==1:
        #initialize the character compinations
        pw.symbols = 0
        pw.low_letters = 0
        pw.high_letters = 0
        pw.digits = 0
        #get the length
        pw.length = int(input("Enter the amount of characters you want in your password: ")) #user input
        #if the length is shorter than the amount of different characters
        if pw.length < 4:
            print("Please state what type of characters you want in your password:")
            character_combination(pw) #ask for the character combination
    elif choice == 2:
        character_combination(pw) # get the character combination
    elif choice == 3:
        #if the character combinations hasn't been set
        if pw.symbols == 0 and pw.low_letters == 0 and pw.high_letters == 0 and pw.digits == 0:
            #while any of the character type amounts are zero or the total of the stated character types exceed the desired length
            while pw.low_letters <1 or pw.high_letters <1 or pw.digits <1 or pw.symbols <1 or pw.low_letters + pw.high_letters + pw.digits + pw.symbols > pw.length:
                pw.symbols = random.randint(0,(pw.length - 3)) #get a random amount and leave at least 3 for the other 3 character types
                pw.low_letters = random.randint(0,((pw.length - pw.symbols)+1)) #get a random amount
                pw.high_letters= random.randint(0,((pw.length - (pw.low_letters + pw.symbols)+1))) #get a random amount
                pw.digits = pw.length - (pw.low_letters + pw.high_letters + pw.symbols)  #the rest goes to the numbers
        
        #if the total does not equal the length
        elif pw.low_letters + pw.high_letters + pw.digits + pw.symbols != pw.length:
            #inform the user
            print("The amount of characters you want cannot be achieved with the comination of characters ")
            print("you want. I will be generating your password based on your character combination.")
        
        #make a string of the stated characters
        charStr = ''.join((random.choice(string.digits) for i in range(pw.digits))) #add the stated amount of numbers
        charStr += ''.join((random.choice(string.ascii_lowercase) for i in range(pw.low_letters))) #add the stated amount of lowercase letters
        charStr += ''.join((random.choice(string.ascii_uppercase) for i in range(pw.high_letters))) #add the stated amount of uppercase letters
        charStr += ''.join((random.choice(string.punctuation) for i in range(pw.symbols))) #add the stated amout of symbols
        
        charList = list(charStr) #turn the  tring into a list
        random.shuffle(charList) #shuffle the list
        passwordStr = ''.join(charList) #create a new string with the shuffled characters
        print("Password: ", passwordStr) # print the password
    elif choice == 4:
        menu() #call the menu
    elif choice == 5:
        break #break out of the endless loop
    else:
        #tell the user what to do
        print ("Please choose one of the 5 (1, 2, 3, 4, 5) options")
        
#Fun fact:59% of people use the same password everywhere 