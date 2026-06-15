"""
Hlavný modul aplikácie pre klasické kryptografické šifry.

Program poskytuje:
- Caesarovu šifru
- Afinnú šifru
- Vernamovu šifru
- Vigenèrovu šifru
- Permutačnú šifru
- Základnú kryptoanalýzu (frekvenčná analýza, index náhodnosti)

"""

from math import gcd
from caesar_cipher import caesar_encrypt, caesar_decrypt
from affine_cipher import affine_encrypt, affine_decrypt
from vernam_cipher import vernam_encrypt, vernam_decrypt, vernam_generate_key
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from permutation_cipher import perm_encrypt, perm_decrypt

def safe_input(prompt, cast_func=str, condition=lambda x: True, error_msg="Neplatný vstup"):
    """
        Bezpečne načíta a overí používateľský vstup.

        Funkcia opakovane vyzýva používateľa na zadanie hodnoty,
        kým nie je úspešne skonvertovaná a neprejde validačnou podmienkou.

        Args:
            prompt (str): Text výzvy zobrazený používateľovi.
            cast_func (callable): Funkcia použitá na konverziu vstupu.
            condition (callable): Validačná funkcia vracajúca True pre platný vstup.
            error_msg (str): Chybové hlásenie pri neplatnom vstupe.

        Returns:
            Any: Overená a skonvertovaná hodnota.
        """
    while True:
        try:
            value = cast_func(input(prompt))
            if not condition(value):
                raise ValueError
            return value
        except:
            print(error_msg)

def choice_of_action():
    """
        Zobrazí menu operácií pre zvolenú šifru.

        Returns:
            int: Hodnota 1 (šifrovanie),
                2 (dešifrovanie) alebo
                3 (popis šifry).
        """
    return safe_input("Zvoľ si možnosť: 1 - šifrovanie, 2 - dešifrovanie, 3 - popis: ", int, lambda x: x in [1,2,3])

def load_description(name):
    """
        Načíta popis šifry zo súboru.

        Args:
            name (str): Názov súboru bez prípony.

        Returns:
            str: Obsah súboru alebo chybová správa.
        """
    print("\n---POPIS---")
    try:
        with open(f"descriptions/{name}.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Popis pre túto šifru neexistuje."

def char_frequency(text):
    """
        Vypočíta frekvenciu písmen v texte.

        Ignoruje nepísmenové znaky a nerozlišuje veľkosť písmen.

        Args:
            text (str): Vstupný text.

        Returns:
            dict[str, int]: Slovník frekvencií znakov.
        """
    freq = {}
    for ch in text:
        if ch.isalpha():
            ch = ch.upper()
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def index_of_coincidence(text, c):
    """
        Vypočíta index náhodnosti textu.

        Args:
            text (str): Analyzovaný text.
            c (int): Normalizačná konštanta.

        Returns:
            float: Hodnota indexu náhodnosti.
        """
    filtered = [ch for ch in text if ch.isalpha()]
    N = len(filtered)

    if N < 2:
        return 0

    freq = char_frequency(filtered)
    total = 0

    for ch in freq:
        total += freq[ch] * (freq[ch] - 1) / (N * (N - 1))

    return total * c


def caesar_bruteforce(text):
    """
        Vykoná útok hrubou silou na Caesarovu šifru.

        Args:
            text (str): Šifrovaný text.
        """
    print("\n---Caesar Bruteforce---")
    for shift in range(26):
        print(f"Shift {shift}: {caesar_decrypt(text, shift)}")

def is_permutation(key):
    """
        Overí platnosť permutačného kľúča.

        Args:
            key (list[int]): Permutačný kľúč.

        Returns:
            bool: True ak ide o platnú permutáciu.
        """
    for i in range(len(key)):
        if key[i] >= len(key) or key[i] < 0:
            return False
        if i > 0 and key[i] == key[i-1]:
            return False
    return True

class Cipher:
    """
        Reprezentuje jednu šifru v registri.

        Attributes:
            name (str): Názov šifry.
            file (str): Súbor s dokumentáciou.
            run (callable): Funkcia vykonávajúca operácie šifry.
        """
    def __init__(self, name, file, run_function):
        """
                Inicializuje objekt Cipher.

                Args:
                    name (str): Názov šifry.
                    file (str): Súbor s popisom.
                    run_function (callable): Obslužná funkcia šifry.
                """
        self.name = name
        self.file = file
        self.run = run_function

def run_caesar(cipher):
    """
        Obsluha Caesarovej šifry.

        Args:
            cipher (Cipher): Objekt šifry.

        Returns:
            tuple: (výsledok, identifikátor šifry)
        """
    action = choice_of_action()

    if action == 3:
        print(load_description(cipher.file))
        return None, "1"

    text = input("Zadaj text: ")
    shift = safe_input("Shift (0-25): ", int, lambda x: 0 <= x < 26)

    if action == 1:
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)

    return result, "1"


