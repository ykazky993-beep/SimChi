
from config import CHARACTERS

data = input("DATA: ")
coder_input = input("POWER (1-10): ")

if not coder_input.isdigit() or not 1 <= int(coder_input) <= 10:
    print("ERROR: INVALID POWER")
    exit()

coder = int(coder_input)
result = ""

try:
    numbers = data.split(",")

    for number in numbers:
        value = int(number.strip())

        if value < 0:
            raise ValueError

        position = round(value ** (1 / coder))

        # Validate exact power
        if position ** coder != value:
            print("ERROR: INVALID DATA")
            exit()

        if not 0 <= position < len(CHARACTERS):
            print("ERROR: INVALID CHARACTER")
            exit()

        result += CHARACTERS[position]

except ValueError:
    print("ERROR: INVALID DATA")
    exit()

print("DECODED:", result)

