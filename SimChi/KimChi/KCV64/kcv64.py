
from config import CHARACTERS

text = input("CHAR. Input: ")
coder_input = input("CODE. Power: ")

if not coder_input.isdigit() or not 1 <= int(coder_input) <= 10:
    print("WARNING: 1-10 is recomended, but you can ignore this.")

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

