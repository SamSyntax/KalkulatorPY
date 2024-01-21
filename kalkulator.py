def dodawanie(a,b):
    return a+b
    
def odejmowanie(a,b):
    return a-b

def mnożenie(a,b):
    return a*b

def dzielenie(a,b):
    if b != 0:
        return a/b
    else:
        print("Nie dzielimy przez 0!")
        
    
print("Kalkulator w python")
        
while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończ")
    
    dzialanie = input("Wprowadź numer działania: ")
    
    if dzialanie == '5':
        print("Zakończono")
        break
    
    if dzialanie in ('1', '2', '3', '4'):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
        
        if dzialanie == '1':
            print("Wynik: ", dodawanie(liczba1, liczba2))
        elif dzialanie == '2':
            print("Wynik: ", odejmowanie(liczba1, liczba2))
        elif dzialanie == '3':
            print("Wynik: ", mnożenie(liczba1, liczba2))
        elif dzialanie == '4':
            print("Wynik: ", dzielenie(liczba1, liczba2))
    else:
        print("Nie ma takiego działania")
        