from math import gcd

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a musi byt nesudelitelne s 26-kou.")
    res = ""
    for ch in text:
        if ch.isalpha():
            a0 = 'A' if ch.isupper() else 'a'
            x = ord(ch) - ord(a0)
            res += chr((a*x + b) % 26 + ord(a0))
        else:
            res += ch
    return res

def mod_inverse(a, m):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    raise ValueError("Neexistuje modularna inverzia.")

def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    res = ""
    for ch in text:
        if ch.isalpha():
            a0 = 'A' if ch.isupper() else 'a'
            y = ord(ch) - ord(a0)
            res += chr((a_inv*(y - b)) % 26 + ord(a0))
        else:
            res += ch
    return res

if __name__ == "__main__":
    print("zadaj text na zasifrovanie")
    plaintext = input()
    print("zadaj parametry a a b")
    a = int(input())
    b = int(input())
    print(affine_encrypt(plaintext, a, b))
    print(affine_decrypt(affine_encrypt(plaintext, a, b), a, b))