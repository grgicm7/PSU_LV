naziv = input("Unesite ime datoteke: ")
# path = "C:\Users\student\Desktop\LV1"+naziv
dat = open(naziv)
brojac = 0
total = 0
avr = 0

for line in dat:
    if line.startswith("X-DSPAM-Confidence: "):
        line_split = line.split(" ")
        pouzdanost = float(line_split[1])
        total += pouzdanost
        brojac += 1
    if brojac > 0:
        avr = total / brojac
        print("Average X-DSPAM-Confidence: ", avr)
else:
    print("Nema linija oblika 'X-DSPAM-Confidence:' u datoteci.")