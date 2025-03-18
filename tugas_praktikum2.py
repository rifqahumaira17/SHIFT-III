while True :
 #menginput nilai pertama dan nilai kedua
 n = float(input("inputkan nilai n : "))
 p = float(input("inputkan nilai p : "))

 #macam macam operasi beserta rumus
 #penjumlahan = n + p
 #pengurangan = n - p
 #perkalian = n*p
 #pembagian = n/p

#operasi kalkulator
 operasi = input("operasi yang dipilih : ")

 if operasi == "penjumlahan" :
  operasi = n + p
 
 elif operasi == "pengurangan" :
  operasi = n - p

 elif operasi == "perkalian" :
  operasi = n*p

 elif operasi == "pembagian" :
  operasi = n/p

 else :
  print("operasi tidak tersedia")
 print(f"hasil operasi adalah : {operasi} ")

#perintah pengulangan atau berhenti
 perintah = input("lanjut atau berhenti : ")
 if perintah == "berhenti":
    break
 elif perintah == "lanjut":
    pass