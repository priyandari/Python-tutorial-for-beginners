"""gaji_drut = 300000
tun_drut = 800000
gaji_dirall = 250000
tun_dirall = 500000
gaji_staff = 100000
tun_staff = 200000
tun_salmar = 250000
gaji_sec = 90000
tun_sec = 250000"""
gaji_bersih = 0.0

"""
nik, nama, jabatan, hari_normal, absen, kasbon

1. Kita menginput data NIK, NAMA, Jabatan, absen, kasbon untuk seluruh karyawan
   Data ini kita simpan data list/dic
2. Kita sudah memiliki data pegawai dalam bentuk list/dic
3. Kita memiliki data dalam bentuk xlsx data pegawai, kemudian kita baca data pegawai
   kita meminta pengguna untuk menentukan kita akan menghitung gaji siapa
   atau
   bulan April, hari normal untuk staff umum, untuk security    
"""

daftar_pegawai = {
    'k67' : {'nama':"Jono", 'jab':'Sec'},
    'k75': {'nama': "Tono", 'jab': 'Sal'},
    'k37': {'nama': "Andi", 'jab': 'Dpro'}
}

data_jabatan ={
    'Dpro' : {'nama_jabatan' : 'Direktur Produksi', 'gaji_pokok_harian': 250000.0, 'tunj_jabatan': 500000.0},
    'Sal': {'nama_jabatan': 'Sales', 'gaji_pokok_harian': 100000.0, 'tunj_jabatan': 250000.0}
}

nik = input(" Input NIK : ")
hari_normal = int(float(input(" Input hari kerja normal (di bulan perhitungan): ")))
absen = int(float(input(" Input jumlah hari absen : ")))
kasbon = float(input(" Input besaran kasbon : "))

#print(daftar_pegawai[nik])
pegawai = daftar_pegawai[nik]
jabatan = pegawai['jab']

if jabatan.title() == 'Drut':
    #gaji_bersih = (hari_normal - absen) * gaji_drut + tun_drut - kasbon
    gaji_bersih = (hari_normal - absen) * data_jabatan[jabatan]['gaji_pokok_harian'] + data_jabatan[jabatan]['tunj_jabatan'] - kasbon
elif (jabatan.title() == 'Dkeu') or (jabatan.title() == 'Dpem') or (jabatan.title() == 'Dpro'):
    #gaji_bersih = (hari_normal - absen) * gaji_dirall + tun_dirall - kasbon
    gaji_bersih = (hari_normal - absen) * data_jabatan[jabatan]['gaji_pokok_harian'] + data_jabatan[jabatan]['tunj_jabatan'] - kasbon
elif jabatan.title() == 'Sec':
    #gaji_bersih = (hari_normal - absen) * gaji_sec + tun_sec - kasbon
    gaji_bersih = (hari_normal - absen) * data_jabatan[jabatan]['gaji_pokok_harian'] + data_jabatan[jabatan]['tunj_jabatan'] - kasbon
elif (jabatan.title() == 'Sal') or (jabatan.title() == 'Mar'):
    #gaji_bersih = (hari_normal - absen) * gaji_staff + tun_salmar - kasbon
    gaji_bersih = (hari_normal - absen) * data_jabatan[jabatan]['gaji_pokok_harian'] + data_jabatan[jabatan]['tunj_jabatan'] - kasbon
else:
    #gaji_bersih = (hari_normal - absen) * gaji_staff + tun_staff - kasbon
    gaji_bersih = (hari_normal - absen) * data_jabatan[jabatan]['gaji_pokok_harian'] + data_jabatan[jabatan]['tunj_jabatan'] - kasbon

print('|{:<5}|{:<10}|{:>20}|'.format(nik, pegawai['nama'], gaji_bersih))