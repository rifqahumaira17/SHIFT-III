import os
import time

from termcolor import colored, cprint

kata = "Happy Eid"
langkah = " " * 20 + kata + " " * 20

durasi = 20

for i in range(len(langkah) - 20 ,-1, -1):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    teks = langkah[i:i + 20]
    cprint(teks, "red")
    
    waktu_durasi = durasi/(len(langkah) - 20 + 1)
    time.sleep(waktu_durasi)
