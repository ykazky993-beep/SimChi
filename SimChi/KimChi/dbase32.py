import base64

data = input("data: ")
decoded = base64.b32decode(data)

print(decoded, "\n")
print(decoded.decode("utf-8", errors="replace"))
