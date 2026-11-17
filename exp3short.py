
from PIL import Image

img = Image.open("cover.png").convert("RGB")
pixels = list(img.getdata())

msg = input("Enter Secret Message: ") + "####"
bits = ''.join(format(ord(c), '08b') for c in msg)

new_pixels = []
i = 0

for p in pixels:
    p = list(p)
    for j in range(3):
        if i < len(bits):
            p[j] = (p[j] & 254) | int(bits[i])
            i += 1
    new_pixels.append(tuple(p))

img.putdata(new_pixels)
img.save("stego.png")
print("Message Hidden!")

# Extract message
bits = ''.join(str(v & 1) for p in new_pixels for v in p)
msg = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
print("Hidden Message:", msg.split("####")[0])
