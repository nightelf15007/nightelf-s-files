import random , string#import module
symbols = 0 #declare variables
low_letters = 0 #declare variables
high_letters= 0 #declare variables
digits = 0 #declare variables
while low_letters <1 or high_letters <1 or digits <1 or symbols <1: #must contain at least one of each
    symbols = random.randint(1,9) #has to leave 3 for the other types
    low_letters = random.randint(1,(12 - symbols)) #random amount of what's left
    high_letters= random.randint(1,(12 - low_letters + symbols)) #random amount of what's left
    digits = 12 - (low_letters + high_letters + symbols) #the rest has to be symbols
charStr = ''.join((random.choice(string.digits) for i in range(digits))) #make a string of random numbers
charStr += ''.join((random.choice(string.ascii_lowercase) for i in range(low_letters))) #make a string of random lowercase letters
charStr += ''.join((random.choice(string.ascii_uppercase) for i in range(high_letters))) #add to the string random uppercase letters
charStr += ''.join((random.choice(string.punctuation) for i in range(symbols))) #add to the string random symbols
charList = list(charStr) #make a list out of the string
random.shuffle(charList) #mix the content of the list up
password = ''.join(charList) #turn the list into a string again
print("Password: ", password) #print out the password

#Fun fact:59% of people use the same password everywhere
