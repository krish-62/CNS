def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch)-base+key)%26+base)
        else:
            result += ch
    return result

text = input("Enter Text: ")
key = int(input("Enter Key: "))

cipher = encrypt(text, key)
print("Encrypted:", cipher)
print("Decrypted:", encrypt(cipher, -key))
