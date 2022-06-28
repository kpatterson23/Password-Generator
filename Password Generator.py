import random

print("Welcome to Password Generator v1.0.") # Greets user
print("ATTENTION: All passwords will contain at least of the following: 1 uppercase letter, 1 lowercase letter, 1 numeric digit, and 1 punctuation mark.") # Warns user what the limitations of of the password program are

def shuffle(password): # Function to shuffle randomly generated password
    templist = list(password)
    random.shuffle(templist)
    return ''.join(templist)

uppercase_letter1 = chr(random.randint(65,90)) #Generates a random Uppercase letter
uppercase_letter2 = chr(random.randint(65,90)) #Generates a 2nd random Uppercase letter
lowercase_letter1 = chr(random.randint(97,122)) #Generates a random lowercase letter
lowercase_letter2 = chr(random.randint(97, 122)) #Generates a 2nd random lowercase letter
digit1 = random.randint(48, 57) # Generates a random number
digit2 = random.randint(48, 57) # Generates a 2nd random number
punct_1 = chr(random.randint(33, 152)) # Generates a random punctuation mark
punct_2 = chr(random.randint(33, 152)) # Generates a 2nd ranom punctuation mark

password = uppercase_letter1 + uppercase_letter2 + lowercase_letter1 + lowercase_letter2 + str(digit1) + str(digit2) + punct_1 + punct_2   
password = shuffle(password) # Calls the Shuffle function, passing in the original password, shuffling it and returning it to this variable

print("Your new password is: {password}".format(password = password)) #Prints out a statement and the new password