print("Správce úkolů - Hlavní menu")
print("1. Přidat nový úkol")
print ("2. Zobrazit úkoly ")
print ("3. Odstranit úkol")
print("4. Konec programu")

akce_uzivatele = input ("Vyberte číslo od 1 do 4")

if akce_uzivatele == "1":
   print("ahoj")
   def pridat_ukol():
        nazev_ukolu = input ("Název úkolu:")
        popis_ukolu = input ("Popis úkolu?")
        print("Úkol", nazev_ukolu, "byl pridan")
        return 
   print (pridat_ukol)
else:
    print ("konec")