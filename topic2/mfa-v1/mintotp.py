import base64
import hmac
import struct
import time


def hotp(key, counter, digits=6, digest="sha1"):
    key = base64.b32decode(key.upper() + "=" * ((8 - len(key)) % 8))
    counter = struct.pack(">Q", counter)
    mac = hmac.new(key, counter, digest).digest()
    offset = mac[-1] & 0x0F
    binary = struct.unpack(">L", mac[offset : offset + 4])[0] & 0x7FFFFFFF
    return str(binary)[-digits:].zfill(digits)


def totp(key, time_step=30, digits=6, digest="sha1", t=None):
    return hotp(key, int((time.time() if t is None else t) / time_step), digits, digest)
