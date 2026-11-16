from PIL import Image

img = Image.open("cover.png").convert("RGB")
pixels = img.load()

msg = input("Enter Secret Message: ") + "####"
binary = ''.join(format(ord(c), '08b') for c in msg)

i = 0
for y in range(img.height):
    for x in range(img.width):
        p = list(pixels[x, y])
        for n in range(3):
            if i < len(binary):
                p[n] = (p[n] & 254) | int(binary[i])
                i += 1
        pixels[x, y] = tuple(p)
        if i == len(binary):
            break
    if i == len(binary):
        break

if i < len(binary):
    raise ValueError("Image is too small for this message.")

img.save("stego.png")
print("Message Hidden Successfully!")

img = Image.open("stego.png").convert("RGB")
binary = ""

for p in img.getdata():
    for v in p:
        binary += str(v & 1)

msg = ""
for i in range(0, len(binary), 8):
    msg += chr(int(binary[i:i+8], 2))
    if msg.endswith("####"):
        break

print("Hidden Message:", msg[:-4])
