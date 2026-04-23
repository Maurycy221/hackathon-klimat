import time
import datetime
import threading
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')


@app.route('/api/zapisz', methods=['POST'])
def zapisz_ze_strony():
    dane = request.json
    wynik = dane.get('wynik', 0)
    urzadzenia = dane.get('urzadzenia', ["Wpis ze strony WWW"])
    zapisz_do_bazy(urzadzenia, wynik)
    return jsonify({"status": "sukces"})

def uruchom_serwer():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR) 
    app.run(port=5000, debug=False, use_reloader=False)


threading.Thread(target=uruchom_serwer, daemon=True).start()

#

def zapisz_do_bazy(podsumowanie, total):
    data_wpisu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("baza_wynikow.txt", "a", encoding="utf-8") as plik:
        plik.write(f"\n--- WPIS: {data_wpisu} ---\n")
        for linia in podsumowanie:
            plik.write(f"{linia}\n")
        plik.write(f"LACZNA EMISJA: {total} kg CO2\n")
    print(f"\n[INFO] Wyniki zostały zapisane do baza_wynikow.txt")

def eco_kalkulator():
    # Twój styl wizualny z terminala
    print("========================================")
    print("   ECO-KALKULATOR EMISJI CO2 v1.0")
    print("========================================")
    print("LINK DO STRONY: http://127.0.0.1:5000")
    print("Ten program obliczy Twoją emisję CO2.\n")

    urzadzenia = {
        "Komputer / Laptop": 0.1,
        "Telewizor LED": 0.15,
        "Konsola do gier": 0.2,
        "Ładowarka telefonu": 0.01,
        "Oświetlenie pokoju": 0.06
    }

    suma_co2 = 0
    podsumowanie = []

    for sprzet, moc in urzadzenia.items():
        try:
            print(f"--- {sprzet} ---")
            godziny = float(input(f"Ile godzin dziennie używasz tego sprzętu? "))
            kwh = moc * godziny
            emisja = round(kwh * 0.7, 3)
            suma_co2 += emisja
            podsumowanie.append(f"{sprzet}: {emisja} kg CO2")
            print(f"Wynik: {emisja} kg CO2 dziennie.\n")
        except ValueError:
            print("BŁŁĄD: Wpisz liczbę!\n")
            continue

    
    print("========================================")
    print("           RAPORT EKOLOGICZNY")
    print("========================================")
    time.sleep(1)

    for linia in podsumowanie:
        print(f"* {linia}")

    total = round(suma_co2, 2)
    print(f"\nŁĄCZNA DZIENNA EMISJA: {total} kg CO2")
    zapisz_do_bazy(podsumowanie, total)

    print("----------------------------------------")
    if total > 1.5:
        print("PORADA: Pamiętaj o wyłączaniu urządzeń!")
    else:
        print("BRAWO! Twoje nawyki są ekologiczne.")
    print("========================================\n")

if __name__ == "__main__":
    eco_kalkulator()
