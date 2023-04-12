import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

#Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
petnajvecih = mtcars.sort_values(by=['mpg'])
print("5 auta s najvecom potrosnjom: \n",petnajvecih.tail(5))

#Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
osamcyl = mtcars.cyl == 8
osamcyl = mtcars.sort_values(by=['mpg'])
print("tri auta s 8 cilindara s najmanjom potrosnjom: \n",osamcyl.head(3))

#Kolika je srednja potrošnja automobila sa 6 cilindara?
sestcyl = mtcars.cyl == 6
sestcyl = mtcars.mpg
print("srednja potrosnja auta sa 6 cilindara: \n",sestcyl.mean())

#Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
srpotrosnja = mtcars[(mtcars.wt >= 2) & (mtcars.wt <= 2.2) & (mtcars.cyl == 4)]
print("srednja potrosnja auta s 4 cilindra mase izmedu 2000 i 2200 lbs: \n",srpotrosnja['mpg'].mean())

#Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
a_mjenjac = mtcars[mtcars.am == 0]
r_mjenjac = mtcars[mtcars.am == 1]
print(len(a_mjenjac))
print(len(r_mjenjac))

#Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
amsto = mtcars[(mtcars.am == 0) & (mtcars.hp > 100)]
print("automobili s automatskim mjenjacem i snagom preko 100 konja\n",amsto['hp'].count())

#Kolika je masa svakog automobila u kilogramima?
print("masa svakog automobila u kilogramima\n",mtcars.wt * 1000 * 0.45359237)






