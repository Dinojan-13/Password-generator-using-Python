import random
import string

print(" Password Generator")

length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits 

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

print("Your generated password is:")
print(password)
