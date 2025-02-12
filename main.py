from datetime import datetime

name =["andi"]

def get_date_from_user():
    date_str = input("Bitte geben Sie ein Datum im Format TT.MM.JJJJ ein: ")
    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y") # Versucht, die Eingabe in ein datetime-Objekt zu konvertieren
        print(f"Das eingegebene Datum ist: {date_obj.strftime('%d.%m.%Y')}") # Ausgabe
    except ValueError:
        print("Fehlerhafte Eingabe. Bitte geben Sie ein gültiges Datum im Format TT.MM.JJJJ ein.")   # Gibt eine Fehlermeldung aus, wenn die Eingabe nicht konvertiert werden kann

if __name__ == "__main__":
    get_date_from_user()

