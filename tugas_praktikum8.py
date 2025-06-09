with open("data_praktikan.txt", "w") as file:
    file.write("2410431001, Yaya, 98,86,87\n")
    file.write("2410431002, Feng, 90,60,81\n")
    file.write("2410431003, Ying, 94,86,76\n")
    file.write("2410431004, Caca, 91,84,77\n")
    file.write("2410431005, Nana, 80,95,92\n")
    file.write("2410431006, Poka, 100,90,95\n")
    file.write("2410431007, Teil, 99,90,60\n")
    file.write("2410431008, Glen, 100,100,90\n")
    file.write("2410431009, Occa, 88,92,70\n")
    file.write("2410431010, Wudi, 70,85,80\n")
    
file_lama = open("data_praktikan.txt", "r")
data = {}
for baris in file_lama:
    nim, nama, pretest, postest, tugas = baris.strip(). split(",")
    data[nim] = [nama.strip(), float(pretest), float(postest),float(tugas)]
file_lama.close()

file_baru = open("data_nilai_akhir.txt", "w")
total_nilai = 0
nilai_akhir = {}

for nim in data: 
    nama, pretest, postest, tugas = data[nim]
    total = (35/100) * pretest + (35/100) * postest + (30/100) * tugas
    nilai_akhir[nim] = total
    total_nilai += total
    file_baru.write(f"{nim}, {nama}, {pretest}, {postest}, {tugas}, {round(total,2)}\n")

file_baru.close()

rata_rata = total_nilai / len(data)
tertinggi = max(nilai_akhir, key = nilai_akhir.get)
terendah = min(nilai_akhir, key = nilai_akhir.get)
bawah_rata_rata = sum(1 for x in nilai_akhir.values() if x < rata_rata)

print("Rata-rata nilai akhir: ", round(rata_rata,2))
print("Nilai tertinggi: " ,nilai_akhir[tertinggi], "-", data[tertinggi][0])
print("Nilai terendah: " ,nilai_akhir[terendah], "-", data[terendah][0])
print("Jumlah praktikan yang di bawah rata-rata:", bawah_rata_rata)
