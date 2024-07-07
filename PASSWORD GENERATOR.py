import random
import string

length = int(input("Desired length of password: ")) #user input

s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation

s = [] 
s.extend(list(s1)) 
s.extend(list(s2))
s.extend(list(s3))
random.shuffle(s) 

passwordCreated = "".join(s[0:length]) #generating password
print(" Password is", passwordCreated) #displaying password