def run_affine(cipher):
    """
        Obsluha afinnnej šifry.

        Args:
            cipher (Cipher): Objekt šifry.

        Returns:
            tuple: (výsledok, identifikátor šifry)
        """
    action = choice_of_action()

    if action == 3:
        print(load_description(cipher.file))
        return None, "2"

    text = input("Zadaj text: ")

    a = safe_input("a: ", int)
    if gcd(a, 26) != 1:
        print("Chyba: 'a' musí byť nesúdeliteľné s 26!")
        return None, "2"

    b = safe_input("b: ", int)

    if action == 1:
        result = affine_encrypt(text, a, b)
    else:
        result = affine_decrypt(text, a, b)

    return result, "2"


def run_vernam(cipher):
    """
        Obsluha Vernamovej šifry.

        Args:
            cipher (Cipher): Objekt šifry.

        Returns:
            tuple: (výsledok, identifikátor šifry)
        """
    action = choice_of_action()

    if action == 3:
        print(load_description(cipher.file))
        return None, "3"

    text = input("Zadaj text: ")

    if action == 1:
        key = vernam_generate_key(len(text))
        print("Kľúč:", key)
        result = vernam_encrypt(text, key)
    else:
        key = input("Zadaj kľúč: ")
        if len(key) != len(text):
            print("Chyba: kľúč musí mať rovnakú dĺžku ako text!")
            return None, "3"
        result = vernam_decrypt(text, key)

    return result, "3"


def run_vigenere(cipher):
    """
        Obsluha Vigenèrovej šifry.

        Args:
            cipher (Cipher): Objekt šifry.

        Returns:
            tuple: (výsledok, identifikátor šifry)
        """
    action = choice_of_action()

    if action == 3:
        print(load_description(cipher.file))
        return None, "4"

    text = input("Zadaj text: ")
    key = input("Kľúč (len písmená): ")

    if not key.isalpha():
        print("Chyba: kľúč musí obsahovať len písmená!")
        return None, "4"

    if action == 1:
        result = vigenere_encrypt(text, key)
    else:
        result = vigenere_decrypt(text, key)

    return result, "4"


def run_permutation(cipher):
    """
        Obsluha permutačnej šifry.

        Args:
            cipher (Cipher): Objekt šifry.

        Returns:
            tuple: (výsledok, identifikátor šifry)
        """
    action = choice_of_action()

    if action == 3:
        print(load_description(cipher.file))
        return None, "5"

    text = input("Zadaj text: ")
    key_input = input("Zadaj permutáciu (napr. 210): ")

    try:
        key = [int(x) for x in key_input]
    except:
        print("Chyba: permutácia musí byť čísla!")
        return None, "5"

    if not is_permutation(key):
        print("Chyba: nie je platná permutácia!")
        return None, "5"

    if action == 1:
        result = perm_encrypt(text, key)
    else:
        result = perm_decrypt(text, key)

    return result, "5"

ciphers_registry = {
    "1": Cipher("Caesar", "caesar_cipher", run_caesar),
    "2": Cipher("Affine", "affine_cipher", run_affine),
    "3": Cipher("Vernam", "vernam_cipher", run_vernam),
    "4": Cipher("Vigenere", "vigenere_cipher", run_vigenere),
    "5": Cipher("Permutation", "permutation_cipher", run_permutation)
}

def main():
    """
        Hlavný vstupný bod programu.

        Zobrazuje menu, spracúva používateľské vstupy,
        spúšťa šifrovanie/dešifrovanie a kryptoanalýzu.
        """
    c = 26

    while True:
        print("\n===MENU===")
        for key in ciphers_registry:
            print(f"{key} - {ciphers_registry[key].name}")

        choice = input("Vyber šifru (alebo q pre koniec): ")

        if choice == "q":
            break

        cipher = ciphers_registry.get(choice)

        if not cipher:
            print("Neplatná voľba!")
            continue

        result, cipher_id = cipher.run(cipher)

        if result is None:
            continue

        print("Výsledok:", result)

        # Kryptoanalýza
        print("\n1 - kryptoanalýza")
        if cipher_id == "1":
            print("2 - bruteforce Caesar")
            print("3 - späť")
            sub = input("Voľba: ")

            if sub == "1":
                print(char_frequency(result))
                print("Index náhodnosti:", index_of_coincidence(result, c))

            elif sub == "2":
                caesar_bruteforce(result)

        else:
            print("2 - späť")
            sub = input("Voľba: ")

            if sub == "1":
                print(char_frequency(result))
                print("Index náhodnosti:", index_of_coincidence(result, c))


if __name__ == "__main__":
    main()

