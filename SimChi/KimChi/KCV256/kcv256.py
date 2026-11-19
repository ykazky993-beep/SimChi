
import base64
from config import KCV256CHAR

# CHARACTER MAPPING
characters = KCV256CHAR

# INPUT
text = input("CHAR. Input: ")
coder = int(input("CODE. Power (1-10): "))

if not 1 <= coder <= 10:
    print("WARNING: Power recomended between 1 and 10, you can ignore this.")

# ENCRYPTION
results = []
encrypted = ""



for char in text:

    # INPUT MAPPING
    if char.isalpha() and char.isascii():
        pos = ord(char.lower()) - ord("a") + 1
        mapped = characters[(pos - 1) % len(characters)]
        index = characters.index(mapped) + 1

    elif char.isdigit():
        index = int(char)
        mapped = char

    else:
        print(f"CHAR. {char} | skipped")
        continue

    # EXPONENTIATION
    R1 = index ** coder

    # MULTIPLICATION
    rest = R1 * coder

    results.append(str(rest))

    # RESULT MAPPING
    rest1 = ""

    for digit in str(rest):
        digit_index = int(digit)

        if digit_index == 0:
            raise ValueError("Digit 0 has no mapping")

        rest1 += characters[
            (digit_index - 1) % len(characters)
        ]

    encrypted += rest1

    # DEBUG
    print(
        f"CHAR. {char} | index-{index} "
        f"| mapped-{mapped!r} "
        f"| power-{coder} "
        f"| result-{rest}"
    )

# RESULT
print("CODE:", ",".join(results))
print("CHARACTER:", encrypted)

# BASE32
b32 = base64.b32encode(
    encrypted.encode("utf-8")
).decode("ascii")

# BASE64
b64 = base64.b64encode(
    b32.encode("ascii")
).decode("ascii")

# OUTPUT
print("BASE32:", b32)
print("ENCRYPTED:", b64)

