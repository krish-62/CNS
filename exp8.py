def inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d

p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))

n = p * q
phi = (p-1) * (q-1)

d = inverse(e, phi)

if d is None:
    print("Invalid e. Choose another value.")
    exit()

print("Public Key:", (e, n))
print("Private Key:", (d, n))

text = input("Enter Plain Text: ")

cipher = []
for ch in text:
    cipher.append(pow(ord(ch), e, n))

print("Encrypted:", cipher)

decrypted = ""
for c in cipher:
    decrypted += chr(pow(c, d, n))

print("Decrypted:", decrypted)
