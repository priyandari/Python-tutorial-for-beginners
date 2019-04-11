from os import system

def CtoR():
    system('cls')
    suhu = float(input("input Suhu (celcius) : "))
    suhubaru = (4/5)*suhu
    print("Suhu ", suhu, "C senilai dengan ", suhubaru, "R" )
    input("Tekan enter untuk lanjut ...")
    # return

while True:
    system('cls')
    print("Menu Program Konversi Suhu :")
    print("____________________________")
    print("1. Celcius ke Reamur")
    print("2. Celcius ke Kelvin")
    print("3. Reamur ke Celcius")
    inputpengguna = input("Pilih (1/2/3 atau (exit) untuk keluar : " )

    if inputpengguna == "1":
        # Kerjakan perintah di sini
        CtoR()
        # print("")    
    elif inputpengguna == "2":
        # Kerjakan perintah di sini
        print("")    
    elif inputpengguna == "3":
        # Kerjakan perintah di sini
        print("")
    elif inputpengguna == "exit":
        # Kerjakan perintah di sini
        print("Selesai")
        break
    else:
        print("Input TIDAK dikenal")