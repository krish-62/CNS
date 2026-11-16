from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890abcdef'
text = input("Enter Text: ")

cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(text.encode(), 16))

print("Encrypted:", encrypted.hex())

cipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(cipher.decrypt(encrypted), 16)

print("Decrypted:", decrypted.decode())
