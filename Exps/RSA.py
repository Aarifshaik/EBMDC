import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    phi0 = phi
    while e > 0:
        temp1, temp2 = phi // e, phi % e
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        phi, e = e, temp2
        x2, x1 = x1, x
        d, y1 = y1, y
    if phi == 1:
        return d + phi0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_candidate(length):
    p = random.randrange(2**(length - 1), 2**length)
    if p % 2 == 0:
        p += 1
    return p

def generate_prime_number(length=8):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keys(keysize=8):
    p = generate_prime_number(keysize)
    q = generate_prime_number(keysize)
    while p == q:
        q = generate_prime_number(keysize)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

public_key, private_key = generate_keys(keysize=8)
print("Public key:", public_key)
print("Private key:", private_key)

message = "Hello Aarif"
print("\nOriginal message:", message)

ciphertext = encrypt(public_key, message)
print("\nEncrypted message:", ciphertext)

decrypted_message = decrypt(private_key, ciphertext)
print("\nDecrypted message:", decrypted_message)
