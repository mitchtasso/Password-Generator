import random
import string

length = 8
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
characters = string.punctuation
        
def generatePass():
    passwordStore = []
    password = ''
    for i in range(0,length):
        if i <= 1:
            gen = random.randint(0,len(lowercase)-1)
            passwordStore.append(lowercase[gen])
        elif i > 1 and i <= 3:
            gen = random.randint(0,len(uppercase)-1)
            passwordStore.append(uppercase[gen])
        elif i > 3 and i <= 5:
            gen = random.randint(0,len(digits)-1)
            passwordStore.append(digits[gen])
        elif i > 5 and i <= length:
            gen = random.randint(0,len(characters)-1)
            passwordStore.append(characters[gen])
    
    random.shuffle(passwordStore)
    for x in range(0,length):
        password += passwordStore[x]
    print(password)

if __name__ == "__main__":
    generatePass()