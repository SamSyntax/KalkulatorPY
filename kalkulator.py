import sys
import os

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        print("Nie można dzielić przez zero.")
        sys.exit(1)

wynikowy_plik = os.path.join(os.path.dirname(os.path.abspath(__file__)), './tmp/wynik.txt')

print("Prosty Kalkulator")

while True:
    try:
        wejscie = input("Wprowadź działanie (np. 5 + 3) lub wpisz 'quit' aby wyjść: ")
        
        if wejscie.lower() == 'quit':
            print("Zakończono program.")
            break

        elementy = wejscie.split()
        liczba1 = float(elementy[0])
        operacja = elementy[1]
        liczba2 = float(elementy[2])

        if operacja == '+':
            wynik = dodawanie(liczba1, liczba2)
        elif operacja == '-':
            wynik = odejmowanie(liczba1, liczba2)
        elif operacja == '*':
            wynik = mnozenie(liczba1, liczba2)
        elif operacja == '/':
            wynik = dzielenie(liczba1, liczba2)
        else:
            print("Nieobsługiwana operacja. Obsługiwane operacje: +, -, *, /")
            continue

        with open(wynikowy_plik, 'w') as plik_wynikowy:
            plik_wynikowy.write(str(wynik))

        print(f"Wynik {operacja} dla {liczba1} i {liczba2} zapisano do {wynikowy_plik}")

    except (ValueError, IndexError):
        print("Błędne dane. Wprowadź poprawne działanie.")
    except ZeroDivisionError:
        print("Nie można dzielić przez zero.")
