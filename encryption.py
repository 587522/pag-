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
    finaloutput = []
    finalword = []
    str(fobject.write(x))
    fobject.close()
    
    encrypt = open('encrypted.txt','w')
    key = int(input("Enter key (numbers 1-26): "))
              
    for character in x:
          number = ord(character) - 96
          output.append(number)
          
          #output2 = ''.join(str(output))
    print (output)#can remove this later
          
    #print(output2)
    for character in output:
          character = int(character) + int(key)
          finaloutput.append(character)
    print(finaloutput)
    
    for i in finaloutput: 
         finalword.append((chr(i)))
    print(finalword)
    print(''.join(finalword))
    
    """

          y = int(newnumbers.append(96))
          final_output = chr(y)
          output = ''.join()
          encrypt.write(str(a))
          """

    encrypt.close()
encryption()              
    
    



