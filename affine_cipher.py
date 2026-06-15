from math import gcd

def affine_encrypt(text, a, b):
    """
        Zašifruje text pomocou afinnnej šifry.

        Afinná šifra používa transformačnú funkciu:

            E(x) = (a * x + b) mod 26

        kde:
            - x je číselná reprezentácia písmena,
            - a a b sú kľúčové parametre.

        Parameter a musí byť nesúdeliteľný s číslom 26,
        aby bolo možné text neskôr dešifrovať.

        Args:
            text (str):
                Text určený na šifrovanie.

            a (int):
                Multiplikatívna časť kľúča.

            b (int):
                Aditívna časť kľúča.

        Returns:
            str:
                Zašifrovaný text.

        Raises:
            ValueError:
                Ak parameter a nie je nesúdeliteľný s 26.
        """
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
    """
        Nájde modulárnu inverziu čísla a modulo m.

        Modulárna inverzia je číslo x také, že:

            (a * x) mod m = 1

        Funkcia používa jednoduché prehľadávanie
        všetkých možných hodnôt od 1 po m - 1.

        Args:
            a (int):
                Číslo, ktorého inverziu hľadáme.

            m (int):
                Modul.

        Returns:
            int:
                Modulárna inverzia čísla a.

        Raises:
            ValueError:
                Ak modulárna inverzia neexistuje.
        """
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    raise ValueError("Neexistuje modularna inverzia.")

def affine_decrypt(text, a, b):
    """
        Dešifruje text zašifrovaný afinnou šifrou.

        Na dešifrovanie sa používa vzťah:

            D(y) = a⁻¹ * (y - b) mod 26

        kde:
            - y je zašifrované písmeno,
            - a⁻¹ je modulárna inverzia parametra a.

        Args:
            text (str):
                Šifrovaný text.

            a (int):
                Multiplikatívna časť kľúča.

            b (int):
                Aditívna časť kľúča.

        Returns:
            str:
                Dešifrovaný text.

        Raises:
            ValueError:
                Ak neexistuje modulárna inverzia parametra a.
        """
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
    """
        Testovacia časť programu.

        Načíta od používateľa text a parametre afinnnej šifry,
        následne vykoná šifrovanie aj dešifrovanie a vypíše výsledky.
        """
    print("zadaj text na zasifrovanie")
    plaintext = input()
    print("zadaj parametry a a b")
    a = int(input())
    b = int(input())
    print(affine_encrypt(plaintext, a, b))
    print(affine_decrypt(affine_encrypt(plaintext, a, b), a, b))