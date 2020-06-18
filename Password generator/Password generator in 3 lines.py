import string , random
chars=string.ascii_letters + string.digits + string.punctuation 
print("Password: " + ''.join(random.choice(chars) for i in range(12))) 