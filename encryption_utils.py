from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Updated key: 32 bytes for AES-256
KEY = b"thisisaverysecurekey1234567890!!"  # Ensure exactly 32 bytes

def encrypt(plaintext):
    """
    Encrypts plaintext using AES encryption.
    :param plaintext: Text to encrypt.
    :return: Base64-encoded encrypted text.
    """
    cipher = AES.new(KEY, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()

def decrypt(ciphertext):
    """
    Decrypts a base64-encoded ciphertext using AES.
    :param ciphertext: Base64-encoded text to decrypt.
    :return: Decrypted plaintext.
    """
    raw = base64.b64decode(ciphertext)
    iv, encrypted_data = raw[:16], raw[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_data), AES.block_size).decode()
