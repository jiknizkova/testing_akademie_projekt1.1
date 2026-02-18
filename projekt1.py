ukoly = []

def hlavni_menu():
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print ("2. Zobrazit úkoly ")
    print ("3. Odstranit úkol")
    print("4. Konec programu")
    print()

def pridat_ukol():
    while True:
        nazev_ukolu = input ("vložte název úkolu: ")
        if nazev_ukolu == "":
            pokyn = input("Jejda, nezdali jste nic. Pokud se raději chccete vrátit do menu, stisknete kláves 'm' a enter."
            "Stiskem jakékoliv jiné klávesy se vrátíte zpět k možnosti zadat název úkolu. ")
            if pokyn == "m":
                break
        else:
            popis_ukolu = input ("vložte popis úkolu: ")
            if popis_ukolu == "":
                pokyn = input("Jejda, nezdali jste nic. Pokud se raději chccete vrátit do menu, stisknete kláves 'm' a enter. "
                "Stiskem jakékoliv jiné klávesy se vrátíte zpět k možnosti zadání názvu a popisu úkolu. ")
                if pokyn == "m":
                    break
            else:
                ukoly.append(f"{nazev_ukolu} - {popis_ukolu}")
                print ("přidali jste úkol", nazev_ukolu)
                print()
                break

def zobrazit_ukoly():
    if len(ukoly)>0:
        for polozka in ukoly:
            print(f"{ukoly.index(polozka) + 1}. úkol: {polozka}")
        print()
    else:
        print("Ještě nemáte zadané žádné úkoly.")
        print()

def odstranit_ukol():
    while True:
        zobrazit_ukoly()
        cislo_ukolu = input("Zadejte číslo úkolu, který chcete smazat: ")
        cislo_ukolu = int(cislo_ukolu)
        skutecne_poradi = cislo_ukolu - 1
        pocet_ukolu = len(ukoly)
        if cislo_ukolu > pocet_ukolu:
            print ("Ups, tenhle úkol v seznamu nemáme. Zkuste to znovu")
            rozhodnuti = input("Pokud se raději chcete vrátit zpět do menu, stisknete klávesu 'm' a enter. ")
            if rozhodnuti == "m":
                break
        else:
            ukoly.pop(skutecne_poradi)
            print("Úkol č. {cislo_ukolu} byl smazán.")
            print()
            break
        


while True:
    hlavni_menu()
    akce_uzivatele = input ("Vyberte číslo od 1 do 4 ")
    print()

    if akce_uzivatele == "1":
        pridat_ukol()

    elif akce_uzivatele == "2":
        zobrazit_ukoly()
       
    elif akce_uzivatele == "3":
         odstranit_ukol()

    elif akce_uzivatele == "4":
        print("Konec programu")
        break

    else:
        print("Ajaj, zadali jste neplatnou volbu, zkuste to znovu.")