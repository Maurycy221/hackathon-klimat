import time

def eco_kalkulator():
    print("========================================")
    print("   ECO-KALKULATOR EMISJI CO2 v1.0")
    print("========================================")
    print("Ten program obliczy, ile kilogramów CO2 emitujesz")
    print("używając codziennie sprzętów domowych.\n")

    # Dane: Moc urządzeń w kilowatach (kW)
    urzadzenia = {
        "Komputer / Laptop": 0.1,
        "Telewizor LED": 0.15,
        "Konsola do gier": 0.2,
        "Ładowarka telefonu": 0.01,
        "Oświetlenie pokoju": 0.06
    }

    suma_co2 = 0
    podsumowanie = []

    # Główna pętla obliczeniowa
    for sprzet, moc in urzadzenia.items():
        try:
            print(f"--- {sprzet} ---")
            godziny = float(input(f"Ile godzin dziennie używasz tego sprzętu? "))
            
            # Obliczenia: kWh = Moc * Czas
            kwh = moc * godziny
            # Średni przelicznik w Polsce: ok. 0.7 kg CO2 na 1 kWh
            emisja = round(kwh * 0.7, 3)
            
            suma_co2 += emisja
            podsumowanie.append(f"{sprzet}: {emisja} kg CO2")
            print(f"Wynik: {emisja} kg CO2 dziennie.\n")
            
        except ValueError:
            print("BŁĄD: Wpisz poprawną liczbę! (użyj kropki zamiast przecinka)\n")
            continue

    # Wyświetlanie raportu końcowego
    print("========================================")
    print("          RAPORT EKOLOGICZNY")
    print("========================================")
    time.sleep(1) # Mały efekt oczekiwania na wynik
    
    for linia in podsumowanie:
        print(f" * {linia}")
    
    total = round(suma_co2, 2)
    print(f"\nŁĄCZNA DZIENNA EMISJA: {total} kg CO2")
    
    # Porada ekologiczna
    print("----------------------------------------")
    if total > 1.5:
        print("PORADA: Twoja emisja jest wysoka. Pamiętaj, aby")
        print("wyłączać listwę zasilającą na noc!")
    else:
        print("BRAWO! Twoje nawyki są bardzo ekologiczne.")
    print("========================================\n")

if __name__ == "__main__":
    eco_kalkulator()
