def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def inverse(a, m):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    return None

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("GCD:", gcd(a, b))

a = int(input("Enter Number: "))
m = int(input("Enter Modulus: "))

print("Modular Inverse:", inverse(a, m))
