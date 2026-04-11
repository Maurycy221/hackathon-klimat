print("Witaj w Eco-Kalkulatorze!")

def oblicz_co2(kwh):
    return kwh * 0.7

energia = float(input("Ile kWh zużyło Twoje urządzenie? "))
wynik = oblicz_co2(energia)

print(f"To urządzenie wyemitowało {wynik} kg CO2.")
