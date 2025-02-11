#Werner ist doof
# Importiert das datetime-Modul aus der datetime-Bibliothek
from datetime import datetime

name =["andi"]

# Definiert eine Funktion, um ein Datum vom Benutzer zu erhalten
def get_date_from_user():
    # Fordert den Benutzer auf, ein Datum im Format TT.MM.JJJJ einzugeben
    date_str = input("Bitte geben Sie ein Datum im Format TT.MM.JJJJ ein: ")
    try:
        # Versucht, die Eingabe in ein datetime-Objekt zu konvertieren
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        # Gibt das eingegebene Datum im gleichen Format aus
        print(f"Das eingegebene Datum ist: {date_obj.strftime('%d.%m.%Y')}")
    except ValueError:
        # Gibt eine Fehlermeldung aus, wenn die Eingabe nicht konvertiert werden kann
        print("Fehlerhafte Eingabe. Bitte geben Sie ein gültiges Datum im Format TT.MM.JJJJ ein.")

# Führt die Funktion aus, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    get_date_from_user()

