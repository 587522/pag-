import string #imports the string module (is this necessary)
#allows the user to input text and encrypts it
#then writes it to the file encrpyted.txt (add more comments and docstrings
"""
def encrypt():
    fobject = open('original.txt', 'w')
    x = input("Enter text: ")
    str(fobject.write(x))
    fobject.close()
    
    encrypt = open('encrypted.txt', 'w')
    #listalpha = list(string.ascii_lowercase)
    y = list(x[::-1])
    del y[0]
    y.append('oy')
    z = ''.join(y)
    encrypt.write(str(z))
    encrypt.close()
encrypt()
"""
def encryption():
    fobject = open('original.txt', 'w')
    x = input("Enter text: ")
    output = []
    str(fobject.write(x))
    fobject.close()
    
    encrypt = open('encrypted.txt','w')
    key = int(input("Enter key (numbers 1-26): "))
              
    for character in x:
          number = ord(character) - 96
          output.append(number)
          print (output)#can remove this later
                  
    if key <=26:
          newnumbers = output.append(key)
          y = int(newnumbers.append(96))
          final_output = chr(y)
          output = ''.join()
          encrypt.write(str(final_output))

    encrypt.close()
encryption()              
    



