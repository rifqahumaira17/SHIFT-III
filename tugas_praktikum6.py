def koordinat():
    print("Masukkan koordinat 3 titik(x,y)!")
koordinat()

titik = []
for i in range(3):
    x = int(input(f"Koordinat titik x untuk titik ke-{i+1} : "))
    y = int(input(f"Koordinat titik y untuk titik ke-{i+1} : "))
    titik.append([x,y])

def sisi (a,b) :
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**1/2

a = sisi(titik[0], titik[1])
b = sisi(titik[1], titik[2])
c = sisi(titik[2], titik[0])

if a==b or b==c or c==a :
    print(f"Terbentuk segitiga sama kaki dengan dua sisi yang sama panjang.")
else :
    print(f"Tidak terbentuk segitiga sama kaki.")