
def unesi_korisnika():
        ime = input("Ime: ")
        prezime= input("Prezime: ")
        god= int(input("God: "))
        korisnik = [ime, prezime,god]
        svi_korisnici.append(korisnik)

def ispisi_korisnike():
    print(svi_korisnici)

svi_korisnici = []
while True:
    a= int(input("1-unos korisnika\n2-ispis\n3-izlaz"))
    if a == 1:
        unesi_korisnika()
    elif a==2:
        ispisi_korisnike()
    else:
        break