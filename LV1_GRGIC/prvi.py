broj_sati = input("Unesite broj radnih sati: ")
zarada = input("Unesite placu po satu: ")

#rezultat = int(broj_sati) * int(zarada)

def total_euro(x, y):
    return x * y

print("Radnik je zaradio", total_euro(int(broj_sati), int(zarada)), "eura")