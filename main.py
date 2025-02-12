from datetime import datetime

def get_date_from_user():
    date_str = input("Bitte geben Sie ein Datum im Format TT.MM.JJJJ ein: ").strip()
    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")  # Konvertiert die bereinigte Eingabe in ein datetime-Objekt
        print(f"Das eingegebene Datum ist: {date_obj.strftime('%d.%m.%Y')}")
    except ValueError:
        print("Fehlerhafte Eingabe. Bitte geben Sie ein gültiges Datum im Format TT.MM.JJJJ ein.")

if __name__ == "__main__":
    get_date_from_user()

