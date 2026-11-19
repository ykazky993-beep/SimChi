
from cryptography.fernet import Fernet

# Generate secret key
key = Fernet.generate_key()

# Initialize Fernet
cipher = Fernet(key)

# Plaintext
text = b"Hello World"

# Encryption
token = cipher.encrypt(text)

print("KEY:", key.decode())
print("TOKEN:", token.decode())

