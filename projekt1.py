print("Správce úkolů - Hlavní menu")
print("1. Přidat nový úkol")
print ("2. Zobrazit úkoly ")
print ("3. Odstranit úkol")
print("4. Konec programu")

ukoly = []

akce_uzivatele = input ("Vyberte číslo od 1 do 4")

if akce_uzivatele == "1":
    print("ahoj")
    nazev_ukolu = input ("vložte název úkolu")
    def pridat_ukol(nazev_ukolu):
        return ukoly.append(nazev_ukolu)
    print (ukoly)
else:
    print ("konec")