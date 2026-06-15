def vigenere_encrypt(text, key):
    """
        Zašifruje text pomocou Vigenèrovej šifry.

        Každé písmeno sa posúva o hodnotu určenú zodpovedajúcim písmenom kľúča.

        Args:
            text (str): Vstupný text na zašifrovanie.
            key (str): Kľúč (slovo) používaný na šifrovanie.

        Returns:
            str: Zašifrovaný text.
        """
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
    """
        Rozšifruje text zašifrovaný Vigenèrovou šifrou.

        Používa opačný posun ako pri šifrovaní.

        Args:
            text (str): Zašifrovaný text.
            key (str): Kľúč použitý pri šifrovaní.

        Returns:
            str: Pôvodný text.
        """
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