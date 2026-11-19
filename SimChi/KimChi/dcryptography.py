
from cryptography.fernet import Fernet

key = b"2_UUdenho04oorFI6FH3bLAAx4E5mleb3suNA0Vv1hk="

cipher = Fernet(key)

token = b"gAAAAABq_nJ2YR2eggAWEqVT7cG7vbXWt-J_4Iqad3YANyZrypMdBr-3W1orBbL5nUvuXUBnQ4FVl6MCpkxTOAXJj0AvW6BEXA=="

# Decryption
plaintext = cipher.decrypt(token)

print(plaintext.decode())

