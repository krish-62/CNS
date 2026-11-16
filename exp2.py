import math

def encrypt(text, key):
    text = text.replace(" ", "").upper()
    rows = math.ceil(len(text)/key)
    text += 'X' * (rows*key-len(text))

    cipher = ""
    for col in range(key):
        for row in range(rows):
            cipher += text[row*key+col]
    return cipher

def decrypt(text, key):
    rows = len(text)//key
    result = ""
    for row in range(rows):
        for col in range(key):
            result += text[col*rows+row]
    return result.rstrip('X')

text = input("Enter Text: ")
key = int(input("Enter Key: "))

cipher = encrypt(text, key)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, key))
