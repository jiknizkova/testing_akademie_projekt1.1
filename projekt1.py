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
        nazev_ukolu = input ("Zadejte název úkolu: ")
        if nazev_ukolu == "":
            pokyn = input("Jejda, nezdali jste nic. Pokud se raději chccete vrátit do menu, stisknete kláves 'm' a enter."
            "Stiskem jakékoliv jiné klávesy se vrátíte zpět k možnosti zadat název úkolu. ")
            if pokyn == "m":
                break
        else:
            popis_ukolu = input ("Zadejte popis úkolu: ")
            if popis_ukolu == "":
                pokyn = input("Jejda, nezdali jste nic. Pokud se raději chccete vrátit do menu, stisknete kláves 'm' a enter. "
                "Stiskem jakékoliv jiné klávesy se vrátíte zpět k možnosti zadání názvu a popisu úkolu. ")
                if pokyn == "m":
                    break
            else:
                ukoly.append({"nazev": nazev_ukolu, "popis": popis_ukolu})
                print (f"Úkol '{nazev_ukolu}' byl přidán")
                print()
                break

def zobrazit_ukoly():
    if len(ukoly)>0:
        for polozka in ukoly:
            print(f"{ukoly.index(polozka) + 1}. úkol: {polozka['nazev']} - {polozka['popis']}")
        print()
    else:
        print("Ještě nemáte zadané žádné úkoly.")
        print()

def odstranit_ukol():
    while True:
        zobrazit_ukoly()
        if ukoly == []:
            break
        else:
            
                try:
                    cislo_ukolu = input("Zadejte číslo úkolu, který chcete smazat: ")
                    cislo_ukolu = int(cislo_ukolu)
                    skutecne_poradi = cislo_ukolu - 1
                    pocet_ukolu = len(ukoly)

                    if cislo_ukolu <= pocet_ukolu and cislo_ukolu > 0:
                        smazany_ukol = ukoly.pop(skutecne_poradi)
                        print(f"Úkol {smazany_ukol['nazev']} byl smazán.")
                        print()
                        break
            
                    else:
                        print ("Ups, tenhle úkol v seznamu nemáme. Zkuste to znovu")
                        rozhodnuti = input("Pokud se raději chcete vrátit zpět do menu, stisknete klávesu 'm' a enter."
                        "Stiskem jakékoliv jiné klávesy se dostanete zppět k výběru úkolů. ")
                        if rozhodnuti == "m":
                            break
                    
                except ValueError:
                    print ("Jej, zadali jste neplatnou hodnotu, zkuste to znovu")

               


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