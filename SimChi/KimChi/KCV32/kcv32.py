from config import CHARACTERS
import base64
import random

# CHARACTER MAPPING
characters = CHARACTERS

text = input("CHAR. Input: ")
text2 = input("CODE. code (enter for random): ")

# CODER
if text2 == "":
    coder = random.randint(1, 100)
    print("CODER:", coder)
else:
    if not text2.isdigit() or int(text2) == 0:
        print("MUST BE POSITIVE INTEGER")
        exit()

    coder = int(text2)

result = []

# ENCRYPT
for char in text:
    if char not in characters:
        print(f"ERROR: UNSUPPORTED CHARACTER: {char}")
        exit()

    position = characters.index(char)
    rest = position * coder

    print(
        f"CHAR. {char} "
        f"index-{position} "
        f"coder-{coder} "
        f"to rest-{rest}"
    )

    result.append(str(rest))

# JOIN
code = ",".join(result)

print("CODE:", code)

# BASE32
encoded = base64.b32encode(code.encode()).decode()

print("BASE32:", encoded)

