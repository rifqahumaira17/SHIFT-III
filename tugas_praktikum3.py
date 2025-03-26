#input jumlah baris (n), minimal n=4
n = int(input("Masukkan jumlah baris : "))

#operasi perhitungan jumlah baris dan kata BOOM
if n <= 3 :
    print("Jumlah baris minimal 4")
else :
    total_BOOM = 0

#perulangan bersarang   for p in range (n) :
    for p in range (n) :
        for q in range (n) :
            if p == q :
                if p == q == n // 2 and n % 2 == 1 :
                    print ("HORE", end= "  ")
                else :
                    print(" 1 ", end= "   ")
            elif p + q == n - 1 :
                print(" 2 ", end= "   ")
            else :
                print("BOOM", end= "  ")
             
                total_BOOM += 1
        print( )

print(f"Total BOOm yang muncul sebanyak = {total_BOOM} ")

