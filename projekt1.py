ukoly = []


def hlavni_menu():
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print ("2. Zobrazit úkoly ")
    print ("3. Odstranit úkol")
    print("4. Konec programu")

def pridat_ukol():
    nazev_ukolu = input ("vložte název úkolu: ")
    popis_ukolu = input ("vložte popis úkolu: ")
    ukoly.append(nazev_ukolu)
    print ("přidali jste úkol", nazev_ukolu)

hlavni_menu()
akce_uzivatele = input ("Vyberte číslo od 1 do 4")

if akce_uzivatele == "1":
    pridat_ukol()



else:
    print ("Ajaj, neplatná volba, zkuste prosím jinou:)")
    hlavni_menu()