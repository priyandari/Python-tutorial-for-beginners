import io
import csv
import urllib.request

def csv_import(url):
    url_open = urllib.request.urlopen(url)
    csvfile = csv.reader(io.StringIO(url_open.read().decode('utf-8')), delimiter=',')
    return csvfile

url = "https://raw.githubusercontent.com/priyandari/Python-tutorial-for-beginners/tutorial2021/nilaiKuliah.csv"

datafile = csv_import(url)
#Diperoleh data mentah sebagai berikut
data_nilaimhs =list(datafile)

#Konversi data nilai dari string menjadi float
for datamhs in data_nilaimhs:
    if datamhs[0] != 'NIM':
        datamhs[2] = float(datamhs[2])
        datamhs[3] = float(datamhs[3])
        datamhs[4] = float(datamhs[4])
        datamhs[5] = float(datamhs[5])

#Menampilkan masing-masing data nilai mahasiswa
for nilai in data_nilaimhs:
    print(nilai)

print("---"*12)

"""
Lanjutkan program untuk
1. Menambahkan nilaiakhir ke dalam variabel list data_nilaimhs.
   Gunakankan proses pengulangan dan fungsi append() untuk menambahkan kolom baru menyimpan nilai akhir.
   Adapun proses pengulangan bisa menggunakan contoh perintah di bawah ini.
    for datanilai in data_nilaimhs[:]:
        >>baris proses di sini<<
    Hati-hati, bahwa baris pertama list data_nilaimhs adalah header, bukan berisi data nilai mahasiswa. Tambahkan juga header NILAIAKHIR.
    Adapun rumus nilaiakhir sebagai berikut:
    nilaiakhir = bobotUK1*UK1 + bobotUK2*UK2 + bobotUK3*UK3 + bobotUK4*UK4
    dimana
    bobotUK1 = 0.2
    bobotUK2 = 0.2
    bobotUK3 = 0.3
    bobotUK4 = 0.3
    Cek dengan menampilkan hasilnya.

2. Hitunglah rata-rata nilai seluruh mahasiswa
   Gunakan iterasi berikut
    for datanilai in data_nilaimhs[1:]:
        >>baris proses di sini<<

3. Hitunglah rata-rata nilai kelas angkatan 2020
   Gunakan iterasi berikut
    for datanilai in data_nilaimhs[12:]:
        >>baris proses di sini<<

4. Tambahkan data Nilai A, B, C, D, atau E pada daftar data_nilaimhs  untuk seluruh mahasiswa dengan ketentuan
    A : 85 - 100
    B : 75 - 85
    C : 65 - 75
    D : 50 - 65
    E : 0 - 50
    Hati-hati, bahwa baris pertama list data_nilaimhs adalah header, bukan berisi data nilai mahasiswa. Tambahkan juga header HURUF.

5. Hitunglah berapa mahasiswa angkatan 2019 yang mendapat nilai B
   Gunakan iterasi berikut
   for datanilai in data_nilaimhs[1:12]:
        >>baris proses di sini<<

6. Hitunglah berapa mahasiswa 2020 yang mendapat nilai B
   Gunakan iterasi berikut
   for datanilai in data_nilaimhs[12:]:
        >>baris proses di sini<<

"""

