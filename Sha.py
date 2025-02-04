import hashlib

# Input data
data = "Hello, World!"

# Compute SHA-256 hash
hash_object = hashlib.sha256(data.encode())
hash_hex = hash_object.hexdigest()

print("SHA-256 Hash:", hash_hex)
