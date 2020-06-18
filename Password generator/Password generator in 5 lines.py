import string #imort module (this is abselute magic)
import random #import module 
chars=string.ascii_letters + string.digits + string.punctuation #choose characters from letters, numbers and symbols
password = ''.join(random.choice(chars) for i in range(12)) #make a string out of the random characters
print("Password: " + password) #print the string

#Fun fact:59% of people use the same password everywhere.