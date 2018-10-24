#Humyra Taifoor
#Encryption and file input/output
#October 24 2018

import string #imports the string module 
#this is one of the encrypting functions
#it will take your words, reverse the letters of the whole phrase, and add an oy to the last word of the sentence.
#it will take message, write it to the file called original.text to store it and then
# it will encrypt it, and write it to the file called encrypted.txt

def encrypt():
    """(str) -> str
    Takes an input and returns your encrypted message in the file called encrypted.txt
    hi
    >>>ihoy
    this is cool
    >>>looc si sihtoy
    """
    #fobject = open('original.txt', 'w') #opens the original.txt file and allows the option to write to it
    x = input("Enter text: ")           #allows the user to input a phrase
    #str(fobject.write(x))               #writes the inputted phrase to the file
    #fobject.close()                     #closes the file
    
    encrypt = open('encrypted.txt', 'w')#opens the encrypted.txt file and allows the option to write to it
    y = list(x[::-1])                   #turns the phrase into a list and then reverses the letters of the phrase
    y.append('oy')                      #adds an oy to the end of the last word of the reversed phrase 
    z = ''.join(y)                      #turns the list back into a string
    print("Your encrypted message is: " +z)                            #prints the encrypted message
    encrypt.write(str(z))               #writes the message to the file
    encrypt.close()                     #closes the file

    

#this is another encryption function but this uses caesar cipher 
def encryption():
    """(str)-> str
    Takes an input and a key, and then using the key, encrypts the message and returns the encrypted messaged
    hi
    1
    >>>ij
    hello
    2
    >>>jgnnq
    """
    #fobject = open('original.txt', 'w') #opens the original.txt file and allows the option to write to it
    x = input("Enter text: ")           #allows the user to input a phrase
    output = []                         #this allows the appending of numbers to these variables later
    finaloutput = []
    finalword = []
    #str(fobject.write(x))               #writes the inputted phrase to the file
    #fobject.close()                     #closes the file
    
    encrypt = open('encrypted.txt','w') #opens the encrypted.txt file and allows the option to write to it
    key = int(input("Enter key (numbers 1-26): "))#asks for a key to shift the numbers
              
    for character in x:                 #a for loop for every character in the variable x
          number = ord(character)       #turns each letter into a number
          output.append(number)         #appends each number to the variable output 
          
   
    for character in output:            #a for loop for every character in output
          character = int(character) + int(key)#adds the key to the number that represents the letter from the inpuuted message
          finaloutput.append(character) #appends each number to the variable finaloutput
    x = finaloutput
     
    for i in x:                         #a for loop for every i in the variable x
        finalword.append(chr(i)) #turns the numbers back into letters and appends them to the variable finalword
    y = finalword
    newword = ''.join(y)        #turns the list of the letters into a string
    print("Your encrypted message is: " +newword)                      #prints the encrypted message
    encrypt.write(newword)              #writes the encrypted message to the file
    encrypt.close()                     #closes the file

def decrypt():
     """(str)->str
     Reads the file encrypted.txt and decrypts the message and returns the decrypted message
     ihoy
     >>>hi
     looc si sihtoy
     >>>this is cool
     """
     decrypt = open('encrypted.txt', 'r')#opens the file encrypted.txt
     x = decrypt.read()                  #reads the file and the things in the file is assigned to the variable x
     y = list(x[::-1])                   #turns the phrase into a list and reverses the letters
     y.remove('y')                       #removes the 'y' that was orginally added
     y.remove('o')                       #removes the 'o' that was orginally added
     z = ''.join(y)                      #turns the list back into a string
     print("Your decrypted message is: " +z)#prints the decrypted message
     decrypt.close                          #closes the file

     original = open('original.txt', 'w') #opens the file original.txt
     original.write(z)                    #writes the decrypted message to the original file
     original.close()                     #closes the file

#reads the file encrypted.txt and decrypts the phrase from it     
def decryption():
    """(str)-> str
    Reads the file encrypted.txt and decrypts the message and returns the decrypted message
    ij
    1
    >>>hi
    jgnnq
    2
    >>>hello
    """
    decryption = open('encrypted.txt', 'r') #opens the file encrypted.txt
    x = decryption.read()               #assigns the variable x to whatever items are in the file
    output = []                         #this allows the appending of numbers to these variables later  
    finaloutput = []
    finalword = []
    key = (int(input("What's the key: "))) #asks for a key to shift the numbers
          
    for character in x:                  #a for loop for every character in the variable x
        number = ord(character)       #turns each letter into a number
        output.append(number)         #appends each number to the variable output 

    for character in output:            #a for loop for every character in output
        character = int(character) - int(key)#subtracts the key to the number that represents the letter from the encrypted message
        finaloutput.append(character) #appends each number to the variable finaloutput

    x = finaloutput

    for i in x:                          #a for loop for every i in the variable x
        finalword.append(chr(i))               #turns the numbers back into letters and appends them to the variable finalword
    y = finalword
    newword = ''.join(y)               #turns the list of the letters into a string
    print("Your decrypted message is: " + newword)                      #prints the decrypted message

    decryption.close                    #closes the file

    original = open('original.txt', 'w')#opens the file original.txt
    original.write(newword)             #writes the varaible newword to the file which is basically the decrypted message 
    original.close()                    #closes the file

#this means that the encryption function was called and in this function,
#it asks which encryption process to use and calls the approprate fuunction
def encryption_time():
    """
    (str)->str
    1
    >>> #will call the encrypt function and run that
    2
    >>> #will call the encryption function and run that 
    """
    hello = input("If you want to try the first encryption, type '1', if you want to try the second encryption, type '2': ")
    if hello == '1':
        encrypt()
    if hello == '2':
        encryption()
#this means that the decryption function was called and in this function,
#it asks which decryption process to use and calls the approprate fuunction
def decryption_time():
    """
    (str)->str
    1
    >>> #will call the decrypt function and run that
    2
    >>> #will call the decryption function and run that 
    """
    woah = input("Try encryption first then this! So refresh the page! If you did the first encryption, then type '1', if you did the second encryption, type '2': ")
    if woah == '1':
        decrypt()
    if woah == '2':
        decryption()

#!!! this is the first thing that runs. It asks if you want to encrypt or decrypt and then calls the appropriate function
start = input("Do you want to encrypt or decrypt today?If you want to encrypt, type '1', if you want to decrypt, type '2': ")
if start == '1':
    encryption_time()
if start == '2':
    decryption_time()



