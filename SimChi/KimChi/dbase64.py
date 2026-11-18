import base64

data = input("data: ")

try:
    decoded = base64.b64decode(data, validate=True)
    print(decoded.decode("ascii"))

except Exception as e:
    print("ERROR:", e)
