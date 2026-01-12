def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isalpha():
            a = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(a) + k) % 26 + ord(a))
        else:
            result += ch
    return result

def caesar_decrypt(text, k):
    result = caesar_encrypt(text, -k)
    return result

if __name__ == "__main__":
    print("zadaj text na zasifrovanie")
    plaintext = input()
    print("zadaj kluc")
    key = int(input())
    result = caesar_encrypt(plaintext, key)
    print(result)
    print(caesar_decrypt(caesar_encrypt(plaintext, key), key))