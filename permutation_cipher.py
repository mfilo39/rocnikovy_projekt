def perm_encrypt(plaintext, perm):
    """
        Zašifruje text pomocou permutačnej šifry.

        Text sa rozdelí na bloky veľkosti permutácie a v každom bloku sa
        znaky preusporiadajú podľa zadanej permutácie.

        Args:
            plaintext (str): Vstupný text na zašifrovanie.
            perm (list): Permutácia indexov (napr. [2,0,1]).

        Returns:
            str: Zašifrovaný text.
        """
    n = len(perm)
    while len(plaintext) % n != 0:
        plaintext += ' '

    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = plaintext[i:i+n]
        encrypted_block = ''.join(block[perm[j]] for j in range(n))
        ciphertext += encrypted_block
    return ciphertext

def inverse_perm(perm):
    """
        Vytvorí inverznú permutáciu.

        Inverzná permutácia slúži na spätné rozšifrovanie.

        Args:
            perm (list): Pôvodná permutácia.

        Returns:
            list: Inverzná permutácia.
        """
    inv = [0]*len(perm)
    for i, p in enumerate(perm):
        inv[p] = i
    return inv

def perm_decrypt(ciphertext, perm):
    """
        Rozšifruje text pomocou permutačnej šifry.

        Používa inverznú permutáciu na obnovenie pôvodného poradia znakov.

        Args:
            ciphertext (str): Zašifrovaný text.
            perm (list): Permutácia použitá pri šifrovaní.

        Returns:
            str: Pôvodný text (s prípadnými doplnenými medzerami).
        """
    inv = inverse_perm(perm)
    n = len(perm)
    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i+n]
        decrypted_block = ''.join(block[inv[j]] for j in range(n))
        plaintext += decrypted_block
    return plaintext

if __name__ == "__main__":
    print(perm_encrypt("HELLOWORLD", [2,0,1]))
    print(perm_decrypt(perm_encrypt("HELLOWORLD", [2,0,1]), [2,0,1]))
