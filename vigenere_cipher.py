def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    j = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('a')
            a = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(a) + shift) % 26 + ord(a))
            j += 1
        else:
            result += ch
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    j = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('a')
            a = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(a) - shift) % 26 + ord(a))
            j += 1
        else:
            result += ch
    return result

if __name__ == "__main__":
    print("zadaj text na zasifrovanie")
    plaintext = input()
    print("zadaj kluc")
    key = input()
    result = vigenere_encrypt(plaintext, key)
    print(result)
    result = vigenere_decrypt(vigenere_encrypt(plaintext, key), key)
    print(result)