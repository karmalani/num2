# das ist das perfekte programm

# import numpy für Betragsfunktion
import numpy as np

# Variablen für das Heronverfahren definieren
a = 2
tol = 1e-8


# definiere eine funktion für das Heronverfahren
def heron(start_wert):
    # Definiere das Ziel des Heronverfahrens
    goal = a ** .5
    # Definiere eine Zählvariable und setze x_k für k=0
    counter = 0
    x_k = start_wert

    # Wiederhole das Heronverfahren, bis die Iterierte konvergiert (|x_k - sqrt(a)|< Toleranz)
    while np.abs(x_k - goal) >= tol:
        # iteriere gemäß des Heronverfahrens
        x_k = 0.5 * (x_k + a / x_k)
        # Erhöhe den Zähler
        counter += 1
        # Falls das Verfahren nicht in weniger als 20 Schritten konvergiert, Schleife abbrechen und das zurückgeben
        if counter >= 20:
            print("Das Heronverfahren konvergiert nicht in weniger als 20 Schritten")
            return
    # Falls das Verfahren in 20 Schritten konvergiert, das Ausgeben
    print("Das Heronverfahren konvergiert in weniger als 20 Schritten")


# Werte wurden experimentell bestimmt
print("Für den Startwert 0.000026246 gilt:")
heron(0.000026246)
print()
print("Für den Startwert 0.000026247 gilt:")
heron(0.000026247)
print()
print("Für den Startwert 76201.428827105 gilt:")
heron(76201.428827105)
print()
print("Für den Startwert 76201.428827106 gilt:")
heron(76201.428827106)
print("\n\n")
print(
    "Damit ist das Intervall, in dem Das Heronverfahren in weniger als 20 Schritten konvergiert ca. [0.000026247,76201.428827105].")
