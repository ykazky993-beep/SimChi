from config import CHARACTERS
# CHARACTER MAPPING
characters = CHARACTERS

data = input("DATA: ")
coder_input = input("CODER: ")

# CODER VALIDATION
if not coder_input.isdigit() or int(coder_input) == 0:
    print("ERROR: INVALID CODER")
    exit()

coder = int(coder_input)

numbers = data.split(",")
result = ""

# DECRYPT
try:
    for number in numbers:
        value = int(number.strip())

        if value % coder != 0:
            print("ERROR: INVALID CODER")
            exit()

        position = value // coder

        if not 0 <= position < len(characters):
            print("ERROR: INVALID CHARACTER")
            exit()

        result += characters[position]

except ValueError:
    print("ERROR: INVALID DATA")
    exit()

print("DECODED:", result)

