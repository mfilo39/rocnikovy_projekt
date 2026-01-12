import random

def vernam_generate_key(plaintext_length):
    key = ''
    for _ in range(plaintext_length):
        key += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return key

def vernam_encrypt(plaintext, key):
    ciphertext = ''
    for p, k in zip(plaintext, key):
        ciphertext += chr(ord(p) ^ ord(k))
    return ciphertext

def vernam_decrypt(ciphertext, key):
    decrypted_text = ''
    for c, k in zip(ciphertext, key):
        decrypted_text += chr(ord(c) ^ ord(k))
    return decrypted_text


if __name__ == "__main__":
    print("zadaj text na zasifrovanie")
    plaintext = input()
    key = vernam_generate_key(len(plaintext))
    print(vernam_encrypt(plaintext, key))
    print(vernam_decrypt(vernam_encrypt(plaintext, key), key))
