# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on
# ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa
# on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne
# ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

# > tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät
#   toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# > tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# > kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään
#   kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle
# kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi
# kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan
# kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta
# tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random
import time

class KilpaAuto:

    def __init__(self, rekisteritunnus, huippunopeus, t_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = t_nopeus
        self.kuljettu_matka = kuljettu_matka

     # Lisää tai vähentää nopeutta annetulla muutoksella kunnes kohdataan min(0) tai max(huippunopeus) nopeus:
    def kiihdytä(self, nopeuden_muutos):
        if nopeuden_muutos < 0:
            toistot = nopeuden_muutos * -1
        else:
            toistot = nopeuden_muutos
        for i in range(toistot):
            if self.tamanhetkinen_nopeus < self.huippunopeus and nopeuden_muutos >= 0:
                self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + 1
            elif nopeuden_muutos < 0 and self.tamanhetkinen_nopeus > 0:
                self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus - 1

    def kulje(self, tunnit):
        matkan_kasvu = self.tamanhetkinen_nopeus * tunnit
        self.kuljettu_matka = self.kuljettu_matka + matkan_kasvu

class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.kilpailun_nimi = nimi
        self.kilpailun_pituus = pituus
        self.kilpailuun_osallistujat = osallistujat

    def tunti_kuluu(self):
        for i in kilpa_autot:
            i.kiihdytä(random.randint(-10, 15))
            #print(f"Kilpa-auton {i.rekisteritunnus} tämänhetkinen nopeus on {i.tamanhetkinen_nopeus} km/h!")

        for i in kilpa_autot:
            i.kulje(1)
            #print(f"Kilpa-auto {i.rekisteritunnus} on kulkenut {i.kuljettu_matka} kilometriä!")

    def tulosta_tilanne(self):
        numero = 1
        for i in self.kilpailuun_osallistujat:
            print(f"---------------------------------------------------------------------------------------------------------\n"
                  f"Osallistuja nro {numero}:\n"
                  f"Tunnus: {i.rekisteritunnus} | Huippunopeus: {i.huippunopeus} km/h | Viimeisin nopeus: "
                  f"{i.tamanhetkinen_nopeus} km/h | Kuljettu matka: {i.kuljettu_matka} km")
            numero += 1
        print(f"---------------------------------------------------------------------------------------------------------")
        numero += 1

    def kilpailu_ohi(self):
        maalissa = 0
        for i in self.kilpailuun_osallistujat:
            if i.kuljettu_matka >= self.kilpailun_pituus:
                maalissa += 1
        if maalissa >= 1:
            arvo = True
        elif maalissa == 0:
            arvo = False
        return arvo

# Luodaan kilpa-autot:
luotu = 0
numero = 0
kilpa_autot = []
while luotu < 10:
    numero = numero + 1
    auto = KilpaAuto(str(f"ABC-{numero}"), random.randint(100,200))
    kilpa_autot.append(auto)
    luotu = luotu + 1

# Luodaan kilpailu:
uusi_kilpailu = Kilpailu("Suuri romuralli", 8000, kilpa_autot)
kilpailu_ohi = False
tunnit = 0
# Kilpailun aloitus:
print(f"'{uusi_kilpailu.kilpailun_nimi}' alkaa!")
print()
time.sleep(0.5)
while kilpailu_ohi == False:
    uusi_kilpailu.tunti_kuluu()
    tunnit = tunnit + 1
    uusi_kilpailu.kilpailu_ohi()
    if tunnit % 10 == 0:
        print()
        print(f"Tunteja on kulunut {tunnit}. Kilpailun tilanne tällä hetkellä: ")
        print()
        uusi_kilpailu.tulosta_tilanne()
    kilpailu_ohi = uusi_kilpailu.kilpailu_ohi()
    time.sleep(0.1)
# Kilpailu looppi loppu
print()
# Selvitetään, mikä autoista saavutti tavoitellun matkapituuden:
print("Kilpailu on päättynyt!")
for i in uusi_kilpailu.kilpailuun_osallistujat:
    if i.kuljettu_matka >= uusi_kilpailu.kilpailun_pituus:
        voittaja = i.rekisteritunnus
print()
print(f"Kilpailun voittaja on kilpa-auto tunnuksella {voittaja}!")
print()
# Tulostetaan kaikkien kilpa-autojen viimeisimmät tiedot:
print("Tässä on vielä kaikkien osallistujien tilanne: ")
uusi_kilpailu.tulosta_tilanne()