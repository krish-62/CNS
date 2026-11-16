from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = b'1234567890abcdef'
iv = get_random_bytes(16)
text = input("Enter Text: ")

cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(text.encode(), 16))

print("Encrypted:", encrypted.hex())

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(encrypted), 16)

print("Decrypted:", decrypted.decode())
