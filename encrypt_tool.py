#!/usr/bin/env python3
import base64
import codecs
from cryptography.fernet import Fernet

def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        return f"Base64 Decryption Failed: {e}"

def hex_encrypt(text):
    return text.encode().hex()

def hex_decrypt(text):
    try:
        return bytes.fromhex(text).decode()
    except Exception as e:
        return f"Hex Decryption Failed: {e}"

def rot13_encrypt_decrypt(text):
    return codecs.encode(text, 'rot_13')

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def fernet_generate_key(password):
    padded = password.ljust(32)[:32]
    return base64.urlsafe_b64encode(padded.encode())

def fernet_encrypt(text, password):
    key = fernet_generate_key(password)
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

def fernet_decrypt(text, password):
    try:
        key = fernet_generate_key(password)
        f = Fernet(key)
        return f.decrypt(text.encode()).decode()
    except Exception as e:
        return f"Fernet Decryption Failed: {e}"

def main():
    print("=== Encryption / Decryption Tool ===")
    print("Run the setup script to use interactively.")

if __name__ == "__main__":
    main()
