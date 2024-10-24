# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

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
                print(f"> Bling! < Kerros {self.tamanhetkinen_kerros}")
            elif self.tamanhetkinen_kerros > kerros:
                self.kerros_alaspäin()
                print(f"> Bling! < Kerros {self.tamanhetkinen_kerros}")
        else:
            print()
            print(f"Hissi on kerroksessa {self.tamanhetkinen_kerros}.")

class Talo:
    def __init__(self, ylin_kerros, alin_kerros, hissejä):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.hissit = []

        for h in range(hissejä):
            hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissi, kerros):
        self.hissit[hissi].siirry_kerrokseen_x(kerros)

    def palohälytys(self):
        print()
        print("BrIIIINg! BRiiiNG! Palohälytys!")
        for h in self.hissit:
            h.tamanhetkinen_kerros = self.alin_kerros

talo1 = Talo(7,0,3)
print("> Ovet sulkeutuvat <")
talo1.aja_hissiä(3-1,6)
print()

hissi = int(input(f"Mitä hissiä haluat käyttöö? {len(talo1.hissit)} kpl: "))
kerros = int(input(f"Mihin kerrokseen haluat mennä? {talo1.alin_kerros}-{talo1.ylin_kerros}: "))
print("> Ovet sulkeutuvat <")
talo1.aja_hissiä(hissi-1,kerros)

print()
print("Missä kerroksissa hissit ovat?")
numero = 1
for h in talo1.hissit:
    print(f"Hissi{numero} on kerroksessa {h.tamanhetkinen_kerros}.")
    numero += 1

talo1.palohälytys()

print()
print("Missä kerroksissa hissit ovat?")
numero = 1
for h in talo1.hissit:
    print(f"Hissi{numero} on kerroksessa {h.tamanhetkinen_kerros}.")
    numero += 1