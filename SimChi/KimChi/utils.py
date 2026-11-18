import base64
import binascii

def is_b64(data):
    try:
        base64.b64decode(data, validate=True)
        return True
    except (binascii.Error, ValueError):
        return False

def is_b32(data):
    try:
        base64.b32decode(data, casefold=False)
        return True
    except (binascii.Error, ValueError):
        return False
