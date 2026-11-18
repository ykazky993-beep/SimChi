
from config import CHARACTERS

text = input("CHAR. Input: ")
coder_input = input("CODE. Power (1-10): ")

if not coder_input.isdigit() or not 1 <= int(coder_input) <= 10:
    print("ERROR: POWER MUST BE 1-10")
    exit()

coder = int(coder_input)
result = []

for char in text:
    if char not in CHARACTERS:
        print(f"ERROR: UNSUPPORTED CHARACTER: {char}")
        exit()

    position = CHARACTERS.index(char)
    value = position ** coder

    print(f"CHAR. {char} | index-{position} | power-{coder} | result-{value}")

    result.append(str(value))

code = ",".join(result)

print("CODE:", code)

