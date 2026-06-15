def caesar_encrypt(text, k):
    """
    Zašifruje text pomocou Caesarovej šifry.

    Každé písmeno sa posunie o k pozícií v abecede.
    Nealfabetické znaky zostávajú nezmenené.

    Args:
        text (str): Vstupný text na zašifrovanie.
        k (int): Posun (kľúč) šifry.

    Returns:
        str: Zašifrovaný text.
    """
    result = ""
    for ch in text:
        if ch.isalpha():
            a = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(a) + k) % 26 + ord(a))
        else:
            result += ch
    return result

def caesar_decrypt(text, k):
    """
        Rozšifruje text zašifrovaný Caesarovou šifrou.

        Dešifrovanie je opačný proces k šifrovaniu (negatívny posun).

        Args:
            text (str): Zašifrovaný text.
            k (int): Kľúč použitý pri šifrovaní.

        Returns:
            str: Pôvodný (dešifrovaný) text.
        """
    result = caesar_encrypt(text, -k)
    return result

if __name__ == "__main__":
    """
    Testovacia časť programu. 
    """
    print("zadaj text na zasifrovanie")
    plaintext = input()
    print("zadaj kluc")
    key = int(input())
    result = caesar_encrypt(plaintext, key)
    print(result)
    print(caesar_decrypt(caesar_encrypt(plaintext, key), key))