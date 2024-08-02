
# RSA Algorithm with small numbers

# Key Generation
p = 3
q = 11
n = p * q
phi_n = (p - 1) * (q - 1)
e = 3
d = 7  # d is the modular inverse of e modulo phi_n

# Public and Private Keys
public_key = (e, n)
private_key = (d, n)

# Encryption
def encrypt(message, public_key):
    e, n = public_key
    ciphertext = pow(message, e, n)
    return ciphertext

# Decryption
def decrypt(ciphertext, private_key):
    d, n = private_key
    message = pow(ciphertext, d, n)
    return message

# Example
original_message = 7
ciphertext = encrypt(original_message, public_key)
decrypted_message = decrypt(ciphertext, private_key)

# Output in Markdown format
print(f"**Original Message:** {original_message}")
print(f"**Encrypted Message:** {ciphertext}")
print(f"**Decrypted Message:** {decrypted_message}")

