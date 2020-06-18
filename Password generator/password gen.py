import random #import module
import string #import module (this is the one that makes the whole thing work)
digits = random.randint(1, 11) #the total should be 12 characters and there should be at least digits and
letters = 12 - digits           #the rest should be letters
#define generate password function
def generate_password(digits, letters): 
    charStr = ''.join((random.choice(string.digits) for i in range(digits))) #create a string containing the amount of random numbers randomly chosen 
    charStr += ''.join((random.choice(string.ascii_letters) for i in range(letters))) #add the amount of random letters randomly chosen to the string
    charList = list(charStr) #turn the string into a list of characters
    random.shuffle(charList) #shuffle the characters around  
    password = ''.join(charList) #save the new order into a variable
    return password #return the password
print("Password: ", generate_password(digits, letters)) #print the password

#Fun fact: It would take an attacker up to 7 months to bruteforce this password, assuming the keys per second is still 17042497.3kps
