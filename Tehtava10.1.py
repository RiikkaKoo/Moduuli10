# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen
# numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi
# on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun
# h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin
# monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat
# hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen
# siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, tamanhetkinen_kerros = 0):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.tamanhetkinen_kerros = tamanhetkinen_kerros

    def kerros_ylöspäin(self):
        self.tamanhetkinen_kerros = self.tamanhetkinen_kerros + 1

    def kerros_alaspäin(self):
        self.tamanhetkinen_kerros = self.tamanhetkinen_kerros - 1

    def siirry_kerrokseen_x(self, kerros):
        print()
        while self.tamanhetkinen_kerros != kerros:
            if self.tamanhetkinen_kerros < kerros:
                self.kerros_ylöspäin()
                print(f"Bling! Kerros {self.tamanhetkinen_kerros}")
            elif self.tamanhetkinen_kerros > kerros:
                self.kerros_alaspäin()
                print(f"Bling! Kerros {self.tamanhetkinen_kerros}")
        else:
            print()
            print(f"Hissi on kerroksessa {self.tamanhetkinen_kerros}.")

# Pääohjelma hissillä liikkuminen
hissi1 = Hissi(0,9)
hissi1.siirry_kerrokseen_x(5)
hissi1.siirry_kerrokseen_x(5)
hissi1.siirry_kerrokseen_x(hissi1.ylin_kerros)
hissi1.siirry_kerrokseen_x(3)
hissi1.siirry_kerrokseen_x(hissi1.alin_kerros)