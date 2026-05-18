import random 
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "!£$%^&*+_-@~#:?<>¬"

all_chars = lower + upper + numbers + symbols
lenght = int(input("Enter a lenght number : "))

password = ''. join(random.sample(all_chars, lenght))
print('Generated:', password)

