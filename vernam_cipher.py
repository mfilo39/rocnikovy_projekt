import random

def vernam_generate_key(plaintext_length):
    """
        Vygeneruje náhodný kľúč pre Vernamovu šifru.

        Kľúč má rovnakú dĺžku ako vstupný text a skladá sa z veľkých písmen A-Z.

        Args:
            plaintext_length (int): Dĺžka vstupného textu.

        Returns:
            str: Náhodne vygenerovaný kľúč.
        """
    key = ''
    for _ in range(plaintext_length):
        key += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return key

def vernam_encrypt(plaintext, key):
    """
        Zašifruje text pomocou Vernamovej šifry (XOR operácia).

        Každý znak textu sa XOR-uje s príslušným znakom kľúča.

        Args:
            plaintext (str): Vstupný text.
            key (str): Tajný kľúč rovnakej dĺžky ako text.

        Returns:
            str: Zašifrovaný text (môže obsahovať netlačiteľné znaky).
        """
    ciphertext = ''
    for p, k in zip(plaintext, key):
        ciphertext += chr(ord(p) ^ ord(k))
    return ciphertext

def vernam_decrypt(ciphertext, key):
    """
        Rozšifruje text pomocou Vernamovej šifry.

        Dešifrovanie je identické so šifrovaním (XOR je inverzná operácia).

        Args:
            ciphertext (str): Zašifrovaný text.
            key (str): Rovnaký kľúč použitý pri šifrovaní.

        Returns:
            str: Pôvodný text.
        """
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
