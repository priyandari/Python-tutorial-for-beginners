namaBulan = 'JanFebMarAprMeiJunJulAugSepOktNovDes'
k = int(input('Masukkan bulan ke : '))

awal = (k-1)*3
akhir = awal + 3
print(namaBulan[awal:akhir])