def GenKey(plainText):
    key = 0
    for i in plainText:
        key += ord(i)
    return key

def Encrypt1(plainText, key):
    cipherText = ""
    for i in plainText:
        cipherText += chr(ord(i) ^ key)
    return cipherText

def Decrypt1(cipherText, key):
    plainText = ""
    for i in cipherText:
        plainText += chr(ord(i) ^ key)
    return plainText


def Encrypt2(plainText, key):
    cipherText = ""
    j=1
    for i in plainText:
        value = ord(i) ^ key * j
        if value > 1114111:
            value = value % 1114112 
        # print(value , end=' ')    
        cipherText += chr(value)
        j+=1
    return cipherText

def Decrypt2(cipherText, key):
    plainText = ""
    j=1
    for i in cipherText:
        value = ord(i) ^ key * j
        if value > 1114111:
            value = value % 1114112  
        # print(value , end=' ')
        plainText += chr(value)
        j+=1
    return plainText

plainText = "Emerging BlockChain adsfsdvhkgbfuvhdfvilzfjvnzsuiervfhnizslhbfiolgjvkpesougdbfuawhjvbaeisuofdhijiworfh"
key=GenKey(plainText)
cipherText = Encrypt1(plainText, key)
DecryptText = Decrypt1(cipherText, key)


cipherText1 = Encrypt2(plainText, key)
DecryptText1 = Decrypt2(cipherText1, key)

print("Key: ", key)
print("\n")
print("Normal XOR Cipher Text: ", cipherText)
print("Normal XOR Decrypt Text: ", DecryptText)

print("\n")

print("Custom XOR Logic Cipher Text: ", cipherText1)
print("Custom XOR Logic Decrypt Text: ", DecryptText1)
