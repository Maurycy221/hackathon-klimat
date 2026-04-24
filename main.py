import datetime
import os
import logging
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')


@app.route('/api/zapisz', methods=['POST'])
def zapisz_ze_strony():
    try:
        dane = request.json
        wynik = dane.get('wynik', 0)
        urzadzenia = dane.get('urzadzenia', ["Wpis ze strony WWW"])
        
        
        data_wpisu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("baza_wynikow.txt", "a", encoding="utf-8") as plik:
            plik.write(f"\n--- WPIS: {data_wpisu} ---\n")
            for linia in urzadzenia:
                plik.write(f"{linia}\n")
            plik.write(f"LACZNA EMISJA: {wynik} kg CO2\n")
        
        print(f"[INFO] Nowy zapis w bazie: {wynik} kg CO2 ({data_wpisu})")
        return jsonify({"status": "sukces"})
    except Exception as e:
        print(f"[BŁĄD] Nie udało się zapisać: {e}")
        return jsonify({"status": "error"}), 500


@app.route('/api/historia', methods=['GET'])
def pobierz_historie():
    try:
        if os.path.exists("baza_wynikow.txt"):
            with open("baza_wynikow.txt", "r", encoding="utf-8") as plik:
                linie = plik.readlines()
                
                ostatnie = "".join(linie[-20:])
                return jsonify({"historia": ostatnie})
        return jsonify({"historia": "Brak historii. Wykonaj pierwsze obliczenie!"})
    except Exception:
        return jsonify({"historia": "Błąd odczytu bazy danych."})


if __name__ == "__main__":
    print("========================================")
    print("SERWER AKTYWNY: http://127.0.0.1:5000")
    print("========================================")
    app.run(port=5000, debug=False)
    