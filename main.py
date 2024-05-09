from datetime import datetime, timedelta

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=5000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=8000)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas["szobaszam"] == szobaszam and foglalas["datum"] == datum:
                return "A szoba már foglalt ekkor."
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append({"szobaszam": szobaszam, "datum": datum})
                return f"A foglalás megerősítve a(z) {datum}-i dátumra {szoba.ar} Ft-ért."
        return "Nincs ilyen szoba."

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas["szobaszam"] == szobaszam and foglalas["datum"] == datum:
                self.foglalasok.remove(foglalas)
                return "A foglalás sikeresen törölve."
        return "Nincs ilyen foglalás."

    def listaz(self):
        if self.foglalasok:
            return "\n".join([f"Szoba: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}" for foglalas in self.foglalasok])
        else:
            return "Nincs foglalás."

def create_sample_hotel():
    hotel = Szalloda("Példa Szálloda")
    hotel.add_szoba(EgyagyasSzoba("101"))
    hotel.add_szoba(EgyagyasSzoba("102"))
    hotel.add_szoba(KetagyasSzoba("201"))
    hotel.add_szoba(KetagyasSzoba("202"))
    hotel.add_szoba(KetagyasSzoba("203"))
    return hotel

def main():
    hotel = create_sample_hotel()

    for _ in range(5):
        tomorrow = datetime.now() + timedelta(days=1)
        datum = tomorrow.strftime('%Y-%m-%d')
        hotel.foglal("101", datum)
        hotel.foglal("201", datum)
        tomorrow += timedelta(days=1)

    print("Üdvözöljük a Példa Szállodában!")
    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        choice = input("Választott művelet: ")

        if choice == "1":
            szobaszam = input("Adja meg a foglalandó szoba számát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            print(hotel.foglal(szobaszam, datum))
        elif choice == "2":
            szobaszam = input("Adja meg a lemondandó foglalás szoba számát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            print(hotel.lemondas(szobaszam, datum))
        elif choice == "3":
            print(hotel.listaz())
        elif choice == "4":
            print("Köszönjük, hogy minket választott! Viszlát!")
            break
        else:
            print("Érvénytelen választás. Kérem, válasszon újra.")

if __name__ == "__main__":
    main()
