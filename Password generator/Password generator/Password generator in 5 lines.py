import string
import random
chars=string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for i in range(12))
print("Password: " + password)