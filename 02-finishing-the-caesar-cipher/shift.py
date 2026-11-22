# output: "print"
# input: "input" (default: string)

message: str = input("Message: ")
key: int = int(input("Key: "))

# print(type(message))
# print(type(key))

# 'str' -> STRING (words)
# 'int' -> INTEGER (whole numbers)
ALPHABET_SIZE=26
ciphertext = ""

for character in message:
    if character >= "A" and character <="Z":
        shifted = ord(character) + key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE 
        ciphertext += chr(shifted)
    else:
        ciphertext += character
print(ciphertext)

plain_text=""

for character in ciphertext:
    if character >= "A" and character <="Z":
        shifted = ord(character) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE 
        plain_text += chr(shifted)
    else:
        plain_text += character
print(ciphertext)


# message = "UPDATE"

# "U" -> "X"
# "P" -> "S"
# "D" -> "G"
# "A" -> "D"
# "T" -> "W"
# "E" -> "H"

# "" -> "" + "X" -> "X"
# "X" -> "X" + "S" -> "XS"
# "XSG"
# "XSGD"
