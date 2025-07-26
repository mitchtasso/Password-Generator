import random
import string
import streamlit as st

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
    
    #Shuffles and assigns to string
    random.shuffle(passwordStore)
    for x in range(0,length):
        password += passwordStore[x]
    return password


#Frontend

st.set_page_config(page_title="Password Generator", page_icon="logo.png")
st.image("logo.png", width=100)
st.title("Password Generator")
number = st.number_input("Length of password (Min 8, Max 24)",min_value=8, max_value=24)
generate = st.button("Generate")

if generate:
    st.text(generatePass(number))