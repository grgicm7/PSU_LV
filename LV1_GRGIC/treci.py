lista = []
suma = 0
while True:
    try:
        x = input("Unesite broj. Ako zelite prekinuti petlju upisite rijec Done: ")

        if (x == 'Done'):
            break;
    
        lista.append(int(x))
        suma += int(x)
    except:
        print("Unjeli ste tip podatka koji nije broj")  


print("Korisnik je unio", len(lista), "broejva")
print("Minimalna vrijednost u listi je", min(lista))
print("Srednja vrijednost brojeva je", (suma / len(lista)))
print("Maksimalna vrijednost u listi je", max(lista))
lista.sort()

print("Sortirana lista: ")
for y in lista:
    print(int(y), end=" ")