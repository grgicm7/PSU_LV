dat = open("C:\\Users\\Marija\\Documents\\FERIT\\3.SEMESTAR\\PRIMIJENJENO STROJNO UCENJE\\LV1_GRGIC\\song.txt")
rjecnik={}
broj_jed=0

for line in dat:
    line=line.rsplit()
    for rijec in line:
        if rijec in rjecnik:
            rjecnik[rijec] += 1
else:
    rjecnik[rijec] = 1

for rijeci in rjecnik:
    if rjecnik[rijeci]==1:
        broj_jed+=1

print(rjecnik)
print(broj_jed)