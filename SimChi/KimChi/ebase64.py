import base64

code = input("data: ")

try:
    decoded = base64.b64decode(code, validate=True)

    if base64.b64encode(decoded).decode() == code:
        print("ALREADY BASE64:", code)
    else:
        encoded = base64.b64encode(code.encode()).decode()
        print("ENCODED:", encoded)

except Exception:
    encoded = base64.b64encode(code.encode()).decode()
    print("ENCODED:", encoded)
