import time
import datetime
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

@app.route('/api/historia', methods=['GET'])
def pobierz_historie():
    try:
        if os.path.exists("baza_wynikow.txt"):
            with open("baza_wynikow.txt", "r", encoding="utf-8") as plik:
                linie = plik.readlines()
                ostatnie = "".join(linie[-15:])
                return jsonify({"historia": ostatnie})
        return jsonify({"historia": "Brak historii."})
    except Exception:
        return jsonify({"historia": "Błąd odczytu bazy."})

def zapisz_do_bazy(podsumowanie, total):
    data_wpisu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("baza_wynikow.txt", "a", encoding="utf-8") as plik:
        plik.write(f"\n--- WPIS: {data_wpisu} ---\n")
        for linia in podsumowanie:
            plik.write(f"{linia}\n")
        plik.write(f"LACZNA EMISJA: {total} kg CO2\n")
    print(f"[INFO] Dane zapisane: {total} kg CO2")

if __name__ == "__main__":
    
    app.run(port=5000, debug=False)
