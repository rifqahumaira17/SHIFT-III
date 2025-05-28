def menu():
    print("menu")
    print("1. tabel pencarian modulo n")
    print("2. mencari nilai sigma x")
    print("3. mencari nilai n!")
    print("4. total dan rata-rata data")
    print("5. keluar")
menu()    

def perkalian_modulo():
    n= int(input("masukkan nilai n (1-10): "))
    while n<=0 or n>10 :
        n = int(input("masukkan nilai n (1-10): "))
    print("tabel perkalian modulo")    
    for i in range(n):
        for j in range(n):
            print((i*j) % n, end="")
        print()   

def sigma():
    bawah = int(input("batas bawah: "))
    atas = int(input("batas atas: "))
    while atas < bawah:
        print("batas atas harus >= batas bawah.")
        atas = int(input("batas atas: "))
        total = 0
    for x in range(bawah, atas +1):
        total += x
        print("Σ x = ",total)     

def faktorial():
    n = int(input("n = "))
    while n<0 :
        n = int(input("masukkan n>= 0: "))
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    print(f"{n}! =",hasil)   

def rata_rata():
    n = int(input("banyak data: "))       
    while n <= 0:
        n = int(input("masukkan lagi (n > 0): "))
    data = []
    for i in range(n):
        angka = float(input(f"data ke-{i+1}: "))
        data.append(angka)
    total = sum(data)    
    rata = total/n
    print("total =",total)  
    print("Rata-rata =",rata) 

    print("-------------")
    print("|no. |nilai|")
    print("-------------")
    print(f"| 1  | {data[0]} |" )
    print(f"| 2  | {data[1]} |")
    print("-------------")
    
while True:
    pilihan = input("pilih menu (1-5): ")

    if pilihan == "1":
        perkalian_modulo()
    elif pilihan == "2":
        sigma()
    elif pilihan == "3":
        faktorial()
    elif pilihan == "4":
        rata_rata()
    elif pilihan == "5":
        print("program selesai.")
        break
    else:
        print("silahkan pilih angka 1-5")   
