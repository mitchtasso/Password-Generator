import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
characters = string.punctuation
all = lowercase + uppercase + digits + characters
        
def generatePass(length):
    passwordStore = []
    password = ''
    #Randomly selects and adds characters to the password array, makes sure that at least two of each type exist.
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
        elif i > 5 and i <= 8:
            gen = random.randint(0,len(characters)-1)
            passwordStore.append(characters[gen])
        else:
            gen = random.randint(0,len(all)-1)
            passwordStore.append(all[gen])
    
    #Shuffles and 
    random.shuffle(passwordStore)
    for x in range(0,length):
        password += passwordStore[x]
    print(password)

if __name__ == "__main__":
    
    while(True):
        print("Please enter the desired length for your password. (8-24 Characters)\n")
        length = input("Length: ")
        if int(length) >= 8 and int(length) <= 24:
            break
        else:
            print("\nPlease enter a valid length.\n")
            continue
    
    generatePass(int(length))