
from config import CHARACTERS
import base64
import math

characters = CHARACTERS

data = input("DATA: ")
coder_input = input("CODER: ")

# CODER VALIDATION
if not coder_input.isdigit() or not 1 <= int(coder_input) <= 10:
    print("ERROR: INVALID CODER")
    exit()

coder = int(coder_input)

# BASE64 DECODE
try:
    decoded = base64.b64decode(data, validate=True).decode()
except Exception:
    print("ERROR: INVALID BASE64")
    exit()

numbers = decoded.split(",")
result = ""

# INTEGER ROOT
def integer_root(value, degree):
    low, high = 0, value

    while low <= high:
        mid = (low + high) // 2
        power = mid ** degree

        if power == value:
            return mid
        elif power < value:
            low = mid + 1
        else:
            high = mid - 1

    return None

# DECRYPT
try:
    for number in numbers:
        value = int(number.strip())

        r1 = integer_root(value, coder)

        if r1 is None:
            print("ERROR: INVALID ROOT")
            exit()

        if r1 % coder != 0:
            print("ERROR: INVALID CHARACTER")
            exit()

        position = r1 // coder

        if not 0 <= position < len(characters):
            print("ERROR: INVALID CHARACTER")
            exit()

        result += characters[position]

except ValueError:
    print("ERROR: INVALID DATA")
    exit()

print("DECODED:", result)

