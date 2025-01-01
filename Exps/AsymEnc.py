from sympy import mod_inverse

def key_generation():

    p = 7  
    q = 11
    n = p * q
    g = 5
    a = 3
    A = pow(g, a, n)

    private_key = (a,n)
    public_key = (g, A, n)

    return private_key, public_key

def encrypt(public_key, m):
    g, A, n = public_key
    k = 6
    
    c1 = pow(g, k, n)  
    c2 = (m * pow(A, k, n)) % n  

    return c1, c2

def decrypt(private_key, c1, c2):

    a,n = private_key

    S = pow(c1, a, n) 
    S_inverse = mod_inverse(S, n)  

    m = (c2 * S_inverse) % n  

    return m

private_key, public_key = key_generation()

print("Private Key:", private_key)
print("Public Key (g, A, n):", public_key)

orginal_message = "BlockChain"
print("Original Message:", orginal_message)
marr= []
for i in orginal_message:
    marr.append(ord(i)-ord('A'))
# m = 13
print("Original Message in number format:", marr)

res= []
for m in marr:
    c1, c2 = encrypt(public_key, m)
    res.append((c1, c2))

print("Cipher Text: ", res)

resdesc = []
for c1, c2 in res:
    decrypted_message = decrypt(private_key, c1, c2)
    resdesc.append(decrypted_message)

print("Decrypted Message in number format:", resdesc)

print("Decrypted Message: ", end='')
for i in resdesc:
    i= i+ord('A')
    print(chr(i), end='')
