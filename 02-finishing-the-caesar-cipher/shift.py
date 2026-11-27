# output: "print"
# input: "input" (default: string)

# getting inputs from an user 
message: str = input("Message: ")
key: int = int(input("Key: "))

# print(type(message))
# print(type(key))

# 'str' -> STRING (words)
# 'int' -> INTEGER (whole numbers)

ALPHABET_SIZE : int =26
ciphertext :str  = ""

#  CONVERSION OF NORMAL TEXT INTO CIPHER TEXT
for character in message:

    # conversion of the capital text 
    if (character >= "A" and character <="Z"):
        shifted :int = ord(character) + key

    # back tracking the letter if its value Greater than 'Z' ASCIi value so this takes back , again starting from 'A'
       
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE 

        ciphertext += chr(shifted)

    #  or(character >= "a" and character <="z") -- > my code for the simple text which didnt work 
    
    # conversion of the lowercase  text 
    elif (character >= "a" and character <="z"):
        shifted = ord(character) + key
    # back tracking the letter if its value Greater than z's ASCII , so this takes back value again starting from 'a'
        if shifted > ord("z") :
            shifted -= ALPHABET_SIZE 

        ciphertext += chr(shifted)

    # conversion of the non alphabet text 
    else:
        ciphertext += character

print("THE CIPHERTEXT :",ciphertext)

plain_text=""


# conversion of the encrypted text to normal text
for character in ciphertext:
    # CAPITAL TEXT 
    if (character >= "A" and character <="Z"):
        shifted = ord(character) - key
        
    # forward tracking the letter if its value less than 'A' ASCII , so this takes back value again to 'Z'
        if (shifted < ord("A")) :
            shifted += ALPHABET_SIZE 
            plain_text += chr(shifted)

        # lower case conversion

    elif (character >= "a" and character <="z"):
         shifted = ord(character) - key
       # forward tracking the letter if its value less than 'a' ASCII , so this takes back value again to 'z'
         if (shifted < ord("a")) :
            shifted += ALPHABET_SIZE 
            plain_text += chr(shifted)
 # conversion of the non alphabet text 
    else:
        plain_text += character


print("THE PLAIN TEXT :",plain_text)


assert plain_text == message