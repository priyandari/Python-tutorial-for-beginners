def cariMaks(listBilangan):
    bildata = -9999999
    for bil in listBilangan:
        if bil > bildata:
            bildata = bil
    return bildata

def cariMin(listBilangan):
    bildata = 999999999
    for bil in listBilangan:
        if bil < bildata:
            bildata = bil
    return bildata
    # print(bil)

bilangan = [76, 65, 98, 77, 45, 98, 55]

bilMin = cariMin(bilangan)
bilMaks = cariMaks(bilangan)
print('Bilangan Minimum :',bilMin)
print('Bilangan Maksimum :',bilMaks)